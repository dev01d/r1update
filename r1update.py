#!/usr/bin/env python3

import os
import platform
import requests

r1_BetaURL = "http://beta.r1soft.com/modules/Ubuntu_2004_x64/"
kernel = platform.release()

# Variable matches released module branch
branch182 = "hcpdriver-cki-%s.182.ko" % kernel
branch209 = "hcpdriver-cki-%s.209.ko" % kernel
branch223 = "hcpdriver-cki-%s.223.ko" % kernel

# Backup server url/IP
backup_url = "https://"


def sysCalls():
    os.system("cp hcpdriver-cki-* /lib/modules/r1soft/")
    os.system("systemctl restart cdp-agent && systemctl status cdp-agent")
    os.system(
        "cd /lib/modules/r1soft/ && serverbackup-setup --get-key %s" % backup_url)


def main():
    req = requests.get(r1_BetaURL + branch182, allow_redirects=True)
    if req.status_code != 404:
        open(branch182, 'wb').write(req.content)
        sysCalls()
    else:
        req = requests.get(r1_BetaURL + branch209, allow_redirects=True)
        if req.status_code != 404:
            open(branch209, 'wb').write(req.content)
            sysCalls()
        else:
            req = requests.get(r1_BetaURL + branch223, allow_redirects=True)
            open(branch223, 'wb').write(req.content)
            sysCalls()


if __name__ == "__main__":
    main()
