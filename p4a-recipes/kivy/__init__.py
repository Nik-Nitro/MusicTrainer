from pythonforandroid.recipe import CythonRecipe
from pythonforandroid.logger import info
import os
import re

class KivyRecipe(CythonRecipe):
    name = 'kivy'
    version = '2.1.0'
    url = 'https://github.com/kivy/kivy/archive/{version}.zip'
    depends = ['python3', 'sdl2', 'pygame']

    def prebuild_arch(self, arch):
        super().prebuild_arch(arch)
        
        build_dir = self.get_build_dir(arch.arch)
        setup_py = os.path.join(build_dir, 'kivy', 'setup.py')
        
        # Модифицируем setup.py, чтобы исключить X11
        if os.path.exists(setup_py):
            with open(setup_py, 'r') as f:
                content = f.read()
            
            # Ищем список window бэкендов и удаляем x11
            # Это примерное решение, нужно смотреть на реальный setup.py
            content = content.replace("'x11'", "''")
            content = content.replace('"x11"', '""')
            
            with open(setup_py, 'w') as f:
                f.write(content)
            info('Modified setup.py to exclude X11')
        
        # Удаляем X11 файлы (на всякий случай)
        window_dir = os.path.join(build_dir, 'kivy', 'core', 'window')
        if os.path.exists(window_dir):
            for f in os.listdir(window_dir):
                if 'x11' in f.lower():
                    os.remove(os.path.join(window_dir, f))
                    info(f'Removed X11 file: {f}')

    def get_recipe_env(self, arch):
        env = super().get_recipe_env(arch)
        env['USE_X11'] = '0'
        env['KIVY_GL_BACKEND'] = 'sdl2'
        return env

recipe = KivyRecipe()
