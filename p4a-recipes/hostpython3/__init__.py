from pythonforandroid.recipe import Recipe
from pythonforandroid.logger import info
import os
import sh
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
        pass

    def get_path_to_python(self):
        # Пытаемся найти Python в системе
        for path in ['/usr/bin/python3.11', '/usr/bin/python3', '/home/user/.venv/bin/python3']:
            if os.path.exists(path):
                info(f'HostPython3: found python at {path}')
                return path
        # Если не нашли - используем sys.executable
        info(f'HostPython3: using sys.executable: {sys.executable}')
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
        import sys
        for path in sys.path:
            if 'site-packages' in path:
                return path
        return '/usr/local/lib/python3.11/site-packages'

    @property
    def pip(self):
        return sh.Command(self.get_path_to_python(), '-m', 'pip')

    @property
    def python(self):
        return sh.Command(self.get_path_to_python())

    def get_build_dir(self, arch_name):
        return os.path.join(self.ctx.build_dir, 'other_builds', 'hostpython3', arch_name)

recipe = HostPython3Recipe()
