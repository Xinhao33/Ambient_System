# Ambient_System
Dans le package ambient_système, il existe 3 packages: 
agx_sdk, qui est le SDK du AgileX.
ROS, le dossier qu'on lance des noeuds
ROSMobile, le dossier pour l'app du ROS.

Pour lancer le programme:

1°)Brancher le CAN bus sur l'ordinateur
dans le terminal installer outil du CAN:
$sudo apt install can-utils

2°) configurer CAN
$ sudo ip link set can0 up type can bitrate 500000

3°) cd dans ROS/catkin_ws

4°)sourcer le programme
$source devel/setup.bash

5°)lancer la connexion du CAN
$ roslaunch scout_bringup scout_robot_base.launch

6°)pour lancer le noeud du GPS:
$ roslaunch getgps getgps.launch

Pour jouer avec téléphone, il faut installer ROSMobile, les codes sont dans ROSMobile/ROS-Mobile-Android/app