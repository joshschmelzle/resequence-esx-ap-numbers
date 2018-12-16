# resequence_esx_ap_numbers

Rename and resequence Ekahau Site Survey's Access Point (AP) names using Python.

An Ekahau Site Survey project is stored as a compressed file with an extension `.esx`. Inside, it contains several JavaScript Object Notation (JSON) files that help organize project data. In particular, `accessPoints.json` contains information for the project's Access Points which will be what this script modifies. All AP names are changed, and the number included in the name is resequenced in a seemingly random order.

> **WARNING: the number from the original AP name will, in no particular order, be changed. don't use this script if you care about that.**

# todo

- [ ] eliminate manual steps; retrieve accessPoints.json directly from .ESX file using zipfile 
- [ ] programmatically replace existing accessPoints.json in .ESX file the modifeid one. 
- [ ] backups! automatically copy and backup .ESX to a new file stamped with an ISO 8601 format.
  - [ ] check both files to ensure they are the same, if not, don't allow the script to proceed.
- [ ] add logging

# requirements

Python 3.5 or greater installed

Tested with Python 3.6.4, Windows 10 Enterprise (10.0.16299 N/A Build 16299), Ekahau ESS Pro 9.2.5.260. 

# usage

- step 1. make a backup of your .ESX file to ensure you have a safe backup
  - this is important.
- step 2. open the .ESX (zip archive) with something like 7-Zip (no need to extract the entire contents we're only after accessPoints.json)
- step 3. pull out the `accessPoints.json` file and put it in the same directory as the script
- step 4. run the script. 
  - you will see old and new AP names printed to the screen. and finally you will see a new JSON file called `accessPoints-resequenced.json`. i advise keeping a copy of both for backup/correlation.
- step 5. open the .ESX and replace the accessPoints.json with the new one. 
  - the new one must be named `accessPoints.json`.
- step 6. open the project in ESS (if you already have it open go to `File > Open` or `CTRL + O` on Windows).

# example

## script

![](https://github.com/joshschmelzle/resequence_esx_ap_numbers/blob/master/resequenceAPs.png)

## before

![](https://github.com/joshschmelzle/resequence_esx_ap_numbers/blob/master/aruba325before.PNG)

## aftertJSON

![](https://github.com/joshschmelzle/resequence_esx_ap_numbers/blob/master/aruba325after.PNG)

# warning

This script will change the name of your Access Points. The AP number in the original name will not match the new name. If this isn't desirable, do not use this script.

# license

project license can be found [here](https://github.com/joshschmelzle/resequence_esx_ap_numbers/blob/master/LICENSE)
