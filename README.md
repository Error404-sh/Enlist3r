# Enlist3r
Author- Manav Doshi (Error404z)
ENLIST3r is my first python project that searches for the subdomains and ip address of a given target url. This is a security recon tool helpful to both website owners and penetration testers. Please note that this tool is meant for education purposes only and the developer will not take any responsibilities for the damage caused by this tool.

# License
ENLIST3r is licenced under GNU General Public License v3.0.


# Dependencies
ENLIST3r runs on requests and socket module. They can be installed from the requirements.txt file.


# Installation on Windows:
python.exe -m pip install -r requirements.txt

# Installation on Linux:
sudo pip install -r requirements.txt

Alternatively, installation is possible even by single module at a time.

# Installation on Windows:
python.exe -m pip install requests
python.exe -m pip install socket

# Installation on Linux:
sudo pip install requests
sudo pip install socket

# HOW TO USE:
Run the script using python ENLIST3r.py and the program will ask for the name of the website for example- name.com and then will print the subdomains and the ip address for them. 
Please make sure you have subdomains.txt in the same folder as the python program. The best method would be to make a folder and add the program and the text file to the folder and open the terminal in the same.

# credits
GEEKSFORGEEKS for the idea and inspiration for the program.(https://www.geeksforgeeks.org/how-to-make-a-subdomain-scanner-in-python/)
Credits for the subdomain_txt file used in the code.( https://github.com/rbsec/dnscan/blob/master/subdomains.txt, Author- rbsec)

# Version
Current version is 1.0.
