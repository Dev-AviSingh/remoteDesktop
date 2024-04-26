import os
def getFileInfo(path):
    info = {}
    info['type'] = 'file'
    info['isDirectory'] = False
    info['name'] = os.path.basename(path)
    info['size'] = os.path.getsize(path)
    info['last_modified'] = os.path.getmtime(path)
    return info


def listDrives():
    drives = []
    if os.name == 'nt':  # Check if the operating system is Windows
        drives = [d[0] + ':\\' for d in os.popen('wmic logicaldisk get caption').read().split()[1:] if len(d) == 2]
    return drives
