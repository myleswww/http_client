# -*- coding: utf-8 -*-


#Author: Myles Wright
#Date: 09/10/2020
#Filename: http_client.py
#HTTP client that sends a request to https://httpbin.org 

import json
import socket
import re
import sys
from request import request
from response import response


def send_socket(message):
    ''' This function sends a string message over TCP'''
    #Most of this function I took from the slides on canvas. There are other ways to do this that I found but I like this one the most.

    server = 'httpbin.org'
    port = 80
    try:
        print("Connecting...")
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((server, port))
    except ConnectionError:
        print("Error connecting... ")
        sys.exit(1)
    try:
        print("Sending...")
        sock.sendall(bytes(message, 'UTF-8'))
        print("Sent!" + "\n")
    except socket.error:
        print("Failed")
        sys.exit(1)
    try:
        print("Recieving response...")
        response = sock.recv(1024)
    except socket.RDS_RECVERR:
        print("Error recieving data...")
        sys.exit(1)
    return response
   





def main():
    #set up the request
    user_input = input("Request: ")
    a = re.split(' +', user_input)
    
    r = request(a[0], a[1])
    
    #send the request, assign it to response
    req = send_socket(r.toString())
    resp = response(req.decode('UTF-8'))
    print(resp.toString())
    #print(resp.decode('UTF-8'))




if __name__== '__main__':
    main()