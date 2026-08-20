from pythonforandroid.recipe import Recipe
from pythonforandroid.logger import info
from pythonforandroid.util import shprint
import os
import sys
import subprocess

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
        python_path = '/usr/local/bin/python3.11'
        if os.path.exists(python_path):
            info(f'HostPython3: found python at {python_path}')
            return python_path
        return sys.executable

    @property
    def python_exe(self):
        return self.get_path_to_python()

    @property
    def local_bin(self):
        return '/usr/local/bin'

    @property
    def site_bin(self):
        return '/usr/local/bin'

    @property
    def site_dir(self):
        for path in sys.path:
            if 'site-packages' in path:
                return path
        return '/usr/local/lib/python3.11/site-packages'

    # ИСПРАВЛЯЕМ: pip должен быть функцией
    @property
    def pip(self):
        def pip_command(*args, **kwargs):
            """Запускает pip3.11 с переданными аргументами"""
            cmd = ['/usr/local/bin/pip3.11'] + list(args)
            return subprocess.check_call(cmd, **kwargs)
        return pip_command

    @property
    def python(self):
        def python_command(*args, **kwargs):
            """Запускает python3.11 с переданными аргументами"""
            cmd = [self.get_path_to_python()] + list(args)
            return subprocess.check_call(cmd, **kwargs)
        return python_command

    def get_build_dir(self, arch_name):
        return os.path.join(self.ctx.build_dir, 'other_builds', 'hostpython3', arch_name)

recipe = HostPython3Recipe()
