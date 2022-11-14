# hddclick

HDDClick runs on a Pico and makes sounds with hard drive activity.
Copy .py-file as main.py to the Rpi Pico and connect some sort of speaker.

```
WARNING: Motherboard HD-activity indicator uses 5V,
         so a voltage divider MUST be used, or your
         3.3V Rpi Pico will be destroyed!

5V >---|4k7R|----+---------2.5V--> Pin IN (3.3V Max)
                 |
                | | 4k7R
                 |
GR  -------------+  GROUND

(if using USB-power from the same machine, no ground connection is required)
Will autosense a Dell-type connection (+-5V). Only connect +5V!
```
