# VirtualBox REST API

This repo is a REST API for vbox. It also has a handy vbox script to allow a user to do some basic virtualbox commands from the command-line. 

Currently only works on Linux. Assumes VBoxManage.

## Examples

```
from vbox import *

v = VirtualBox("ubuntu18-01")
v.create()
v.set_cpus(8)
v.set_memory("8192")
v.set_ostype("Ubuntu_64")
v.create_sata_controller()
v.set_nic()
v.set_bridge_adapter(adapter="enp0s25")
v.set_mac_address()
v.create_hd("/home/logan/VBoxStack/ubuntu18-01", "40000")
v.attach_storage("SATA Controller", 0, "hdd", "/home/logan/VBoxStack/ubuntu18-01.vdi")
v.attach_storage("SATA Controller", 1, "dvddrive", "/home/logan/VBoxStack/ubuntu-18.04.5-live-server-amd64.iso")
v.set_boot()
v.set_vrde(True, 7000)
v.start_headless()
```

## Python

If you are only wanting to use vbox.py, you don't need to install anything.

If you are wanting to use the REST API:

```
pip install fastapi
pip install uvicorn

uvicorn api:app --host 0.0.0.0
```

## VBox

5.2.4 has a bug on my system where VMs don't shut down.

VBox 6.1 and 6.0 vrde didn't work when I installed it using dpkg.

If I install just 5.2.44 from vbox vrde works but there's no graphics to stream. 


```
wget -q https://www.virtualbox.org/download/oracle_vbox_2016.asc -O- | sudo apt-key add -
wget -q https://www.virtualbox.org/download/oracle_vbox.asc -O- | sudo apt-key add -
sudo add-apt-repository "deb http://download.virtualbox.org/virtualbox/debian bionic contrib"
sudo apt update
sudo apt install virtualbox-6.1 dkms -y

cd /tmp
wget https://download.virtualbox.org/virtualbox/6.1.12/Oracle_VM_VirtualBox_Extension_Pack-6.1.12.vbox-extpack
sudo VBoxManage extpack install Oracle_VM_VirtualBox_Extension_Pack-6.1.12.vbox-extpack
```

Ignore this, or don't I'm a readme not a cop.

```
sudo apt-get install virtualbox-dkms -y
sudo dpkg --purge virtualbox-qt
sudo dpkg --purge virtualbox-5.2
sudo dpkg --purge virtualbox
wget https://download.virtualbox.org/virtualbox/5.2.44/virtualbox-5.2_5.2.44-139111~Ubuntu~bionic_amd64.deb
sudo dpkg -i virtualbox-5.2_5.2.44-139111~Ubuntu~bionic_amd64.deb
sudo apt-get install virtualbox-qt -y
sudo apt --fix-broken install
sudo apt-get install virtualbox-qt -y
```
