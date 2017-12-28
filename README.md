Gary Lim
Dec 27, 2017
Version 1 Rev 0
Python 3.6
This Python script retrieves the configuration of a Ciena Waveserver.
The DNS name or IP addresses of the Ciena Waveserver is listed in a separate file.
This script will read the DNS name or IP address from the file:
python waveserver_config.py <ip_address_filename>
The script will save the save the configuration of each Ciena Waveserver in the directory
/Users/garylim/python_projects/ssh_waveserver_scripts/<today's date>
If there is an error connecting to the target device, the script will write an error.log
in the same directory as the config files called error.log
