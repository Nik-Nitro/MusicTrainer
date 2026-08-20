from pythonforandroid.recipe import PythonRecipe
from pythonforandroid.util import ensure_dir
import os
import shutil
import glob
import subprocess

class KivyRecipe(PythonRecipe):
    version = '2.1.0'
    url = 'https://github.com/kivy/kivy/archive/{version}.tar.gz'
    
    # Отключаем X11 на всех уровнях
    def get_recipe_env(self, arch):
        env = super().get_recipe_env(arch)
        
        # Ключевые переменные для отключения X11
        env['USE_X11'] = '0'
        env['KIVY_GL_BACKEND'] = 'sdl2'
        env['KIVY_NO_X11'] = '1'
        env['KIVY_USE_SDL2'] = '1'
        env['KIVY_USE_X11'] = '0'
        
        # Добавляем флаги компиляции
        cflags = env.get('CFLAGS', '')
        cflags += ' -DKIVY_NO_X11 -DUSE_X11=0'
        env['CFLAGS'] = cflags
        
        return env
    
    def build_arch(self, arch):
        # Сначала патчим setup.py
        setup_py = self.get_build_dir(arch.arch) + '/setup.py'
        if os.path.exists(setup_py):
            with open(setup_py, 'r') as f:
                content = f.read()
            
            # Добавляем отключение X11 в начало setup.py
            patch = '''
import os
os.environ['USE_X11'] = '0'
os.environ['KIVY_GL_BACKEND'] = 'sdl2'
os.environ['KIVY_NO_X11'] = '1'
os.environ['KIVY_USE_X11'] = '0'
'''
            content = patch + content
            
            with open(setup_py, 'w') as f:
                f.write(content)
        
        # Патчим все .pyx файлы
        build_dir = self.get_build_dir(arch.arch)
        for root, dirs, files in os.walk(build_dir):
            for file in files:
                if file.endswith('.pyx') or file.endswith('.py'):
                    filepath = os.path.join(root, file)
                    with open(filepath, 'r') as f:
                        content = f.read()
                    
                    # Заменяем все упоминания X11
                    content = content.replace('USE_X11', 'USE_X11_DISABLED')
                    content = content.replace('KIVY_USE_X11', 'KIVY_USE_X11_DISABLED')
                    
                    with open(filepath, 'w') as f:
                        f.write(content)
        
        super().build_arch(arch)
        
        # После сборки чистим ссылки на X11 в библиотеках
        lib_dir = self.get_build_dir(arch.arch) + '/kivy'
        if os.path.exists(lib_dir):
            so_files = glob.glob(f"{lib_dir}/**/*.so", recursive=True)
            for so in so_files:
                try:
                    # Пытаемся удалить ссылки на X11 из .so файлов
                    subprocess.run([
                        'patchelf', '--remove-needed', 'libX11.so', so
                    ], capture_output=True)
                except:
                    pass

recipe = KivyRecipe()
