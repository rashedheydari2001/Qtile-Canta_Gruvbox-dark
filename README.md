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
sudo pacman -S kvantum qt5ct 
```
gtk theme from aur:
```
yay -S canta-gtk-theme 
```
icon theme from arch repo:
```
sudo pacman -S papirus-icon-theme
```
download canta kvantum theme from this link: https://store.kde.org/p/1306414
