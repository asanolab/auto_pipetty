cmake_minimum_required(VERSION 3.0.2)
project(auto_pipetty)

find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  roscpp
  rospy
  std_msgs
)

catkin_package()

###########
## Build ##
###########
include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

#############
## Install ##
#############
catkin_install_python(PROGRAMS
  scripts/pipetty_motor_serial.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
  )
