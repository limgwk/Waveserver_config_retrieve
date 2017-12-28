# Gary Lim
# Dec 27, 2017
# Version 1 Rev 0
# Python 3.6
# This Python script retrieves the configuration of a Ciena Waveserver.
# The DNS name or IP addresses of the Ciena Waveserver is listed in a separate file.
# This script will read the DNS name or IP address from the file:
# python waveserver_config.py <ip_address_filename>
# The script will save the save the configuration of each Ciena Waveserver in the directory
# /Users/garylim/python_projects/ssh_waveserver_scripts/<today's date>
# If there is an error connecting to the target device, the script will write an error.log
# in the same directory as the config files called error.log

import paramiko
import getpass
from sys import argv
from time import sleep
from datetime import date
from os import path
from os import mkdir
import socket

def ssh_connect(ssh_ip_address, ssh_username, ssh_password):
	try:
		remote_conn_pre=paramiko.SSHClient()
		remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		remote_conn_pre.connect(ssh_ip_address, username=ssh_username, password=ssh_password, look_for_keys=False, allow_agent=False)
		print ("SSH connection establisehd to %s"%ssh_ip_address)

		remote_conn = remote_conn_pre.invoke_shell()
		print ("Interactive SSH session established")

		remote_conn.send("system shell session set more off\n")
		sleep(2)

		remote_conn.send("config show brief\n")
		sleep(2)
		output = remote_conn.recv(20000)

		ssh_buffer = output
		print (ssh_buffer) # For debugging
	
		target_dir = '/Users/garylim/python_projects/ssh_waveserver_scripts/' + str(date.today()) + '/'
		if not path.isdir(target_dir):
			mkdir(target_dir)
		
		# Save ssh output to file
		save_file = open(target_dir + ssh_ip_address + '-config-show.txt', 'wb')
		save_file.write(ssh_buffer)
		save_file.close()

	except socket.error:
		print(ssh_ip_address + "IP Connection Error") # For debugging
		target_dir = '/Users/garylim/python_projects/ssh_waveserver_scripts/' + str(date.today()) + '/'
		error_file = open(target_dir + 'error.log', 'a')
		error_file.write(ssh_ip_address + ' IP Connection Error\n')
		error_file.close()

# Main Program

script, filename = argv

username = input("Username: ")
password = getpass.getpass("Password: ")

ip_address_file = open(filename, 'r')

for ip_address in ip_address_file:
	ssh_connect(ip_address.strip(), username, password)
	
ip_address_file.close()