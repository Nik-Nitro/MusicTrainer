from pythonforandroid.recipe import CythonRecipe
from pythonforandroid.logger import info
import os

class KivyRecipe(CythonRecipe):
    name = 'kivy'
    version = '2.1.0'
    url = 'https://github.com/kivy/kivy/archive/{version}.zip'
    depends = ['python3', 'sdl2', 'pygame']

    def get_recipe_env(self, arch):
        env = super().get_recipe_env(arch)
        
        # Жестко отключаем X11 через макросы препроцессора
        env['CFLAGS'] = env.get('CFLAGS', '') + ' -DUSE_X11=0'
        env['CXXFLAGS'] = env.get('CXXFLAGS', '') + ' -DUSE_X11=0'
        
        # Даем понять системе сборки, что мы используем SDL2
        env['KIVY_GL_BACKEND'] = 'sdl2'
        env['USE_X11'] = '0'
        
        return env

recipe = KivyRecipe()
