[app]

# ============================================
# ОСНОВНЫЕ НАСТРОЙКИ
# ============================================

title = MusicTrainer
package.name = musictrainer
package.domain = org.niknitro
version = 17.5

# ============================================
# ИСХОДНЫЙ КОД
# ============================================

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,md
source.exclude_exts = spec,db,pyc,pyo
source.exclude_dirs = tests, __pycache__, .git, .buildozer, to_delete_backup
source.include_patterns = data/*, exercises/*, screens/*, core/*, ui/*

# ============================================
# ЗАВИСИМОСТИ (ВАЖНО!)
# ============================================

# Фиксируем версии для стабильности
requirements = python3==3.11.0,kivy==2.1.0,pygame==2.6.1,numpy

hostpython3 = /usr/local/bin/python3.11

# ============================================
# ЛОКАЛЬНЫЕ РЕЦЕПТЫ
# ============================================

p4a.local_recipes = ./p4a-recipes

# ============================================
# ОРИЕНТАЦИЯ
# ============================================

orientation = portrait

# ============================================
# ANDROID НАСТРОЙКИ
# ============================================

android.permissions = INTERNET, VIBRATE, RECORD_AUDIO, MODIFY_AUDIO_SETTINGS
android.api = 30
android.minapi = 24
android.ndk_api = 24
android.sdk = 33

# ИСПРАВЛЯЕМ: используем 28c (как в Dockerfile)
android.ndk = 28c

# ИСПРАВЛЯЕМ: явно указываем build-tools
android.build_tools = 33.0.2
android.archs = arm64-v8a, armeabi-v7a
android.enable_androidx = True
android.auto_sign = True
android.accept_sdk_license = True

[buildozer]

log_level = 2
build_dir = ./.buildozer
bin_dir = ./bin
