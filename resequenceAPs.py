#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" A utility will rename and resequence Ekahau Site Survey AP names

* The AP name will never include a number higher than the total number of APs listed in accessPoints.json.
* WARNING: The original number that is in the AP name will change. You may care about this, and if so, don't use this script.
* Use at your own risk and always make a backup before you test.

CREDITS: Or Weis for the UpdateableZipFile class

TODO: MAJOR REFACTOR
"""

__author__ = "Josh Schmelzle"
__version__ = "0.0.2"
__status__ = "Alpha"

import shutil
import datetime
import os
import zipfile
from zipfile import ZipFile, ZIP_STORED, ZipInfo
import tempfile
import json
import filecmp
import sys

class UpdateableZipFile(ZipFile):
    """
    Add delete (via remove_file) and update (via writestr and write methods)
    To enable update features use UpdateableZipFile with the 'with statement',
    Upon  __exit__ (if updates were applied) a new zip file will override the exiting one with the updates
    """

    class DeleteMarker(object):
        pass

    def __init__(self, file, mode="r", compression=ZIP_STORED, allowZip64=False):
        # Init base
        super(UpdateableZipFile, self).__init__(file, mode=mode,
                                                compression=compression,
                                                allowZip64=allowZip64)
        # track file to override in zip
        self._replace = {}
        # Whether the with statement was called
        self._allow_updates = False

    def write(self, filename, arcname=None, compress_type=None):
        arcname = arcname or filename
        # If the file exits, and needs to be overridden,
        # mark the entry, and create a temp-file for it
        # we allow this only if the with statement is used
        if self._allow_updates and arcname in self.namelist():
            temp_file = self._replace[arcname] = self._replace.get(arcname,
                                                                   tempfile.TemporaryFile())
            with open(filename, "rb") as source:
                shutil.copyfileobj(source, temp_file)
        # Otherwise just act normally
        else:
            super(UpdateableZipFile, self).write(filename, 
                                                 arcname=arcname, compress_type=compress_type)

    def __enter__(self):
        # Allow updates
        self._allow_updates = True
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # call base to close zip file, organically
        try:
            super(UpdateableZipFile, self).__exit__(exc_type, exc_val, exc_tb)
            if len(self._replace) > 0:
                self._rebuild_zip()
        finally:
            # In case rebuild zip failed,
            # be sure to still release all the temp files
            self._close_all_temp_files()
            self._allow_updates = False

    def _close_all_temp_files(self):
        for temp_file in self._replace.values():
            if hasattr(temp_file, 'close'):
                temp_file.close()

    def _rebuild_zip(self):
        tempdir = tempfile.mkdtemp()
        try:
            temp_zip_path = os.path.join(tempdir, 'new.zip')
            with ZipFile(self.filename, 'r') as zip_read:
                # Create new zip with assigned properties
                with ZipFile(temp_zip_path, 'w', compression=self.compression,
                             allowZip64=self._allowZip64) as zip_write:
                    for item in zip_read.infolist():
                        # Check if the file should be replaced / or deleted
                        replacement = self._replace.get(item.filename, None)
                        # If marked for deletion, do not copy file to new zipfile
                        if isinstance(replacement, self.DeleteMarker):
                            del self._replace[item.filename]
                            continue
                        # If marked for replacement, copy temp_file, instead of old file
                        elif replacement is not None:
                            del self._replace[item.filename]
                            # Write replacement to archive,
                            # and then close it (deleting the temp file)
                            replacement.seek(0)
                            data = replacement.read()
                            replacement.close()
                        else:
                            data = zip_read.read(item.filename)
                        zip_write.writestr(item, data)
            # Override the archive with the updated one
            shutil.move(temp_zip_path, self.filename)
        finally:
            shutil.rmtree(tempdir)
            
def main():
    projectFile = "sample.esx"
    fileName ="accessPoints.json"
    
    projectFile = "sample.esx"
    cwd = os.getcwd()
    current = "{}\{}".format(cwd, projectFile)
    projectExtension = projectFile.rsplit('.', 1)[0]
    projectName = projectFile.rsplit('.', 1)[1]
    
    # ISO 8601 YYYYMMDDtHHMMSS 20181216t172303 
    now = datetime.datetime.now().replace(microsecond=0).isoformat().replace("-", "").replace(":", '').lower()
    backup = current.rsplit('.', 1)[0] + "." + now + ".esx.bak"
    
    print("current directory: {}".format(cwd))
    print("file: {}".format(projectFile))
    print("name: {}".format(projectExtension))
    print("extension: {}".format(projectName))
    print("current: {}".format(current))
    print("backup: {}".format(backup))
    
    # make a backup of the current project
    shutil.copy2(current, backup)
    
    # make sure the backup file is the same, if not, do not continue.
    if (filecmp.cmp(current, backup)):
        # make sure file is actually an archive that zipfile can handle.
        if (zipfile.is_zipfile(current)): 
            data = object()
            newapfile = ""
            
            with zipfile.ZipFile(current, 'r') as zip:
                #print("namelist(): {}".format(zip.namelist()))
                #print("infolist(): {}".format(zip.infolist()))
                try:
                    info = zip.getinfo(fileName)
                    content = zip.read(fileName)
                    print("{} is {} bytes".format(info.filename, info.file_size))
                    
                    data = json.loads(content)
                    
                    oldapfile = "accessPoints.old." + now + ".json"
                    
                    # write existing json to file
                    with open(oldapfile, 'w') as out:
                        json.dump(data, out, indent=4)
                    
                    print("copy of old json wrote to {}".format(oldapfile))
                    print("{} is {} bytes".format(oldapfile, os.path.getsize(oldapfile)))
                    
                    num = 1
                    
                    for ap in data['accessPoints']:
                        old = ap["name"]
                        ap["name"] = "AP{}".format(num)
                        new = ap["name"]
                        print("old: {} - new: {}".format(old, new))
                        num = num + 1
                    
                    #print(data) #todo write to filev
                    
                    now = datetime.datetime.now().replace(microsecond=0).isoformat().replace("-", "").replace(":", '').lower()
                    newapfile = "accessPoints.new." + now + ".json"
                    
                    # write modified json
                    with open(newapfile, 'w') as out:
                        json.dump(data, out, indent=4)
                        
                    print("copy of new json wrote to {}".format(newapfile))
                    print("{} is {} bytes".format(newapfile, os.path.getsize(newapfile)))
                except KeyError:
                    print("ERROR: did not find {} in {}".format(fileName, projectFile))
            
            with UpdateableZipFile(current, "a") as o:
                o.write(newapfile, fileName)
        else:
            print("problem opening with zipfile")
    else:
        print("exiting because could not validate backup file against the original.")
 
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(-1)
    sys.exit(0)
