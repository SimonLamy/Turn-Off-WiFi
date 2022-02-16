# Turn-Off-WiFi
Script that I use to turn off WiFi on my Pi after a certain amount of time with crontab.

In crontab, I use the following line to ask me if I want to turn WiFi off after 1 hour : 
```
@reboot sleep 36000 XAUTHORITY=/home/pi/.Xauthority DISPLAY=:0 python3 path/to/WiFiTurnOff.py
