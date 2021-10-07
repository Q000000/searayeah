# Linux install process.
* Change store region mirrors to Russia.
* Update Kernel
* Update Nvidia drivers
* Enable Trim
  ```bash
  sudo systemctl enable fstrim.timer
  sudo systemctl start fstrim.timer
  sudo systemctl status fstrim.timer
  ```
* Enable [Swapfile](https://wiki.manjaro.org/index.php?title=Swap)
* Do not forget these Settings:
  * Time
  * Screen edges
  * Startup and shutdown
  * Input devices
  * Display and monitor
  * Notifications 3 sec
  * Inteface scale 125%
  * Auto mount all the drives
  * Left Ctrl-Left shift lang change
  * Set OpenGl 3.1
  * Add 'keep above others' to windows
* Confiture task bar
* Configure [Git](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
* Configure Dolphin
* Configure Konsole
* Configure Spectacle
* Set up programs and configure them
  * onlyoffice
  * [arc-kde](https://github.com/PapirusDevelopmentTeam/arc-kde)
  * [papirus-icon-theme](https://github.com/PapirusDevelopmentTeam/papirus-icon-theme)
  * Inkscape
  * Discord
  * Jetbrains Toolbox
  * Kolorpaint
  * Teamviewer
  * Zoom
  * [Sublime Text](https://github.com/searayeah/searayeah/tree/main/SublimeSetup)
  * Firefox
  * Chrome
  * Spotify
  * ttf-ms-fonts
  * Thunderbird
  * Gnome boxes
  * Telegram
  * Vk messsenger
  * OBS
  * kio-gdrive
* Configure autostart
![image](https://user-images.githubusercontent.com/57370975/135800713-0e81e4ec-d422-4f4f-83ef-895567dc62a6.png)

Result
![Screenshot_20211004_085237](https://user-images.githubusercontent.com/57370975/135800670-35721881-094f-42e0-9e59-e4001f336ea1.png)