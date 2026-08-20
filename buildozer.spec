[app]

title = MusicTrainer
package.name = musictrainer
package.domain = org.niknitro
version = 17.5

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,md
source.exclude_exts = spec,db,pyc,pyo
source.exclude_dirs = tests, __pycache__, .git, .buildozer, to_delete_backup
source.include_patterns = data/*, exercises/*, screens/*, core/*, ui/*

requirements = python3==3.11,kivy==2.1.0,pygame==2.6.1,numpy

hostpython3 = /usr/local/bin/python3.11

p4a.local_recipes = ./p4a-recipes

# Ключевой параметр - игнорируем setup.py проекта
ignore_setup_py = True

orientation = portrait

android.permissions = INTERNET, VIBRATE, RECORD_AUDIO, MODIFY_AUDIO_SETTINGS
android.api = 30
android.minapi = 24
android.ndk_api = 24
android.sdk = 33

# МЕНЯЕМ NDK НА СТАБИЛЬНУЮ ВЕРСИЮ!
android.ndk = 23c  # или 25c, но НЕ 28c!
android.build_tools = 33.0.2
android.archs = arm64-v8a
android.enable_androidx = True
android.auto_sign = True
android.accept_sdk_license = True

[buildozer]

log_level = 2
build_dir = ./.buildozer
bin_dir = ./bin
