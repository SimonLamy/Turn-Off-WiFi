# Turn-Off-WiFi
Script that I use to turn off WiFi on my Pi after a certain amount of time with crontab. A window is displayed with a 10 seconds countdown and 2 button : one to cancel and an other one to instantly turn off WiFi.

In crontab, I use the following line to ask me if I want to turn WiFi off after 1 hour : 
```
@reboot sleep 36000 XAUTHORITY=/home/pi/.Xauthority DISPLAY=:0 python3 path/to/WiFiTurnOff.py
