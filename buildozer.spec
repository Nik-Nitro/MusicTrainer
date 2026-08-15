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
# ЗАВИСИМОСТИ
# ============================================

requirements = python3,kivy==2.3.1,pygame==2.6.1,numpy

# ============================================
# ОРИЕНТАЦИЯ
# ============================================

orientation = portrait

# ============================================
# ANDROID НАСТРОЙКИ
# ============================================

# Разрешения
android.permissions = INTERNET, VIBRATE, RECORD_AUDIO, MODIFY_AUDIO_SETTINGS

# API версии
android.api = 31
android.minapi = 21

# SDK и NDK
android.sdk = 33
android.ndk = 23b

# АВТОМАТИЧЕСКОЕ ПРИНЯТИЕ ЛИЦЕНЗИЙ
android.accept_sdk_license = True

# Отключаем автоматическую установку build-tools
android.allow_app_ndk_version_mismatch = True

# Указываем версию build-tools через отдельный параметр
android.build_tools = 33.0.2
android.gradle_dependencies = 
android.add_src = 

# Поддержка архитектур
android.archs = arm64-v8a, armeabi-v7a

# Подпись
android.enable_androidx = True
android.auto_sign = True

# ============================================
# НАСТРОЙКИ СБОРКИ
# ============================================

[buildozer]

log_level = 2
build_dir = ./.buildozer
bin_dir = ./bin
