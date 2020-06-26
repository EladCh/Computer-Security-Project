# Computer-Security-Project
Implementation of double bloom filter &amp; password strength

## Dependencies for ubuntu18.04:
python version 3.6 (or newer)
```
$ sudo apt-get update
$ sudo apt-get install -y python3.6
$ sudo apt-get install -y python3-pip
```
## Dependencies for centos7:
```
$ sudo yum update
$ sudo yum install -y python36-setuptools
$ sudo yum install -y python3-devel
$ sudo easy_install-3.6 pip

```
extra dependencies
```
$ sudo pip3 install mmh3
$ sudo pip3 install bitarray
```
PySimpleGUI
```
pip3 install pysimplegui
```
## Visualization
In wsl applications X server is required to run on the windows machine.
Download can be found here: https://sourceforge.net/projects/xming/
In order to set the display to the right output use the following in the CMD:
```
export DISPLAY=:0
```

