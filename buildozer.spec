[app]

# ============================================
# ОСНОВНЫЕ НАСТРОЙКИ
# ============================================

# Название приложения (отображается на экране)
title = MusicTrainer

# Внутреннее имя пакета (только латиница, без пробелов)
package.name = musictrainer

# Домен организации (в обратном порядке)
package.domain = org.niknitro

# Версия приложения
version = 17.5

# ============================================
# ИСХОДНЫЙ КОД
# ============================================

# Папка с main.py (текущая директория)
source.dir = .

# Расширения файлов для включения
source.include_exts = py,png,jpg,kv,atlas,json,md

# Расширения файлов для исключения
source.exclude_exts = spec,db,pyc,pyo

# Папки для исключения
source.exclude_dirs = tests, __pycache__, .git, .buildozer, to_delete_backup

# Папки для включения по шаблону
source.include_patterns = data/*, exercises/*, screens/*, core/*, ui/*

# ============================================
# ЗАВИСИМОСТИ (ВАЖНО!)
# ============================================

# Библиотеки, необходимые для приложения
requirements = python3,kivy==2.3.1,pygame==2.6.1,numpy

# ============================================
# ОРИЕНТАЦИЯ И ВНЕШНИЙ ВИД
# ============================================

# Ориентация экрана: portrait (книжная) или landscape (альбомная)
orientation = portrait

# Заставка при запуске (опционально)
# presplash.filename = %(source.dir)s/data/presplash.png

# Иконка приложения (опционально)
# icon.filename = %(source.dir)s/data/icon.png

# ============================================
# ANDROID НАСТРОЙКИ
# ============================================

# Разрешения Android
android.permissions = INTERNET, VIBRATE, RECORD_AUDIO, MODIFY_AUDIO_SETTINGS

# Целевая версия Android API (31 = Android 12)
android.api = 31

# Минимальная версия Android API (21 = Android 5.0)
android.minapi = 21

# Версия Android SDK
android.sdk = 33

# Версия Android NDK
android.ndk = 23b

# Поддержка AndroidX
android.enable_androidx = True

# Автоподпись APK
android.auto_sign = True

# ============================================
# НАСТРОЙКИ СБОРКИ
# ============================================

[buildozer]

# Уровень логирования (0 = ошибки, 1 = инфо, 2 = подробно)
log_level = 2

# Папка для временных файлов сборки
build_dir = ./.buildozer

# Папка для готовых APK
bin_dir = ./bin
