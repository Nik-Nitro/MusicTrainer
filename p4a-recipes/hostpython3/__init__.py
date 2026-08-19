from pythonforandroid.recipe import Recipe
from pythonforandroid.logger import info
import os

class HostPython3Recipe(Recipe):
    name = 'hostpython3'
    version = '3.11'
    url = None

    def should_build(self, arch):
        return False

    def build_arch(self, arch):
        pass

    def get_path_to_python(self):
        # Для GitHub Actions путь к Python 3.11
        return '/opt/hostedtoolcache/Python/3.11.16/x64/bin/python3'

    @property
    def python_exe(self):
        return '/opt/hostedtoolcache/Python/3.11.16/x64/bin/python3'

    @property
    def local_bin(self):
        return '/opt/hostedtoolcache/Python/3.11.16/x64/bin'

    @property
    def site_bin(self):
        return '/opt/hostedtoolcache/Python/3.11.16/x64/bin'

    @property
    def site_dir(self):
        import sys
        for path in sys.path:
            if 'site-packages' in path:
                return path
        return '/opt/hostedtoolcache/Python/3.11.16/x64/lib/python3.11/site-packages'

    @property
    def pip(self):
        import sh
        return sh.Command('/opt/hostedtoolcache/Python/3.11.16/x64/bin/pip3')

    @property
    def python(self):
        import sh
        return sh.Command('/opt/hostedtoolcache/Python/3.11.16/x64/bin/python3')

    def get_build_dir(self, arch_name):
        return os.path.join(self.ctx.build_dir, 'other_builds', 'hostpython3', arch_name)

recipe = HostPython3Recipe()
