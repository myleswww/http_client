# -*- coding: utf-8 -*-


#Author: Myles Wright
#Date: 09/10/2020
#Filename: request.py
#HTTP client that sends a request to https://httpbin.org 

import json
import socket
import re
import sys


#request class
class request(object):
    method = " "
    path = " "
    version = "HTTP/1.1"
    headers = {"Host": "httpbin.org",
               "User-Agent": "Mozilla/5.0",
               "Accept": "*",
               "Accept-Language": "en-US,en; q=0.5",
               "Accept-Encoding": "gzip, deflate, br",
               "Referer": "https://developer.mozilla.org/testpage.html",
               "Connection": "keep-alive",
               "Upgrade-Insecure-Requests": "1",
               "Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.7"
               }    
    data = " " 
    
    

    def setMethod(self, type_input): #recieved a positional argument error for both setMethod and setPath. added a throwaway variable 'a' to deal with this, LOL
        """set the method to GET or POST"""
        self.method = type_input
        return type_input
        

    def setPath(self, input):
        """set the path to the target resource"""
        self.path = input
        return input
        

    def setData(self, input):
        """add the data for POST requests"""
        self.data = input
        return input

    def addHeader(self, header, value):
        """add a header to the request"""
        self.headers[header] = value



    def get_headers(self):
        """returns a string of correctly formatted dictionary items"""
        formatted_headers = "\n"
        print("Formatting headers...")
        for key, value in self.headers.items():
            formatted_headers = formatted_headers + f"{key}: {value}\n"
        #print(formatted_headers)
        return formatted_headers

    def toString(self):
        """prints the request formatted like we saw in class(use json)"""
        #print(self.data)
        return self.data

    def __init__(self, type_input, path):
        """Does everything to return a string of the data"""
        sp = " "
        self.method =  self.setMethod(type_input)
        self.path = self.setPath(path)
        
        self.data = str(self.method + sp + self.path + sp + self.version + self.get_headers() + "\n")
        