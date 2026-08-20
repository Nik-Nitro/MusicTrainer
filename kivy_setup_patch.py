import os

# Отключаем X11
os.environ['USE_X11'] = '0'
os.environ['KIVY_GL_BACKEND'] = 'sdl2'
os.environ['KIVY_NO_X11'] = '1'
os.environ['KIVY_USE_X11'] = '0'

from setuptools import setup
setup()
