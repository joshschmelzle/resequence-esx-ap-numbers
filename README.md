# resequence_esx_ap_numbers

Rename and resequence Ekahau Site Survey's (ESS) Access Point (AP) names using Python.

Project contents for Ekahau Site Survey are stored as a compressed file with an extension `.esx`. Inside, it contains several JavaScript Object Notation (JSON) files that help organize project data. One of them called `accessPoints.json` contains information for the project's Access Points. 

This script opens the `.esx` file, pulls out the `accessPoints.json`, renames and resequences the AP names/numbers, and then repackages the project file. The script will create a backup before doing anything to your project. 

It's important to note that all AP names will change, and the number included in the name is re-sequenced in no particular order.

> **WARNING: the number in the original name will in no particular order be changed. if you care about your existing AP numbers don't use this script.**

# requirements

Python 3.5 or greater installed.

Tested with Python 3.6.4, Windows 10 Enterprise (10.0.16299 N/A Build 16299), Ekahau ESS Pro 9.2.5.260. 

# usage

Run this script from the same directory as your .esx project.

# todo

- [ ] implement args parsing
- [ ] use `.esx` project instead of `projectFile = "sample.esx"`
- [ ] refactor
- [ ] add logging

# example output

```
>new-esx-file-update-accesspoints-json.py
current directory: C:\Users\josh\dev\python\ekahau-ap-rename
file: sample.esx
name: sample
extension: esx
current: C:\Users\josh\dev\python\ekahau-ap-rename\sample.esx
backup: C:\Users\josh\dev\python\ekahau-ap-rename\sample.20181217t080936.esx.bak
accessPoints.json is 8995 bytes
copy of old json wrote to accessPoints.old.20181217t080936.json
accessPoints.old.20181217t080936.json is 11594 bytes
old: Aruba AP-325 (22) - new: AP1
old: Aruba AP-325 (13) - new: AP2
old: Aruba AP-325 (24) - new: AP3
old: Aruba AP-325 (16) - new: AP4
old: Aruba AP-325 (7) - new: AP5
old: Aruba AP-325 (19) - new: AP6
old: Aruba AP-325 (21) - new: AP7
old: Aruba AP-325 (1) - new: AP8
old: Aruba AP-325 (6) - new: AP9
old: Aruba AP-325 (11) - new: AP10
old: Aruba AP-325 (9) - new: AP11
old: Aruba AP-325 (2) - new: AP12
old: Aruba AP-325 (5) - new: AP13
old: Aruba AP-325 (23) - new: AP14
old: Aruba AP-325 (15) - new: AP15
old: Aruba AP-325 (4) - new: AP16
old: Aruba AP-325 (14) - new: AP17
old: Aruba AP-325 (20) - new: AP18
old: Aruba AP-325 (10) - new: AP19
old: Aruba AP-325 (12) - new: AP20
old: Aruba AP-325 (8) - new: AP21
old: Aruba AP-325 (18) - new: AP22
old: Aruba AP-325 (3) - new: AP23
old: Aruba AP-325 (17) - new: AP24
copy of new json wrote to accessPoints.new.20181217t080936.json
accessPoints.new.20181217t080936.json is 11282 bytes
```

# license

project license can located [here](https://github.com/joshschmelzle/resequence_esx_ap_numbers/blob/master/LICENSE)
