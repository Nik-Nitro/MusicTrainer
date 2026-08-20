from pythonforandroid.recipe import MesonRecipe
from pythonforandroid.logger import info
import os

class KivyRecipe(MesonRecipe):
    name = 'kivy'
    version = '2.1.0'
    url = 'https://github.com/kivy/kivy/archive/{version}.zip'
    depends = ['python3', 'sdl2', 'pygame']

    def get_recipe_env(self, arch, with_flags_in_cc=True):
        env = super().get_recipe_env(arch, with_flags_in_cc=with_flags_in_cc)
        
        # Отключаем X11
        env['USE_X11'] = '0'
        env['KIVY_GL_BACKEND'] = 'sdl2'
        
        # Добавляем флаги для кросс-компиляции
        ndk_sysroot = self.ctx.ndk.sysroot
        env['CFLAGS'] = env.get('CFLAGS', '') + f' -I{ndk_sysroot}/usr/include'
        env['CXXFLAGS'] = env.get('CXXFLAGS', '') + f' -I{ndk_sysroot}/usr/include'
        
        # Добавляем путь к Python include
        python_include = os.path.join(
            self.ctx.get_python_install_dir(arch.arch),
            'android-build', 'android-root', 'include', 'python3.11'
        )
        env['CFLAGS'] = env.get('CFLAGS', '') + f' -I{python_include}'
        env['CXXFLAGS'] = env.get('CXXFLAGS', '') + f' -I{python_include}'
        
        return env

recipe = KivyRecipe()
