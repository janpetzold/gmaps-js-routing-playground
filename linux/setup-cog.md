# Cog setup

[Cog](https://github.com/Igalia/cog) is a lightweight browser view without user interface based on WPE-Webkit which is optimized for embedded devices. It seems rather promising for the use case but took me a while to work on my Raspberry computers. See these instructions for a Raspberry Pi 4B, Raspberry Zero 2 and Raspberry Zero 1.

## Preparation

Install Bookworm OS on the Raspberry via flashing, Bullseye will also work but then cog release 0.18.3 will be the maxmimum. When starting the Pi, make sure to activate Wayland in the "Advanced Settings" of `raspi-config`.

## Install cog

    sudo apt update && sudo apt upgrade
    sudo apt remove cog
    sudo apt install libwpe-1.0-1 libwpe-1.0-dev libwpewebkit-1.0-3 libwpewebkit-1.0-dev libwpebackend-fdo-1.0-1 libwpebackend-fdo-1.0-dev
    sudo apt install git meson libepoxy-dev libgles2-mesa-dev libwebp-dev libcairo2-dev libglib2.0-dev libjpeg-dev libpng-dev libsqlite3-dev libxt-dev libsoup2.4-dev libnotify-dev libxslt-dev libxml2-dev 
    sudo apt install libdrm-dev libinput-dev libgbm-dev weston libwayland-dev wayland-protocols
    git clone https://github.com/Igalia/cog.git
    cd cog
    meson build
    cd build
    ninja
    sudo ninja install

## Run

For me only the "drm" mode worked on Raspberry 4B.

    ./cog -P drm -O renderer=gles,rotation=0 https://www.google.com/maps

For the Raspberry Zeros I just ran

    ./cog -P drm https://www.google.com/maps

## Performance

The idea of this exercise was to see how the performance (average fps / frames per second) differs between the different Raspis / if my benchmark works at all. Find the results here:

| Browser | HP Probook Laptop (Windows) | Raspberry 4B (Bookworm) | Raspberry Zero 2 (Bullseye) | Raspberry Zero 1 (Bullseye) |
| ----------- | --------------------------- | ----------------------- | --------------------------- | --------------------------- |
| Chromium | 60fps | 40fps | ~5fps (unstable) | Browser does not start |
| cog | Not tested | 30fps | ~9fps (stable) | 3fps