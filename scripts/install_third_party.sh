#!/bin/bash

# Проверка наличия папки third_party
if [ "$(basename "$(pwd)")" != "scripts" ]; then
    echo "Error: Please execute the script from the 'scripts' folder"
    exit 1
fi

# fanuc
git -C ../third_party clone https://github.com/ros-industrial/fanuc.git -b melodic-devel

# abb
git -C ../third_party clone https://github.com/ros-industrial/motoman.git -b kinetic-devel

#yaskawa
git -C ../third_party clone https://github.com/ros-industrial/abb_experimental.git -b kinetic-devel
