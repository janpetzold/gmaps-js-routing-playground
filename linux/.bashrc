# Simplest way is to boot into console and then launch x-server with the basic settings defined in .xinitrc
if [[ "$(tty)" = "/dev/tty1" ]] && [[ $- == *i* ]]; then
    startx
fi