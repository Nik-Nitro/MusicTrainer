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
ignore_setup_py = True

orientation = portrait

android.permissions = INTERNET, VIBRATE, RECORD_AUDIO, MODIFY_AUDIO_SETTINGS
android.api = 30
android.minapi = 24
android.ndk_api = 24
android.sdk = 33
android.ndk = 23c
android.build_tools = 33.0.2
android.archs = arm64-v8a
android.enable_androidx = True
android.auto_sign = True
android.accept_sdk_license = True

# Переменные для отключения X11
android.env = USE_X11=0,KIVY_GL_BACKEND=sdl2,KIVY_NO_X11=1,KIVY_USE_X11=0

[buildozer]

log_level = 2
build_dir = ./.buildozer
bin_dir = ./bin
