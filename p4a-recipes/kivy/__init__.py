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
        
        # 1. Явно запрещаем pkg-config искать X11
        ndk_sysroot = self.ctx.ndk.sysroot
        env['PKG_CONFIG_LIBDIR'] = f'{ndk_sysroot}/usr/lib/pkgconfig'
        
        # 2. Переопределяем CFLAGS, чтобы компилятор НЕ лез в /usr/include
        env['CFLAGS'] = (
            f'-target aarch64-linux-android24 '
            f'-fPIC '
            f'-I{ndk_sysroot}/usr/include '
            f'-I{ndk_sysroot}/usr/include/aarch64-linux-android '
            f'-I{self.ctx.get_python_install_dir(arch.arch)}/android-build/android-root/include/python3.11'
        )
        env['CXXFLAGS'] = env['CFLAGS']
        
        # 3. Отключаем X11 через переменные
        env['USE_X11'] = '0'
        env['KIVY_GL_BACKEND'] = 'sdl2'
        
        return env

recipe = KivyRecipe()
