# Qtile-Canta_Gruvbox-dark
config file for qtile window manager
![Screenshot from 2022-07-09 14-20-12](https://user-images.githubusercontent.com/81459372/178104057-2deaae08-c889-445a-aaeb-ee9e2d0be63f.png)


1 : first of all install base dependency
```
sudo pacman -S qtile picom dmenu
```
from chaotic aur: for adding chaotic aur repo go to this website https://aur.chaotic.cx/
```
sudo pacman -S networkmanager-dmenu-git
```
2 : install font dependency
from arch repo:
```
sudo pacman -S noto-fonts noto-fonts-cjk noto-fonts-emoji noto-fonts-extra ttf-fira-code
```
from chatic aur: 
```
sudo pacman -S nerd-fonts-fantasque-sans-mono ttf-malayalam-font-chilanka nerd-fonts-fira-code
```
from aur:
```
yay -S vazir-code-fonts vazirmatn-fonts
```
3 : install config file
```
git clone https://github.com/rashedheydari2001/Qtile-Canta_Gruvbox-dark.git && cd Qtile-Canta_Gruvbox-dark/.config && mv fontconfig alacritty picom qtile ~/.config && chmod +x ~/.config/qtile/autostart.sh && cd .. && cd etc && sudo mv -f environment /etc && sudo fc-cache -rsv && fc-cache -vf && sudo fc-cache -vf
```
4 : install theme dependency and theme and icon theme
theme dependency from arch repo:
```
sudo pacman -S kvantum qt5ct lxappearance
```
gtk theme from aur:
```
yay -S canta-gtk-theme 
```
icon theme from arch repo:
```
sudo pacman -S papirus-icon-theme xcursor-vanilla-dmz
```
download canta kvantum theme from this link: https://store.kde.org/p/1306414
<br>
extract archive file and open up kvantum click on install and select your folder inside the folder you extract it and select canta dark and click on use this theme 
<br>
5 : set up theme and font
<br>
open up lxappearance and select canta dark for theme and dmz light for cursor theme and select papirus dark for icon theme and click on apply 
<br>
open your qt5ct for theme in main page select kvantum dark for qt app font select this value:
![Screenshot from 2022-07-09 19-42-19](https://user-images.githubusercontent.com/81459372/178111662-39491635-a73b-4e7c-b426-5d17bdc2604a.png)
and for icon theme select papirus-dark
<br>
6 : Keyboard layout 
go to  this config file 
```
nano .config/qtile/autostart.sh
```
if you don't need layout remove line number one
<br>
if you need a layout set up your layout like this us,uk
<br>
7 : if you have a pc and you don't have a battery disable the battery widget from this config file
```
nano .config/qtile/config.py
```
go to line number 174 and remove the battery widget
<br>
8 : shortcut 
if you don't like my shortcut so change it open up this config file:
```
nano .config/qtile/config.py
```
go to line number 13 you can see custom shortcuts
mod4 or mod = superkey or windows key, mod1 = alt, shift = shift
<br>
example shortcut 
<br>
Key[mod, othermod if you need it like shift], 'keyboard char', lazy.spawn('Command'), desc="comment"),
<br>
congratulations now you have completely done
