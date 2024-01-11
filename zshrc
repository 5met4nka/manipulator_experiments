#!/bin/bash

# ROS paths
source /opt/ros/noetic/setup.zsh
source ~/moveit_ws/devel/setup.zsh

# single-machine ROS configuration
export ROS_HOSTNAME=$(hostname).local
export ROS_MASTER_URI=http://localhost:11311
