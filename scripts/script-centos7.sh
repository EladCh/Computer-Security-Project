#basic dependencies
sudo yum update
sudo yum install -y python36-setuptools
sudo easy_install-3.6 pip

#extra dependencies
sudo pip3 install mmh3
sudo pip3 install bitarray

#pysimplegui
sudo pip3 install PySimpleGUI

#running the program
sudo python3 -m gui
