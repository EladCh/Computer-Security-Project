#basic dependencies
sudo yum update
sudo yum install -y python36-setuptools
sudo yum install -y python3-devel
sudo easy_install-3.6 pip

#extra dependencies
sudo -H pip3 install mmh3
sudo -H pip3 install bitarray

#pysimplegui
sudo -H pip3 install pysimplegui

#running the program
sudo python3 -m gui

