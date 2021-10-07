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

# Windows install process.
* Turn off all the shit in the install process
* After first launch wait for all the drivers to be installed and then reboot
* Update system
* Set TEMP path variable to C:\TEMP
* Disable File indexing(close all the programs before that)
* Install browser
* Install [Win-rar](https://www.rarlab.com/)
* Turn off defender in settings
* [Activate system](https://github.com/massgravel/Microsoft-Activation-Scripts)
* Install MS c++ distributives
* Do not forget these Settings:
  * temp
  * dffgd
  * Ctrl-Shift change lang
  * Swap file
  * Disable System protection
  * Disable restore points
  * Disable remote access
  * Ultimate powerplan
  * Turn off fast startup
  * Cursors
  * Set up task bar
  * Turn off Firewall and set up Defender
  * Enable hidden files and extensions
  * Sound and mircophone settings
  * Disable User account control
* Setup Nvidia driver and configure it
* Add Hw monitor in autostart
* Install software
  * Add tablet driver to Defender exceptions

Result
![VTzPaHfbVtI](https://user-images.githubusercontent.com/57370975/135751155-bf95e04f-637d-40fe-a248-79d489cdbfc6.jpg)
![image](https://user-images.githubusercontent.com/57370975/136049861-8ec30fbd-45f6-4462-bea4-f5c4905ad079.png)
