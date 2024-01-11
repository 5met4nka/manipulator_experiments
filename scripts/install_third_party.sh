#!/bin/bash

# Проверка наличия папки third_party
if [ ! -d "third_party" ]; then
    echo "Error: The folder 'third_party' was not found in the current directory. Execute the script in the 'manipulator_experiments' folder"
    exit 1
fi

# fanuc
git -C third_party clone https://github.com/ros-industrial/fanuc.git -b melodic-devel
