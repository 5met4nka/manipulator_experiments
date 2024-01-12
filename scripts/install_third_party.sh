#!/bin/bash

# Проверка запуска из папки scripts
if [ "$(basename "$(pwd)")" != "scripts" ]; then
    echo "Error: Please execute the script from the 'scripts' folder"
    exit 1
fi

# fanuc
git -C ../third_party clone https://github.com/ros-industrial/fanuc.git -b melodic-devel

#yaskawa
git -C ../third_party clone https://github.com/ros-industrial/motoman.git -b kinetic-devel

# abb
git -C ../third_party clone https://github.com/ros-industrial/abb_experimental.git -b kinetic-devel
git -C ../third_party clone https://github.com/ros-industrial/abb.git -b kinetic-devel

sudo apt-get update && sudo apt-get install -y \
    ros-$ROS_DISTRO-moveit