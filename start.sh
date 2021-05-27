#!/bin/bash
mkdir ~/.lybing/
cp lybing.py ~/.lybing/
cp lybing.sh ~/.lybing/

sudo pip install requests
sudo pip install beautifulsoup4

chmod a+x ~/.lybing/lybing.sh
