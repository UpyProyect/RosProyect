# ROS_MASTER and ROS_SLAVE

Where you see "<<        >>" just replace without the signs.

Step 1: Setup sever newtwork 
PC1 = # server
  ```
  $ ifconfig -----------------------------------> To get the "PC1"
  $ sudo atom etc/hosts -----------------------------------> Add in the end  "PC2_IP"
  $ roscore -----------------------------------> Run it
  $ echo %ROS_MASTER_URI -----------------------------------> To get the "PORT"
  $ export ROS_IP=<PC1_IP> -----------------------------------> Run it

  ```
  Step 2: Setup slave newtwork
  PC2 = # Slave
  ```
  $ ifconfig -----------------------------------> To get the "PC2"
  $ sudo atom etc/hosts -----------------------------------> Add in the end  "PC1_IP"
  $ export ROS_MASTER_URI=http://<<PC1_IP>>:<<port>> -----------------------------------> Run it
  $ export ROS_IP=<<PC2_IP>> -----------------------------------> Run it
  
  ```
  Step 3: Check if everything is OK
  
  ```
  $ rostopic pub /test std_msgs/String hello
  $ rostopic echo /test  -----------------------------------> Have to receive msg "hello"
  
  
  
  $ rostopic echo /test  -----------------------------------> Have to receive msg "hello"
  $ rostopic pub/ test std_msgs/String hello
  ```
  #NOTE: YOU HAVE TO EXPORT THE IP IN EACH TERMINAL
  
