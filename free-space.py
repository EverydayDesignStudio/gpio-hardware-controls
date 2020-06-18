#!/usr/bin/env python3

import psutil

path = '/'
bytes_available = psutil.disk_usage(path).free
megs_available = round(bytes_available / 1024 / 1024, 2)
gigs_available = round(bytes_available / 1024 / 1024 / 1024, 2)
print("{g} Gigabytes Available".format(g=gigs_available))
print("{m} Megabytes Available".format(m=megs_available))
