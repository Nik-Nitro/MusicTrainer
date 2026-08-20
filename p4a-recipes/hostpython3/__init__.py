from pythonforandroid.recipe import Recipe
from pythonforandroid.logger import info
import os
import sh

class HostPython3Recipe(Recipe):
    name = 'hostpython3'
    version = '3.11'
    url = None

    def should_build(self, arch):
        return False

    def build_arch(self, arch):
        pass

    def get_path_to_python(self):
        return '/usr/bin/python3.11'

    @property
    def python_exe(self):
        return '/usr/bin/python3.11'

    @property
    def local_bin(self):
        return '/usr/bin'

    @property
    def site_bin(self):
        return '/usr/bin'

    @property
    def site_dir(self):
        import sys
        for path in sys.path:
            if 'site-packages' in path:
                return path
        return '/usr/lib/python3.11/site-packages'

    @property
    def pip(self):
        return sh.Command('/usr/bin/pip3.11')

    @property
    def python(self):
        return sh.Command('/usr/bin/python3.11')

    def get_build_dir(self, arch_name):
        return os.path.join(self.ctx.build_dir, 'other_builds', 'hostpython3', arch_name)

recipe = HostPython3Recipe()
