#!/bin/bash
user=$1
if [ ! -d /FileManager/ ];then
  sudo  cp FileManager /FileManager -R
fi
if [ ! -d /fileshared/ ];then
  mkdir "/fileshared/"
  chmod 777 /fileshared/ -R
  fi
if [ ! -d /home/$user/messages ];then
  mkdir /home/$user/messages
  chown $user:$user /home/$user/messages
  chmod 770 /home/$user/messages
  pip install pyqt5
fi
if [ ! -f /bin/filemanager ];then
cp /FileManager/filemanager.py /bin/filemanager
chmod +x /bin/filemanager
fi