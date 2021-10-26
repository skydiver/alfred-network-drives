#!/usr/bin/python3

import json
from drives import get_network_drives

mounts = []
drives = get_network_drives()

for drive in drives:
    mounts.append({
        "arg": drive['path'],
        "title": drive['name'],
        "subtitle": "Mounted by {} at {}".format(drive['user'], drive['path'])
    })


if len(mounts) == 0:
    mounts.append({
        "title": "No mounted network drives found",
    })
else:
    mounts.append({
        "arg": "all",
        "title": "* Unmount all *",
        "subtitle": "Unmount all your network drives",
    })


print(json.dumps({"items": mounts}, indent=2))