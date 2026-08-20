from pythonforandroid.recipe import Recipe
from pythonforandroid.logger import info
import os
import sys

class HostPython3Recipe(Recipe):
    name = 'hostpython3'
    version = '3.11'
    url = None
    
    def should_build(self, arch):
        return False

    def download_if_necessary(self):
        info('HostPython3: using system python, skipping download')
        return

    def download(self):
        info('HostPython3: using system python, skipping download')
        return

    def build_arch(self, arch):
        info('HostPython3: using system python, skipping build')
        return

    def get_path_to_python(self):
        # Используем Python 3.11 из контейнера
        python_path = '/usr/local/bin/python3.11'
        if os.path.exists(python_path):
            info(f'HostPython3: found python at {python_path}')
            return python_path
        # fallback
        return sys.executable

    def get_build_dir(self, arch_name):
        return os.path.join(self.ctx.build_dir, 'other_builds', 'hostpython3', arch_name)

recipe = HostPython3Recipe()
