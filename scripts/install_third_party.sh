#!/bin/bash

# Проверка запуска из папки scripts
if [ "$(basename "$(pwd)")" != "scripts" ]; then
    echo "Error: Please execute the script from the 'scripts' folder"
    exit 1
fi

# fanuc
git -C ../third_party clone https://github.com/ros-industrial/fanuc.git -b melodic-devel
git -C ../third_party clone https://github.com/ros-industrial/fanuc_experimental -b melodic-devel

#yaskawa
git -C ../third_party clone https://github.com/ros-industrial/motoman.git -b kinetic-devel
git -C ../third_party clone https://github.com/ros-industrial/motoman_experimental -b kinetic-devel

# abb
git -C ../third_party clone https://github.com/ros-industrial/abb_experimental.git -b kinetic-devel
git -C ../third_party clone https://github.com/ros-industrial/abb.git -b kinetic-devel
git -C ../third_party clone https://github.com/ros-industrial/abb_driver.git -b melodic-devel

# moveit tutorials (source https://docs.ros.org/en/melodic/api/moveit_tutorials/html/doc/getting_started/getting_started.html)
git -C ../third_party clone https://github.com/ros-planning/moveit_tutorials.git -b master
git -C ../third_party clone https://github.com/ros-planning/panda_moveit_config.git -b noetic-devel

# rosserial
git -C ../third_party clone https://github.com/ros-drivers/rosserial.git -b noetic-devel
