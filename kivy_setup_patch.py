import os
import sys
from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext

# Переопределяем поиск библиотек
os.environ['USE_X11'] = '0'
os.environ['KIVY_GL_BACKEND'] = 'sdl2'
os.environ['KIVY_NO_X11'] = '1'
os.environ['KIVY_USE_SDL2'] = '1'

class CustomBuildExt(build_ext):
    def build_extensions(self):
        # Удаляем все ссылки на X11 из линковки
        for ext in self.extensions:
            if hasattr(ext, 'libraries'):
                if 'X11' in ext.libraries:
                    ext.libraries.remove('X11')
                if 'x11' in ext.libraries:
                    ext.libraries.remove('x11')
            if hasattr(ext, 'extra_link_args'):
                ext.extra_link_args = [
                    arg for arg in ext.extra_link_args 
                    if 'X11' not in arg and 'x11' not in arg
                ]
        super().build_extensions()

# Подменяем команду build_ext
setup(
    cmdclass={
        'build_ext': CustomBuildExt,
    },
)
