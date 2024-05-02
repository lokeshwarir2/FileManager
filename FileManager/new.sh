#!/bin/bash
user1=$1
file1=$2
f=$(echo ${file1##*/})
time1=$(date | cut -d" " -f 4)
date1=$(date +%F)
filename="("$date1"-"$time1")"$f
user=$(whoami)
group1=($user$user1)
egrep -i "^$group1" /etc/group
if [ $? -ne 0 ]; then
sudo groupadd $group1
fi
sudo usermod -G $group1 $user
sudo usermod -G $group1 $user1
path=/fileshared/$filename
cp $file1 $path
sudo chown $user:$group1 $path -R
sudo chmod 2771 $path -R
