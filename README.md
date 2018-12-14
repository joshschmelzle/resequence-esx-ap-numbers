# resequence_esx_ap_numbers

Resequence Ekahau's Site Survey (.esx accessPoints.json) Access Point (AP) names using Python.

In no particular order, the new AP #'s will never be higher than the total number of APs.

# requirements

Python 3.5 or greater installed

Tested with Python 3.6.4, Windows 10 Enterprise (10.0.16299 N/A Build 16299), Ekahau ESS Pro 9.2.5.260. 

# sample output

- step 1. make a backup of your .ESX file to ensure you have a safe backup
  - this is important.
- step 2. open the .ESX (zip archive) with something like 7-Zip (no need to extract the entire contents we're only after accessPoints.json)
- step 3. pull out the `accessPoints.json` file and put it in the same directory as the script
- step 4. run the script. 
  - you will see old and new AP names printed to the screen. and finally you will see a new JSON file called `accessPoints-resequenced.json`. i advise keeping a copy of both for backup/correlation.
- step 5. open the .ESX and replace the accessPoints.json with the new one. 
  - the new one must be named `accessPoints.json`.
- step 6. open the project in ESS (if you already have it open go to `File > Open` or `CTRL + O` on Windows).

## script

![](https://github.com/joshschmelzle/resequence_esx_ap_numbers/blob/master/resequenceAPs.png)

## before

![](https://github.com/joshschmelzle/resequence_esx_ap_numbers/blob/master/aruba325before.PNG)

## after

![](https://github.com/joshschmelzle/resequence_esx_ap_numbers/blob/master/aruba325after.PNG)

# caveat

- All of the AP names and #'s that were in the AP name will change. this is okay for me, but you might care about this. don't use this script if that is the case.

# license

project license can be found [here](https://github.com/joshschmelzle/netsh_quality_to_dbm/blob/master/LICENSE)
