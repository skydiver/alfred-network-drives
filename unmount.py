#!/usr/bin/python3

import subprocess
from drives import get_network_drives

drives = get_network_drives()

for drive in drives:
    command = "umount {}".format(drive['path'])
    mount = subprocess.getstatusoutput(command)
