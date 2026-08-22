from pythonforandroid.recipe import PythonRecipe
from pythonforandroid.logger import info
import os

class NumpyRecipe(PythonRecipe):
    version = '1.26.4'
    # ИСПРАВЛЯЕМ URL НА ПРАВИЛЬНЫЙ
    url = 'https://files.pythonhosted.org/packages/source/n/numpy/numpy-{version}.tar.gz'
    depends = ['python3', 'hostpython3']
    
    def get_recipe_env(self, arch):
        env = super().get_recipe_env(arch)
        
        # Отключаем BLAS/LAPACK для упрощения сборки на Android
        env['NPY_BLAS_ORDER'] = ''
        env['NPY_LAPACK_ORDER'] = ''
        env['ATLAS'] = 'None'
        
        # Флаги для кросс-компиляции
        env['CFLAGS'] = env.get('CFLAGS', '') + ' -O2 -fPIC'
        
        info(f'NumpyRecipe: Setting up environment for {arch}')
        return env
    
    def build_arch(self, arch):
        info(f'NumpyRecipe: Building for {arch}')
        super().build_arch(arch)
        info(f'NumpyRecipe: Build completed for {arch}')

recipe = NumpyRecipe()
