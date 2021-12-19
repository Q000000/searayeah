# Windows install process.
* Turn off all the shit in the install process
* After first launch wait for all the drivers to be installed and then reboot
* Update system
* Set TEMP path variable to C:\TEMP
* Disable File indexing(close all the programs before that)
* Enable names and extensions in Explorer
* Delete not used temp folders' contents
* Turn off defender in settings
* Install browser
* Install [Win-rar](https://www.rarlab.com/)
* [Activate system](https://github.com/massgravel/Microsoft-Activation-Scripts)
* Install [MS C++ distributives](https://www.techpowerup.com/download/visual-c-redistributable-runtime-package-all-in-one/)
* Settings:
  * System
    * Sound settings(do nothing on call)
    * Turn off notifications
    * Turn off focus assist for all apps and times
    * Ultimate powerplan
      ```bash
      powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61
      ```
    * Turn off fast startup
    * Don't enable storage sense(it's better to manually enable it once a month)
    * Turn off tablet mode
    * Pressing Alt-Tab shows open windows only
    * Virtual desktop - all desktops
    * Turn off share across devices
    * Related settings
    * Adjust system for best performance except smooth edges of screen fonts
    * Set up swapfile
    * Disable system protection and restore points
    * Turn off remote assistance connections
  * Devices
    * Turn off Bluetooth and its notifications(in related settings)
    * Don't let Windows manage my printer
    * Mouse set up [cursor](https://github.com/searayeah/searayeah/tree/main/SystemsSetup/EverSummerCursors) and speed
    * Turn off touchpad when mouse is connected
    * Turn off all typechecking stuff and enable Ctrl-Shift lang change
    * Turn off autoplay(take no action)
    * Turn off all USB notifications
  * Network & Internet
    * Turn off Wifi and Hotspot 2.0
    * Turn off all VPN shit
    * Turn on Airplane mode
    * Proxy disable automatic setting detection
  * Personalization
    * Solid black color background
    * Enable Dark theme
    * Turn off transparency
    * In themes set up desktop icons
    * Delete start panel folders
    * Set up icons on task bar
    * Set up task bar
  * Apps
    * Delete dolby atmos
    * Turn off map updates
    * Turn off windows security icon on startup
    * Turn off Realtek on startup
  * Accounts
    * In sign-in disable automatic session restore
  * Time & Language
    * Set up time and time zone
  * Gaming
    * Turn off gamebar
    * Turn off broadcasting and captures as much as possible
  * Ease of access
    * In display turn off windows animations and turn desktop background image
    * Turn off touch feedback in mouse pointer
    * Don't allow narrator to start by keybind
    * Turn off sticky keys on keyboard
  * Search
    * Turn off safe search
    * Disable cloud content search
    * Disable history
  * Privacy
    * Turn off everything in privacy
    * Feedback frequency - never
  * Update & Security
    * Turn off delivery optimization
    * Turn off domain, private, public firewall
    * Turn off defender notifications
* Control panel
  * Change user account control settings
  * Disable maintenance messages
  * Turn of shit notifications
    ```bash
    Group Policy -> Computer Configuration -> Administrative Templates -> Windows Components -> Windows Security -> Notifications -> Hide all notifications
    ```
* Setup [Nvidia driver](https://www.nvidia.com/Download/index.aspx) and configure it
* Add [Hw-monitor](https://www.cpuid.com/softwares/hwmonitor.html) in autostart
  ```bash
  C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp
  ```
* Set up Firefox
* Add music to music folder
* Install [tablet driver](https://github.com/OpenTabletDriver/OpenTabletDriver)
  ```bash
  Display 1400x1050
  X, Y 960, 540
  Width, Height 50, 37.5
  Filters off
  ```

Result
![VTzPaHfbVtI](https://user-images.githubusercontent.com/57370975/135751155-bf95e04f-637d-40fe-a248-79d489cdbfc6.jpg)
![image](https://user-images.githubusercontent.com/57370975/136390358-1e36eba0-f5f3-44ff-a7db-051db97f4585.png)
