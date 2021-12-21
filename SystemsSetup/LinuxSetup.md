# Linux install process.
* Download Manjaro LTS w/o pre-installed software
* Set English language and locale
* Enable AUR and its updates
* Install alongside
* Change store region mirrors to Russia
* Update Kernel(5.14)
* Install Nvidia drivers(Auto-install proprietary)
* Set up Firefox
* Set up Konsole
* Enable Trim
  ```bash
  sudo systemctl enable fstrim.timer
  sudo systemctl start fstrim.timer
  sudo systemctl status fstrim.timer
  ```
* Enable [Swapfile](https://wiki.manjaro.org/index.php?title=Swap#Using_a_Swapfile)
* Settings
  * Quick Settings
    * Dark theme
  * Appearance
    * Window Decorations -> Titlebar options
  * Workspace Behavior
    * Screen adges
    * Virtual desktops
  * Startup and Shutdown
    * Login screen
    * Desktop session
  * Notifications
  * Regional Settings
    * Date & Time
  * KDE Wallet -> Disable
  * Input Devices
    * Keyboard -> Layouts -> Switching bind
    * Mouse
    * Touchpad
  * Display and Monitor
    * Scale 125%
    * Compositor
    * Night color
  * Bluetooth -> Disable
  * Removable storage -> Auto-mounting
* Confiture task bar
* Configure [Git](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
* Configure Dolphin
* Configure Spectacle
* Configure Desktop
* Software list
  * Onlyoffice
  * VLC
  * CMake
  * [arc-kde-git](https://github.com/PapirusDevelopmentTeam/arc-kde)
  * [papirus-icon-theme-git](https://github.com/PapirusDevelopmentTeam/papirus-icon-theme)
  * Inkscape
  * Discord
  * Kolourpaint
  * Teamviewer
  * Zoom
  * [Sublime Text](https://github.com/searayeah/searayeah/tree/main/SystemsSetup/SublimeSetup)
  * Firefox
  * [Spotify](https://wiki.manjaro.org/index.php/Spotify#PGP_signatures_could_not_be_verified)
  * ttf-ms-fonts
  * Thunderbird
  * Gnome boxes
  * Telegram Desktop
  * Vk messsenger
  * OBS
  * qBittorrent
* Configure autostart
![image](https://user-images.githubusercontent.com/57370975/135800713-0e81e4ec-d422-4f4f-83ef-895567dc62a6.png)

Result
![Screenshot_20211004_085237](https://user-images.githubusercontent.com/57370975/135800670-35721881-094f-42e0-9e59-e4001f336ea1.png)
