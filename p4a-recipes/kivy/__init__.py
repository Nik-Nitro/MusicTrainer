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
        self._remove_x11_files(build_dir)
        info('✅ X11 removed during prebuild')

    def build_arch(self, arch):
        # Вызываем перед сборкой
        build_dir = self.get_build_dir(arch.arch)
        self._remove_x11_files(build_dir)
        info('✅ X11 removed during build')
        
        # Продолжаем сборку
        super().build_arch(arch)

    def _remove_x11_files(self, build_dir):
        window_dir = os.path.join(build_dir, 'kivy', 'core', 'window')
        if os.path.exists(window_dir):
            for f in os.listdir(window_dir):
                if 'x11' in f.lower():
                    file_path = os.path.join(window_dir, f)
                    if os.path.isfile(file_path):
                        os.remove(file_path)
                        info(f'Removed X11 file: {f}')
        
        # Удаляем рекурсивно все X11 файлы
        for root, dirs, files in os.walk(build_dir):
            for f in files:
                if 'x11' in f.lower():
                    file_path = os.path.join(root, f)
                    if os.path.isfile(file_path):
                        os.remove(file_path)
                        info(f'Removed X11 file: {file_path}')

    def get_recipe_env(self, arch):
        env = super().get_recipe_env(arch)
        env['USE_X11'] = '0'
        env['KIVY_GL_BACKEND'] = 'sdl2'
        return env

recipe = KivyRecipe()
