# SkyEvent
![sky](https://user-images.githubusercontent.com/29212540/54962596-d6fbc600-4f3b-11e9-9529-b099dd646df9.jpg)

Application that displays an image of the night sky based on longitude, latitude, and time.
Currently runs exclusively from command line. 

Utilizes this api by John Walker for getting images. Please check it out!
(https://www.fourmilab.ch/yoursky/)

## Dependencies
Uses Images, requests, and mechanize.

## Usage
python3 yourskymech.py [ARGS]

Arguments: 
- -u Used before specifying date in year/month/day hour:minute:second format
- -la Specify latitude
- -lo Specify longitude
- -n Direction of lat (N/S)
- -e Direction of lon (E/W)
- -co Toggle equator
- -m Toggle moon and planets
- -o Toggle constelation outlines
- -cn Toggle constellation names
- -is Set image size (in px)
- -sc Change image theme (1,2,3)
Support for time coming in next commit.
