
#!/usr/bin/env python3

import subprocess
from pythonping import ping
import socket
import os

os.system('figlet Range-Scanner')

print("\033[0;32;1m")
print("""----------------------------------------------
Developed by Swam Htet Aung => Made in Myanmar
""")

# color
green = '\033[0;32;1m'
white = '\033[0;37;0m'
yellow = '\033[0;33;1m'
red = '\033[0;31;1m'


print(yellow)

ip = input("Enter you ip to scan => ")
start = int(input("Enter start number to scan => "))
end = int(input("Enter end number to scan => "))
print('\n')

split_ip = ip.split('.')	# split ip by .

# remove back from ip to scan
to_scan = split_ip[0] + '.' + split_ip[1] + '.' + split_ip[2]

for ip_range in range(start, end + 1):	# scan ip range
	scanning = to_scan + f".{ip_range}"

	ping_ip = subprocess.call(["ping", "-c", "1", "-n", "-W", "2", ip], stdout=subprocess.DEVNULL)

	if subprocess.call(["ping", "-c", "1", "-n", "-W", "2", ip], stdout=subprocess.DEVNULL):	# online = 0
		print(f"{green}{scanning}{white} is online")
		try:
			web = socket.gethostbyaddr(scanning)	# web detect
			print(f"{green}web detect {web}\n{white}")

		except:
			print(f'{red}no web found\n{white}')

	else:
		print(f"{scanning} is offline\n")