from pythonforandroid.recipe import PythonRecipe
from pythonforandroid.logger import info
import os

class Python3Recipe(PythonRecipe):
    name = 'python3'
    version = '3.11.0'
    url = 'https://github.com/python/cpython/archive/refs/tags/v3.11.0.tar.gz'
    # depends убираем, чтобы избежать цикла

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

recipe = Python3Recipe()
