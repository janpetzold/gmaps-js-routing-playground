# Cog setup

[Cog](https://github.com/Igalia/cog) is a lightweight browser view without user interface based on WPE-Webkit which is optimized for embedded devices. It seems rather promising for the use case but took me a while to work on my Raspberry computers. See these instructions for a Raspberry Pi 4B and Raspberry Zero 2.

The version I used was cog 0.19.1 based on WPE Webkit 2.38.6 but this will change since it is based on cogs git repo.

## Preparation

Install Bookworm OS on the Raspberry via flashing. When starting the Pi, make sure to activate Wayland in the "Advanced Settings" of `raspi-config`.

## Install

    sudo apt update && sudo apt upgrade
    sudo apt install libwpe-1.0-1 libwpe-1.0-dev libwpewebkit-1.0-3 libwpewebkit-1.0-dev libwpebackend-fdo-1.0-1 libwpebackend-fdo-1.0-dev
    sudo apt install git meson libepoxy-dev libgles2-mesa-dev libwebp-dev libcairo2-dev libglib2.0-dev libjpeg-dev libpng-dev libsqlite3-dev libxt-dev libsoup2.4-dev libnotify-dev libxslt-dev libxml2-dev libxtst-dev libportal-dev libdrm-dev libinput-dev libgbm-dev
    git clone git clone https://github.com/Igalia/cog.git
    cd cog
    meson build
    cd build
    ninja
    sudo ninja install

## Run

For me only the "drm" mode worked.

    cog -P drm -O renderer=gles,rotation=0 https://www.google.com/maps