#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" A utility will rename and resequence Ekahau Site Survey AP names

* The AP name will never include a number higher than the total number of APs listed in accessPoints.json.
* WARNING: The original number that is in the AP name will change. You may care about this, and if so, don't use this script.
* Use at your own risk and always make a backup before you test.
"""

__author__ = "Josh Schmelzle"
__version__ = "0.0.1"
__status__ = "Alpha"

import argparse
import json
import sys

def initialize():
    parser = argparse.ArgumentParser(
        description="Renames and resequences Ekahau Site Surveys accessPoints.json.",
        epilog="Made with Python by {}".format(__author__),
        fromfile_prefix_chars='@'
        )
        
    parser.add_argument('command', nargs="?", default="rename", help="default argument. initiates the renaming of AP names in accessPoints.json", choices=['rename'])
    parser.add_argument('-V', '--version', action="version", version="%(prog)s {}".format(__version__))
    
    return parser

def main():
    data = object()
    filename = 'accessPoints.json'
    try:
        with open(filename) as file:
            data = json.load(file)
            
            x = 1
            
            for i in data['accessPoints']:
                old = i["name"]
                i["name"] = "AP{}".format(x)
                new = i["name"]
                x = x + 1
                print("old: {} - new: {}".format(old, new))
        
        # write modified json to new file
        with open('accessPoints-resequenced.json', 'w') as out:
            json.dump(data, out)
    except FileNotFoundError:
        print("could not find {}".format(filename))
    except ValueError:
        print("could not decode {} as json".format(filename))

if __name__ == '__main__':
    parser = initialize()
    try:
        args = parser.parse_args()
        if args.command == 'rename':
            main()
    except KeyboardInterrupt:
        logger.critcial("stop requested...")
        sys.exit(-1)
    sys.exit(0)
