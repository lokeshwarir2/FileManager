#!/bin/bash
if [ ! -d /FileManager/ ];then
  cp FileManager /FileManager -R
  chmod 777 /FileManager/
fi

if [ ! -d /fileshared/ ];then
  mkdir "/fileshared/"
  chmod 777 /fileshared/
  fi
user=$(whoami)
if [ ! -d /home/$user/messages ];then
  mkdir /home/$user/messages
  chown $user:$user /home/$user/messages -R
  chmod 770 /home/$user/messages
fi
if [ ! -f /bin/filemanager ];then
cp /FileManager/filemanager.py /bin/filemanager
chmod +x /bin/filemanager
fi