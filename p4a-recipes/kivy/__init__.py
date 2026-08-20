from pythonforandroid.recipe import CythonRecipe
from pythonforandroid.logger import info
import os

class KivyRecipe(CythonRecipe):
    name = 'kivy'
    version = '2.1.0'
    url = 'https://github.com/kivy/kivy/archive/{version}.zip'
    depends = ['python3', 'sdl2', 'pygame']

    def prebuild_arch(self, arch):
        super().prebuild_arch(arch)
        
        build_dir = self.get_build_dir(arch.arch)
        info(f'Build dir: {build_dir}')
        
        # Ищем и удаляем все X11 файлы
        for root, dirs, files in os.walk(build_dir):
            for f in files:
                if 'x11' in f.lower():
                    file_path = os.path.join(root, f)
                    info(f'Removing X11 file: {file_path}')
                    os.remove(file_path)
        
        # Создаём заглушку для window_x11.pyx
        window_dir = os.path.join(build_dir, 'kivy', 'core', 'window')
        if os.path.exists(window_dir):
            dummy_path = os.path.join(window_dir, 'window_x11.pyx')
            with open(dummy_path, 'w') as f:
                f.write('# Dummy file to prevent X11 compilation\n')

    def get_recipe_env(self, arch):
        env = super().get_recipe_env(arch)
        env['USE_X11'] = '0'
        env['KIVY_GL_BACKEND'] = 'sdl2'
        return env

recipe = KivyRecipe()
