name: Build Android APK

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build-android:
    name: Build APK with Buildozer
    runs-on: ubuntu-22.04

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Build with Buildozer
        uses: digreatbrian/buildozer-action@v2
        with:
          python-version: 3.11
          buildozer-cmd: buildozer android debug
          dockerfile: Dockerfile

      - name: Upload APK
        uses: actions/upload-artifact@v4
        with:
          name: musictrainer-apk
          path: bin/*.apk
