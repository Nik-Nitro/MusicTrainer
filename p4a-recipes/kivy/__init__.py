from pythonforandroid.recipe import PythonRecipe
import os
import re
import glob

class KivyRecipe(PythonRecipe):
    version = '2.1.0'  # <-- ВОЗВРАЩАЕМ 2.1.0
    url = 'https://github.com/kivy/kivy/archive/{version}.tar.gz'
    
    def get_recipe_env(self, arch):
        env = super().get_recipe_env(arch)
        
        env['USE_X11'] = '0'
        env['KIVY_GL_BACKEND'] = 'sdl2'
        env['KIVY_NO_X11'] = '1'
        env['KIVY_USE_X11'] = '0'
        env['KIVY_GRAPHICS'] = 'gles'
        env['KIVY_GLES'] = '1'
        env['KIVY_GLES2'] = '1'
        env['USE_GLES2'] = '1'
        env['KIVY_USE_GLES2'] = '1'
        
        cflags = env.get('CFLAGS', '')
        cflags += ' -DKIVY_NO_X11 -DUSE_X11=0 -DKIVY_GLES2=1 -DKIVY_GLES=1 -DUSE_GLES2=1 -DKIVY_USE_GLES2=1'
        env['CFLAGS'] = cflags
        
        return env
    
    def build_arch(self, arch):
        build_dir = self.get_build_dir(arch.arch)
        print(f"=== KIVY: Building for {arch} in {build_dir} ===")
        
        if not os.path.exists(build_dir):
            print(f"=== KIVY: ERROR - build_dir does not exist! ===")
            return
        
        # ============================================================
        # ПАТЧИМ gl_redirect.h
        # ============================================================
        gl_redirect_path = os.path.join(build_dir, 'kivy', 'include', 'gl_redirect.h')
        if os.path.exists(gl_redirect_path):
            print(f"=== KIVY: Patching gl_redirect.h ===")
            with open(gl_redirect_path, 'r') as f:
                content = f.read()
            content = re.sub(r'#include <GL/gl.h>', '#include <GLES2/gl2.h>', content)
            content = re.sub(r'#include <GL/glu.h>', '// GLU not needed on Android', content)
            content = re.sub(r'#include <GL/glext.h>', '#include <GLES2/gl2ext.h>', content)
            content = re.sub(r'#include <GL/glcorearb.h>', '// GLcore not needed on Android', content)
            content = re.sub(r'#ifdef USE_GLES2', '#if 1 // USE_GLES2 forced for Android', content)
            content = re.sub(r'#ifndef USE_GLES2', '#if 0 // USE_GLES2 forced for Android', content)
            with open(gl_redirect_path, 'w') as f:
                f.write(content)
            print("=== KIVY: gl_redirect.h patched ===")
        else:
            print(f"=== KIVY: WARNING - gl_redirect.h not found ===")
        
        # ============================================================
        # СОЗДАЕМ ЗАГЛУШКИ ДЛЯ GL/gl.h
        # ============================================================
        gl_dir = os.path.join(build_dir, 'kivy', 'include', 'GL')
        os.makedirs(gl_dir, exist_ok=True)
        
        for header in ['gl.h', 'glext.h', 'glu.h']:
            path = os.path.join(gl_dir, header)
            with open(path, 'w') as f:
                f.write(f'''/* {header} stub for Android */
#ifndef __{header.upper().replace('.', '_')}_STUB__
#define __{header.upper().replace('.', '_')}_STUB__
#ifdef __ANDROID__
#include <GLES2/gl2.h>
#else
#error "Use GLES2 on Android"
#endif
#endif
''')
            print(f"=== KIVY: Created GL/{header} stub ===")
        
        # ============================================================
        # ПАТЧИМ ВСЕ .py, .pyx, .pxd файлы
        # ============================================================
        for root, dirs, files in os.walk(build_dir):
            for file in files:
                if file.endswith(('.py', '.pyx', '.pxd')):
                    path = os.path.join(root, file)
                    try:
                        with open(path, 'r') as f:
                            content = f.read()
                        content = re.sub(r'USE_X11\s*=\s*[10]', 'USE_X11 = 0', content)
                        content = re.sub(r'KIVY_USE_X11\s*=\s*[10]', 'KIVY_USE_X11 = 0', content)
                        content = re.sub(r'if\s+USE_X11\s*:', 'if False:', content)
                        content = re.sub(r'elif\s+USE_X11\s*:', 'elif False:', content)
                        content = re.sub(r'USE_GLES2\s*=\s*[10]', 'USE_GLES2 = 1', content)
                        content = re.sub(r'KIVY_GLES2\s*=\s*[10]', 'KIVY_GLES2 = 1', content)
                        content = re.sub(r'KIVY_GLES\s*=\s*[10]', 'KIVY_GLES = 1', content)
                        with open(path, 'w') as f:
                            f.write(content)
                    except:
                        pass
        
        # ============================================================
        # УДАЛЯЕМ X11 ФАЙЛЫ
        # ============================================================
        for pattern in ['**/window_x11.py', '**/window_x11.pyx', '**/window_x11.pxd']:
            for path in glob.glob(f'{build_dir}/{pattern}', recursive=True):
                try:
                    os.remove(path)
                    print(f"Removed X11 file: {path}")
                except:
                    pass
        
        # ============================================================
        # ПАТЧИМ setup.py
        # ============================================================
        setup_path = os.path.join(build_dir, 'setup.py')
        if os.path.exists(setup_path):
            with open(setup_path, 'r') as f:
                content = f.read()
            patch = '''
import os
os.environ['USE_X11'] = '0'
os.environ['KIVY_GL_BACKEND'] = 'sdl2'
os.environ['KIVY_NO_X11'] = '1'
os.environ['KIVY_USE_X11'] = '0'
os.environ['KIVY_GRAPHICS'] = 'gles'
os.environ['KIVY_GLES2'] = '1'
os.environ['KIVY_GLES'] = '1'
os.environ['USE_GLES2'] = '1'
os.environ['KIVY_USE_GLES2'] = '1'
'''
            content = patch + content
            content = re.sub(r'use_x11\s*=\s*True', 'use_x11 = False', content)
            content = re.sub(r'use_gles\s*=\s*False', 'use_gles = True', content)
            with open(setup_path, 'w') as f:
                f.write(content)
            print(f"=== KIVY: setup.py patched ===")
        
        # ============================================================
        # ПАТЧИМ kivy/__init__.py
        # ============================================================
        init_path = os.path.join(build_dir, 'kivy', '__init__.py')
        if os.path.exists(init_path):
            with open(init_path, 'r') as f:
                content = f.read()
            patch = '''
import os
os.environ['USE_X11'] = '0'
os.environ['KIVY_GL_BACKEND'] = 'sdl2'
os.environ['KIVY_NO_X11'] = '1'
os.environ['KIVY_USE_X11'] = '0'
os.environ['KIVY_GRAPHICS'] = 'gles'
os.environ['KIVY_GLES2'] = '1'
os.environ['KIVY_GLES'] = '1'
'''
            if 'USE_X11' not in content:
                content = patch + content
            with open(init_path, 'w') as f:
                f.write(content)
            print(f"=== KIVY: kivy/__init__.py patched ===")
        
        # ============================================================
        # ЗАПУСКАЕМ СТАНДАРТНУЮ СБОРКУ
        # ============================================================
        print("=== KIVY: Calling super().build_arch() ===")
        try:
            super().build_arch(arch)
            print("=== KIVY: super().build_arch() completed successfully ===")
        except Exception as e:
            print(f"=== KIVY: super().build_arch() failed: {e} ===")
            raise

recipe = KivyRecipe()
