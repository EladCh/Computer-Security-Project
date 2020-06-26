#basic dependencies
sudo apt-get update
sudo apt-get install -y python3.6
sudo apt-get install -y python3-pip

#extra dependencies
sudo -H pip3 install pysimplegui
sudo -H pip3 install mmh3
sudo -H pip3 install bitarray

#running the code
sudo python3 -m gui

