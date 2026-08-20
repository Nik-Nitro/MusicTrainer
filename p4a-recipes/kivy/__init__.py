from pythonforandroid.recipe import CythonRecipe
from pythonforandroid.logger import info
import os
import shutil

class KivyRecipe(CythonRecipe):
    name = 'kivy'
    version = '2.1.0'
    url = 'https://github.com/kivy/kivy/archive/{version}.zip'
    depends = ['python3', 'sdl2', 'pygame']

    def prebuild_arch(self, arch):
        super().prebuild_arch(arch)
        
        # Удаляем все X11-файлы
        build_dir = self.get_build_dir(arch.arch)
        kivy_dir = os.path.join(build_dir, 'kivy')
        
        # Удаляем все файлы с x11 в названии
        for root, dirs, files in os.walk(kivy_dir):
            for f in files:
                if 'x11' in f.lower():
                    file_path = os.path.join(root, f)
                    info(f'Removing X11 file: {file_path}')
                    os.remove(file_path)
        
        # Удаляем папку window_x11 если есть
        window_dir = os.path.join(kivy_dir, 'core', 'window')
        if os.path.exists(window_dir):
            for f in os.listdir(window_dir):
                if 'x11' in f.lower():
                    file_path = os.path.join(window_dir, f)
                    if os.path.isfile(file_path):
                        info(f'Removing X11 file: {f}')
                        os.remove(file_path)

    def get_recipe_env(self, arch):
        env = super().get_recipe_env(arch)
        env['USE_X11'] = '0'
        env['KIVY_GL_BACKEND'] = 'sdl2'
        return env

recipe = KivyRecipe()
