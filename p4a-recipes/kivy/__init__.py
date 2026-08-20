from pythonforandroid.recipe import PythonRecipe
import os
import re

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
            with open(setup_path, 'w') as f:
                f.write(patch + content)
        
        super().build_arch(arch)

recipe = KivyRecipe()
