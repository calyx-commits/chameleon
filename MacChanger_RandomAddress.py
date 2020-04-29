import re
import subprocess
from random import choice, randint

print('''Welcome to CHARIMAN, your all-in-one Macchanger. Review our instructions here
1 - manual (enter your desired New MacAddrress)
2 - automatic (random MacAddress will be assigned)
''')

inp = input()
network_interface = input('Please enter your network interface here: ')

def main():
    if inp == '1':
        new_mac = input('Please enter your desired MacAddress: ').strip()
        change_mac(network_interface, new_mac)
    elif inp == '2':
        random = mac_random()
        print(random)
        change_mac(network_interface, random)

def mac_random():
    cisco = ['00','40','96']
    dell = ['00','14','22']

    mac_address = choice([cisco,dell])

    for i in range(3):
        one = choice(str(randint(0,9)))
        two = choice(str(randint(0,9)))
        three = (str(one + two))
        mac_address.append(three)
    return ':'.join(mac_address)

def change_mac(network_interface,new_mac):

    subprocess.call(['ifconfig ' + str(network_interface) + ' down'], shell = True)

    subprocess.call(['ifconfig ' + str(network_interface) + ' hw ether ' + str(new_mac)+ ' '], shell=True)

    subprocess.call(['ifconfig ' + str(network_interface) + ' up'], shell=True)

def current_mac():
    output = subprocess.check_output(['ifconfig '+'wlan0'], shell = True)

    current_mac = re.search('\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', str(output))

    print('Old Mac address is {} and new Mac address is {}'. format(current_mac, new_mac))

if __name__ == '__main__':
    main()