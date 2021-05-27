#!/bin/bash
cd ~/.lybing/
find ~/.lybing/ -type f \( -name 'wallpaper.jpg' \) -print0 | shuf -n1 -z | xargs -0 feh --bg-scale
python lybing.py
sleep 10s
find ~/.lybing/ -type f \( -name 'wallpaper.jpg' \) -print0 | shuf -n1 -z | xargs -0 feh --bg-scale
