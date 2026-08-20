name: Build Android APK

on:
  push:
    branches: [ main ]
  workflow_dispatch:

jobs:
  build-android:
    name: Build APK with Buildozer
    runs-on: ubuntu-22.04

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Build APK
        run: |
          docker run --rm \
            -v "$PWD:/home/user/hostcwd" \
            -w /home/user/hostcwd \
            -e USE_X11=0 \
            -e KIVY_GL_BACKEND=sdl2 \
            -e KIVY_NO_X11=1 \
            -e KIVY_USE_X11=0 \
            --entrypoint /bin/bash \
            kivy/buildozer:latest \
            -c "
              cd /home/user/hostcwd
              # Проверяем файлы
              echo '=== Checking files ==='
              ls -la
              echo '=== Checking buildozer.spec ==='
              head -20 buildozer.spec || echo 'buildozer.spec not found!'
              echo '=== Run buildozer ==='
              buildozer android debug --verbose
            "

      - name: Upload APK
        if: success()
        uses: actions/upload-artifact@v4
        with:
          name: musictrainer-apk
          path: bin/*.apk
          if-no-files-found: error

      - name: Upload build log
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: build-log
          path: build.log
          if-no-files-found: warn
