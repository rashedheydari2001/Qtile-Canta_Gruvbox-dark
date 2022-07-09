#!/bin/env bash
setxkbmap -model pc105 -layout us,ir -option grp:alt_shift_toggle -option numpad:microsoft
feh --bg-scale "/home/rashed/Pictures/wallpaper/2.jpg"
picom --experimental-backend --config .config/picom/picom.conf &
