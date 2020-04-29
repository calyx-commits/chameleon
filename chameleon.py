import re
import subprocess

network_interface = input('Please enter your network interface: ').strip()
new_mac = input('Please enter your desired MacAddress: ').strip()

def change_mac(network_interface,new_mac):
    subprocess.call(['ifconfig ' + str(network_interface) + ' down'], shell = True)
    subprocess.call(['ifconfig ' + str(network_interface) + ' hw ether ' + str(new_mac)+ ' '], shell=True)
    subprocess.call(['ifconfig ' + str(network_interface) + ' up'], shell=True)

def current_mac():
    output = subprocess.check_output(['ifconfig '+'wlan0'], shell = True)
    current_mac = re.search('\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', str(output))
    print('Old Mac address is {} and new Mac address is {}'. format(current_mac, new_mac))

change_mac(network_interface,new_mac)
current_mac() 