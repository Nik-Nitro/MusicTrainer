from pythonforandroid.recipe import PythonRecipe
import os
import re
import glob

class KivyRecipe(PythonRecipe):
    version = '2.1.0'
    url = 'https://github.com/kivy/kivy/archive/{version}.tar.gz'
    
    def get_recipe_env(self, arch):
        env = super().get_recipe_env(arch)
        env['USE_X11'] = '0'
        env['KIVY_GL_BACKEND'] = 'sdl2'
        env['KIVY_NO_X11'] = '1'
        env['KIVY_USE_X11'] = '0'
        env['CFLAGS'] = env.get('CFLAGS', '') + ' -DKIVY_NO_X11 -DUSE_X11=0'
        return env
    
    def build_arch(self, arch):
        build_dir = self.get_build_dir(arch.arch)
        
        # Патчим все .py, .pyx, .pxd файлы от X11
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
                        with open(path, 'w') as f:
                            f.write(content)
                    except:
                        pass
        
        # Удаляем файлы X11
        for pattern in ['**/window_x11.py', '**/window_x11.pyx', '**/window_x11.pxd']:
            for path in glob.glob(f'{build_dir}/{pattern}', recursive=True):
                try:
                    os.remove(path)
                    print(f"Removed X11 file: {path}")
                except:
                    pass
        
        # Патчим setup.py
        setup_path = f'{build_dir}/setup.py'
        if os.path.exists(setup_path):
            with open(setup_path, 'r') as f:
                content = f.read()
            patch = '''
import os
os.environ['USE_X11'] = '0'
os.environ['KIVY_GL_BACKEND'] = 'sdl2'
os.environ['KIVY_NO_X11'] = '1'
os.environ['KIVY_USE_X11'] = '0'
'''
            content = patch + content
            content = re.sub(r'use_x11\s*=\s*True', 'use_x11 = False', content)
            with open(setup_path, 'w') as f:
                f.write(content)
            print(f"Patched setup.py at: {setup_path}")
        
        super().build_arch(arch)

recipe = KivyRecipe()
