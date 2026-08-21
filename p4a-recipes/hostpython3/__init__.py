from pythonforandroid.recipe import Recipe
from pythonforandroid.logger import info
import os
import sys
import subprocess

class HostPython3Recipe(Recipe):
    name = 'hostpython3'
    version = '3.11.0'
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

    @property
    def pip(self):
        def pip_command(*args, **kwargs):
            info(f'HostPython3: pip called with args: {args}')
            info(f'HostPython3: pip called with kwargs: {kwargs}')
            
            cmd = ['/usr/local/bin/pip3.11'] + list(args)
            
            # Извлекаем _env
            env = kwargs.pop('_env', None)
            if env:
                new_env = os.environ.copy()
                new_env.update(env)
                kwargs['env'] = new_env
            
            # ИГНОРИРУЕМ ВСЕ СПЕЦИАЛЬНЫЕ ПАРАМЕТРЫ P4A
            kwargs.pop('_iter', None)
            kwargs.pop('_spawn', None)
            kwargs.pop('_bg', None)
            kwargs.pop('_tee', None)
            kwargs.pop('_fg', None)
            kwargs.pop('_out_bufsize', None)      # <-- ДОБАВЛЕНО!
            kwargs.pop('_err_to_out', None)       # <-- ДОБАВЛЕНО!
            kwargs.pop('_env', None)
            kwargs.pop('_timeout', None)
            kwargs.pop('_cwd', None)
            kwargs.pop('_hide', None)
            kwargs.pop('_long', None)
            kwargs.pop('_ok_code', None)
            kwargs.pop('_with', None)
            kwargs.pop('_piped', None)
            
            info(f'HostPython3: pip final cmd: {cmd}')
            info(f'HostPython3: pip final kwargs: {kwargs}')
            
            return subprocess.check_call(cmd, **kwargs)
        return pip_command

    @property
    def python(self):
        def python_command(*args, **kwargs):
            cmd = [self.get_path_to_python()] + list(args)
            env = kwargs.pop('_env', None)
            if env:
                new_env = os.environ.copy()
                new_env.update(env)
                kwargs['env'] = new_env
            
            # ИГНОРИРУЕМ ВСЕ СПЕЦИАЛЬНЫЕ ПАРАМЕТРЫ P4A
            kwargs.pop('_iter', None)
            kwargs.pop('_spawn', None)
            kwargs.pop('_bg', None)
            kwargs.pop('_tee', None)
            kwargs.pop('_fg', None)
            kwargs.pop('_out_bufsize', None)      # <-- ДОБАВЛЕНО!
            kwargs.pop('_err_to_out', None)       # <-- ДОБАВЛЕНО!
            kwargs.pop('_env', None)
            kwargs.pop('_timeout', None)
            kwargs.pop('_cwd', None)
            kwargs.pop('_hide', None)
            kwargs.pop('_long', None)
            kwargs.pop('_ok_code', None)
            kwargs.pop('_with', None)
            kwargs.pop('_piped', None)
            
            return subprocess.check_call(cmd, **kwargs)
        return python_command

    def get_build_dir(self, arch_name):
        return os.path.join(self.ctx.build_dir, 'other_builds', 'hostpython3', arch_name)

recipe = HostPython3Recipe()
