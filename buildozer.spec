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

requirements = python3,kivy==2.3.1,pygame==2.6.1,numpy

orientation = portrait

android.permissions = INTERNET, VIBRATE, RECORD_AUDIO, MODIFY_AUDIO_SETTINGS
android.api = 31
android.minapi = 21
android.sdk = 33
android.ndk = 23b
android.build_tools = 33.0.2
android.archs = arm64-v8a, armeabi-v7a
android.enable_androidx = True
android.auto_sign = True

[buildozer]

log_level = 2
build_dir = ./.buildozer
bin_dir = ./bin
