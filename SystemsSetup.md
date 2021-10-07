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
* Enable names and extensions in Explorer
* Delete not used temp folders' contents
* Install browser
* Install [Win-rar](https://www.rarlab.com/)
* Turn off defender in settings
* [Activate system](https://github.com/massgravel/Microsoft-Activation-Scripts)
* Install [MS C++ distributives](https://www.techpowerup.com/download/visual-c-redistributable-runtime-package-all-in-one/)
* Do not forget these Settings:
  * Sound settings
  * Turn off notifications
  * Turn off focus assist for all apps and times
  * Ultimate powerplan
    ```bash
    powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61 
    ```
  * Turn off fast startup
  * Don't enable storage sense(it's better to manually enable it once a month)
  * Turn off tablet mode
  * Turn off share across devices
  * Turn off Bluetooth and its notifications
  * Don't let Windows manage my printer
  * Mouse set up [cursor](//TO-DO) and speed
  * Turn off touchpad when mouse is connected
  * Turn off all typechecking stuff and enable Ctrl-Shift lang change
  * Turn off autoplay(take no action)
  * Turn off all USB notifications
  * Turn off Wifi and Hotstop 2.0
  * Turn off all VPN shit
  * Turn on Airplane mode
  * Turn off remote turning on mobile hotspot
  * Proxy disable automatic setting detection
  * Peresonalization solid black color background
  * Turn off transparency
  * Enable Dark theme
  * In themes set up desktop icons
  * Delete start panel stuff
  * Disable people and set up icons on task bar
  * Turn off map updates
  * Turn off windows security icon on startup
  * In sign-in disable automatic session restore
  * Set up time and time zone
  * Turn off gamebar in gaming
  * Turn off broadcasting and captures as much as possible
  * In display turn off windows animations and turn desktop background image
  * Turn off type feedback
  * Don't allow narrator to start by keybind
  * Turn off sticky keys on keyboard
  * Turn off everything in privacy
  * Feedback frequency - never
  * Turn off delivary optimization
  * Turn of defender notifications
  * Turn off safe search
  * Set up task bar
  * Adjust system for best performance except smooth edges of screen fonts
  * Set up swapfile
  * Disable system protection and restore points
  * Turn off remote assistance connections
  * Turn off firewall
  * Change user account control settings
* Setup [Nvidia driver](https://www.nvidia.com/Download/index.aspx) and configure it
* Add [Hw monitor](https://www.cpuid.com/softwares/hwmonitor.html) in autostart
  ```bash
  C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp
  ```
* Set up Firefox
* Add music to music folder
* Install [tablet driver](https://github.com/hawku/TabletDriver)(dont'forget to turn off defender and add driver to exceptions)
  ```bash
  Window size 1400x1050
  Offset 260,15
  Size 50x37.5
  Filters off
  ```

Result
![VTzPaHfbVtI](https://user-images.githubusercontent.com/57370975/135751155-bf95e04f-637d-40fe-a248-79d489cdbfc6.jpg)
![image](https://user-images.githubusercontent.com/57370975/136390358-1e36eba0-f5f3-44ff-a7db-051db97f4585.png)

