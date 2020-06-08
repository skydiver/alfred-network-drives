#!/usr/local/bin/python3

import os
import subprocess
import re
import json

types = ['smbfs', 'afpfs']
mounts = []

mount = subprocess.getstatusoutput('mount -v')
lines = mount[1].split('\n')
for line in lines:
    matching = any(word in line for word in types)
    if matching:
        path = re.search(r'on\s(.*?)\s\(', line).group(1)
        user = re.search(r'by\s(.*?)\)', line).group(1)
        name = os.path.basename(path)
        mounts.append({
            "arg": path,
            "title": name,
            "subtitle": "Mounted by {} at {}".format(user, path)
        })


if len(mounts) == 0:
    mounts.append({
        "title": "No mounted network drives found",
    })


print(json.dumps({"items": mounts}, indent=2))