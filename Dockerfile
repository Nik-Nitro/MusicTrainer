FROM python:3.11-slim

ENV PYTHON_VERSION=3.11 \
    LANG=C.UTF-8 \
    LC_ALL=C.UTF-8 \
    DEBIAN_FRONTEND=noninteractive \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    HOSTPYTHON=/usr/local/bin/python3.11 \
    HOSTPYTHON_VERSION=3.11 \
    ANDROID_HOME=/home/builder/.buildozer/android/platform/android-sdk \
    ANDROID_SDK_ROOT=/home/builder/.buildozer/android/platform/android-sdk \
    URL_python3=https://github.com/python/cpython/archive/refs/tags/v3.11.0.tar.gz

RUN python3 --version && echo "Python version is 3.11"

RUN apt-get update && apt-get install -y \
    git zip unzip wget curl make \
    default-jdk \
    autoconf libtool pkg-config \
    zlib1g-dev libncurses5-dev libncursesw5-dev \
    cmake libffi-dev libssl-dev \
    libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev \
    libgl1-mesa-dev \
    portaudio19-dev \
    libblas-dev liblapack-dev gfortran \
    patchelf \
    ninja-build \
    sudo \
    && rm -rf /var/lib/apt/lists/* && apt-get clean

RUN ln -sf /usr/local/bin/python3.11 /usr/local/bin/python3

RUN git config --global http.postBuffer 524288000 && \
    git config --global http.lowSpeedLimit 0 && \
    git config --global http.lowSpeedTime 999999

RUN pip install --no-cache-dir \
    buildozer==1.6.0 \
    setuptools==69.5.1 \
    wheel==0.43.0 \
    python-for-android==2024.01.21 \
    meson==1.4.0 \
    cython==0.29.37

RUN python3 -c "import sys; print(f'Python {sys.version}')" && pip list --version

RUN useradd -m -u 1000 builder \
    && mkdir -p /home/builder/.buildozer \
    && mkdir -p /home/builder/.android \
    && touch /home/builder/.buildozer/default.spec \
    && echo "### User Sources for Android SDK Manager" > /home/builder/.android/repositories.cfg \
    && chown -R builder:builder /home/builder \
    && chmod -R 755 /home/builder \
    && echo "builder ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

USER builder
WORKDIR /app

RUN git config --global --add safe.directory '*' \
    && git config --global user.email "builder@local" \
    && git config --global user.name "Builder" \
    && git config --global http.postBuffer 524288000

ENV TERM=xterm-256color \
    USE_X11=0 \
    KIVY_GL_BACKEND=sdl2 \
    KIVY_NO_X11=1 \
    KIVY_USE_X11=0
