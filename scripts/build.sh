#!/bin/bash

catkin build \
    moveit \
    moveit_msgs \
    moveit_resources \
    moveit_tutorials \
    moveit_visual_tools \
    fanuc \
    fanuc_experimental \
    -j$(($(nproc)-2))

# widowx_arm_ikfast_plugin
# widowx_block_manipulation
