from pythonforandroid.recipe import MesonRecipe
from pythonforandroid.logger import info
import os

class KivyRecipe(MesonRecipe):
    name = 'kivy'
    version = '2.1.0'
    url = 'https://github.com/kivy/kivy/archive/{version}.zip'
    depends = ['python3', 'sdl2', 'pygame']

    def get_recipe_env(self, arch):
        env = super().get_recipe_env(arch)
        
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

    def get_meson_options(self, arch):
        """Возвращает опции для Meson"""
        return [
            '-Duse_x11=disabled',
            '-Duse_sdl2=enabled',
            '-Dgl_backend=sdl2',
            f'-Dpython_include_dir={self.ctx.get_python_install_dir(arch.arch)}/android-build/android-root/include/python3.11',
        ]

recipe = KivyRecipe()
