#!/usr/bin/env python
# coding: utf-8

# In[2]:


#importing libraries requests and socket
#A BIG THANKYOU TO GEEKS FOR GEEKS FOR PROVIDING ME WITH THE INSPIRATION FOR THIS IDEA. 
#credits=https://www.geeksforgeeks.org/how-to-make-a-subdomain-scanner-in-python/
import requests
import socket
print("""
  ______ _   _ _      _____  _____ _______ ____  _____  
 |  ____| \ | | |    |_   _|/ ____|__   __|___ \|  __ \ 
 | |__  |  \| | |      | | | (___    | |    __) | |__) |
 |  __| | . ` | |      | |  \___ \   | |   |__ <|  _  / 
 | |____| |\  | |____ _| |_ ____) |  | |   ___) | | \ \ 
 |______|_| \_|______|_____|_____/   |_|  |____/|_|  \_\  version 1.0
                                                        
Disclaimer: Developer assume no liability and are not responsible for any damages caused by ENLIST3R.
This tool is meant to be a test project and used only for education purposes only.
""")
#define method Request
def request(url):
    #if method does not requests return subdomain, then pass
    try:
        return requests.get("http://"+url)
        
        
    except requests.exceptions.ConnectionError:
        pass
#taking user input
target_url=str(input("enter website name Please only use website.com, do not include www or https :"))
flag=0
#Eror checks for the user to not input https , http, www,/ and //
while flag==0:
    #if found, throw error
    if target_url.find('https') != -1 or target_url.find('http') != -1 or target_url.find('www') != -1 or target_url.find('/') != -1 or target_url.find('//') != -1:
        print("Input error")
        target_url=str(input("enter website name Please only use website.com, do not include www or https :"))
    else:
        flag=1
#open subdomain txt.
#Credits to https://github.com/rbsec/dnscan/blob/master/subdomains.txt, Author- rbsec
#keeping subdomains.txt in same folder
with open("subdomains.txt","r") as wordlist_file:
    #for loop to test for subdomains
    for line in wordlist_file:
        word = line.strip()
        test_url = word + "." + target_url
        #check response
        response = request(test_url)
        if response:
            #if response is true, search for ip address
            ip_address=(socket.gethostbyname(test_url))
            print(
            "\nDiscovered subdomain -->" + test_url+
            "\nIp address :"+ ip_address)


# In[ ]:




