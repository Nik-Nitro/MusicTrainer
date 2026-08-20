FROM python:3.11-slim

ENV URL_python3=https://github.com/python/cpython/archive/refs/tags/v3.11.0.tar.gz
ENV USE_X11=0
ENV KIVY_GL_BACKEND=sdl2
ENV KIVY_NO_X11=1
ENV KIVY_USE_X11=0

RUN apt-get update && apt-get install -y \
    git zip unzip wget curl make \
    default-jdk \
    autoconf libtool pkg-config \
    zlib1g-dev libncurses5-dev libncursesw5-dev \
    cmake libffi-dev libssl-dev \
    libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev \
    libgl1-mesa-dev libgles2-mesa-dev \
    portaudio19-dev \
    libblas-dev liblapack-dev gfortran \
    patchelf \
    ninja-build \
    sudo \
    && rm -rf /var/lib/apt/lists/* && apt-get clean

# Создаем пользователя
RUN useradd -m -u 1000 builder && \
    echo "builder ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

USER builder

# Устанавливаем зависимости с фиксированными версиями
RUN pip install --user \
    buildozer==1.6.0 \
    setuptools==69.5.1 \
    wheel==0.43.0 \
    python-for-android==2024.01.21 \
    meson==1.4.0 \
    cython==0.29.37

ENV PATH="/home/builder/.local/bin:${PATH}"

# Создаем рабочую директорию
WORKDIR /app
