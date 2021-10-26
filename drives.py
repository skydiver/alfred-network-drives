#!/usr/bin/python3

import os
import subprocess
import re

types = ['smbfs', 'afpfs']

def get_network_drives():
    drives = []

    mount = subprocess.getstatusoutput('mount -v')
    lines = mount[1].split('\n')

    for line in lines:
        matching = any(word in line for word in types)
        if matching:
            path = re.search(r'on\s(.*?)\s\(', line).group(1)
            user = re.search(r'by\s(.*?)\)', line).group(1)
            name = os.path.basename(path)
            drives.append({
                "user": user,
                "path": path,
                "name": name,
            })

    return drives