import os
import subprocess

print("""
         υ´• ﻌ •`υ
Welcome to my linux script
What do you want to do?
(1) Installation before chroot
(2) Post Installation after chroot
(3) Install AUR helper [yay]
(4) Install packages
(5) Install applications
(6) Install desktop environment
""")
pick = input("Pick from 1 to 7: ")

if pick == "1":
    os.system("reflector --country Australia --age 6 --protocol https --sort rate --save /etc/pacman.d/mirrorlist")
    os.system("pacstrap -K /mnt base linux linux-firmware grub efibootmgr os-prober neovim sudo networkmanager python3")
    os.system("genfstab -U /mnt >> /mnt/etc/fstab") 

if pick == "2":
    os.system("sed -i '171s/^#//' /etc/locale.gen")
    os.system("locale-gen")
    os.system("echo LANG=en_US.UTF-8 > /etc/locale.conf")
    os.system("echo localhost > /etc/hostname")
## MAC address randomization
    os.system("echo [device-mac-randomization] >> /etc/NetworkManager/conf.d/wifi_rand_mac.conf && echo wifi.scan-rand-mac-address=yes >> /etc/NetworkManager/conf.d/wifi_rand_mac.conf && echo [connection-mac-randomization] >> /etc/NetworkManager/conf.d/wifi_rand_mac.conf && echo ethernet.cloned-mac-address=random >> /etc/NetworkManager/conf.d/wifi_rand_mac.conf && echo wifi.cloned-mac-address=random >> /etc/NetworkManager/conf.d/wifi_rand_mac.conf")
## unique DUID per connection
    os.system("echo [connection] >> /etc/NetworkManager/conf.d/duid.conf && echo ipv6.dhcp-duid=stable-uuid >> /etc/NetworkManager/conf.d/duid.conf")
## Enable IPv6 privacy
    os.system("echo [connection] >> /etc/NetworkManager/conf.d/ip6-privacy.conf && echo ipv6.ip6-privacy=2 >> /etc/NetworkManager/conf.d/ip6-privacy.conf")
    os.system("sudo systemctl enable NetworkManager")
    os.system("mkinitcpio -P")
    os.system("passwd")
    os.system("grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=GRUB")
# Detecting other operating systems
    os.system("sed -i '63s/^#//' /etc/default/grub")
    os.system("grub-mkconfig -o /boot/grub/grub.cfg")
## Setting unique machine ID to a generic ID (Whonix ID)
    os.system("echo b08dfa6083e7567a1921a715000001fb > /var/lib/dbus/machine-id")
## Adding a user
    os.system("useradd -m -G wheel,audio,video,storage,kvm,scanner,optical,input,floppy,disk user")
    os.system("passwd user")
## allowing members of group wheel sudo access in the sudoers file
    os.system("sed -i '85s/^#//' /etc/sudoers")
## Enabling multilib repo
    os.system("echo [multilib] >> /etc/pacman.conf && echo Include = /etc/pacman.d/mirrorlist >> /etc/pacman.conf")
## Time sync
    os.system("timedatectl set-ntp true")
## Set Time Zone
    os.system("timedatectl set-timezone Zone/SubZone")

if pick == "3":
    os.system("sudo pacman -S --needed git base-devel && cd /opt && sudo git clone https://aur.archlinux.org/yay.git && sudo chown -R $USER:users ./yay && cd yay && makepkg -si")

if pick == "4":
    os.system("sudo pacman -S mesa lib32-mesa xf86-video-amdgpu amdvlk lib32-amdvlk libva-mesa-driver lib32-libva-mesa-driver mesa-vdpau lib32-mesa-vdpau amd-ucode nvtop xorg-xwayland ttf-font-awesome ttf-dejavu ttf-bitstream-vera lib32-fontconfig ttf-liberation wqy-zenhei pipewire pipewire-alsa pipewire-pulse pipewire-jack bluez bluez-utils blueman ntfs-3g wget cups cups-pdf htop cmus neofetch ncdu ranger yt-dlp ffmpeg gnupg exfat-utils intel-ucode android-tools man ufw iptables sane sane-airscan ipp-usb testdisk neovim nerd-fonts gpa linux-headers")
    os.system("yay -S ani-cli memtest86-efi ix python-spotdl")
    os.system("sudo pacman -S xdg-user-dirs && xdg-user-dirs-update")
    os.system('echo "-o ~/Downloads/%(title)s.%(ext)s" > ~/yt-dlp.conf')
    os.system("cp config/.alacritty.yml ~/.alacritty.yml")
    os.system("sudo systemctl enable cups && sudo systemctl start cups")
    os.system("sudo systemctl enable bluetooth && sudo systemctl start bluetooth")
    os.system("sudo systemctl enable ufw && sudo systemctl start ufw && sudo systemctl enable iptables && sudo systemctl start iptables && sudo ufw enable && sudo systemctl enable ipp-usb && sudo systemctl start ipp-usb")
    os.system("cp config/.bashrc ~/.bashrc")
    os.system("git clone https://github.com/LazyVim/starter ~/.config/nvim")
    os.system("rm -rf ~/.config/nvim/.git")
    os.system("sudo echo Colour >> /etc/pacman.conf")
    os.system("chsh -s /bin/bash")
    os.system("chsh -s /bin/bash user")

if pick == "5":
    os.system("sudo pacman -S alacritty firefox krusader kompare unace krename lhasa unarj unrar unzip xz zip arj p7zip kde-cli-tools nemo docker libreoffice audacity handbrake blender gimp mpv obs-studio krita gwenview torbrowser-launcher transmission-gtk keepassxc ark inkscape okular kdenlive darktable kdiskmark pavucontrol veracrypt system-config-printer net-tools wine perl-image-exiftool vlc nmap whois thunderbird ghex tor proxychains metadata-cleaner bleachbit gnome-disk-utility")
# arduino lmms peazip/p7zip-gui steam lutris gamemode lib32-gamemode onionshare ventoy-bin rpi-imager universal-android-debloater linux-wifi-hotspot kdeconnect mpv-webm ardour lmms trimage simple-scan skanlite spectacle gnome-maps
    os.system("sudo pacman -S flatpak && flatpak install com.discordapp.Discord && yay -S flatseal")
    os.system("yay -S rar blobsaver librewolf-bin freetube-git")
# minecraft-launcher lunar-client unityhub
    os.system("xdg-settings set default-web-browser librewolf.desktop")
    os.system("sudo systemctl enable tor && sudo systemctl start tor")
    os.system("sudo usermod -aG docker $USER && sudo systemctl enable docker && sudo systemctl start docker")
    os.system("sudo pacman -S virt-manager qemu libvirt ovmf dnsmasq swtpm && sudo systemctl start libvirtd && sudo systemctl enable libvirtd && sudo usermod -aG libvirt $USER")

if pick == "6":
    os.system("sudo pacman -S hyprland seatd waybar rofi-emoji hyprland cliphist otf-font-awesome polkit-kde-agent dunst swaybg xdg-desktop-portal-hyprland udiskie noto-fonts-cjk noto-fonts-emoji swayidle pavucontrol")
    os.system("yay -S rofi-power-menu ttf-symbola rofi-bluetooth-git rofi-lbonn-wayland-git swaylock-effects")
    os.system("sudo systemctl enable seatd && sudo systemctl start seatd && sudo usermod -aG seat $USER")
    os.system("wget -P ~/Documents/Backgrounds https://w.wallhaven.cc/full/3l/wallhaven-3lz78d.jpg")
    os.system("cp -r config/hypr/ ~/.config/ && cp -r config/waybar/ ~/.config/")

## post installation
# download tor browser
# configure librewolf
# config krusader
# login to discord
# import xml blobsaver
# import keepassxc database
# virt-manager set Graphical console scaling to Always
# add screenshot shortcut obs-studio
# add printer
# config proxychains
