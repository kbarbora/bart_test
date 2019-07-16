#!/bin/bash
    
# ----------------Bart test dependencies------------
# The following dependencies are needed
# in order to be able to run the Bart test
# please install them running the following command:
#       pip-sync
#                                author: Kevin Barba
# --------------------------------------------------       
echo "Need sudo privileges to install dependencies"
sudo pip install future
sudo pip install numpy
sudo pip install psychopy
sudo pip install openpyxl
sudo pip install xlrd
sudo pip install xlwt
sudo pip install xlsxwriter
sudo pip install pandas

if [[ "$OSTYPE" == "darwin"* ]]; then
    sudo python -m pip install -U pyo
elif [[ "$OSTYPE" == "linux-gnu" ]]; then
    sudo apt-get install python-pyo
else
    echo "[Error] OS not detected. Exiting"
    echo
    exit
fi
