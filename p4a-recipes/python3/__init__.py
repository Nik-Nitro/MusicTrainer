from pythonforandroid.recipe import Recipe
from pythonforandroid.logger import info
import os

class Python3Recipe(Recipe):
    name = 'python3'
    version = '3.11.0'
    url = 'https://github.com/python/cpython/archive/refs/tags/v3.11.0.tar.gz'

    def download_if_necessary(self):
        download_url = 'https://github.com/python/cpython/archive/refs/tags/v3.11.0.tar.gz'
        target = os.path.join(self.ctx.packages_path, 'python3', 'v3.11.0.tar.gz')
        os.makedirs(os.path.dirname(target), exist_ok=True)

        if os.path.exists(target):
            info('Python3 already downloaded')
            return

        info('Downloading Python3 from {}'.format(download_url))
        self.download_file(download_url, target)

    def get_recipe_env(self, arch):
        env = super().get_recipe_env(arch)
        env['PYTHON_VERSION'] = '3.11'
        return env

    def include_root(self, arch):
        """Возвращает путь к заголовочным файлам Python."""
        # arch может быть объектом или строкой
        arch_name = arch.arch if hasattr(arch, 'arch') else arch
        return os.path.join(
            self.get_build_dir(arch_name),
            'android-build', 'android-root', 'include', 'python3.11'
        )

    def get_build_dir(self, arch_name):
        return os.path.join(
            self.ctx.build_dir, 'other_builds', 'python3',
            arch_name + '__ndk_target_' + str(self.ctx.ndk_api)
        )

recipe = Python3Recipe()
