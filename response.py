# -*- coding: utf-8 -*-


#Author: Myles Wright
#Date: 09/10/2020
#Filename: response.py
#HTTP client that sends a request to https://httpbin.org 

import json
import socket
import re
import sys

class response(object):
    version = ""
    code = 0
    message = ""
    headers = {}
    data = {}
    
    def __init__(self, response):
        """set the response headers in the class dict object"""
        
        self.data = response


    def getHeader(self, header):
        """return the value of the specified header"""
        return self.headers[header]



    def getData(self):
        """return just the data from the response"""
        return self.headers[1]



    def toString(self):
        """prints the request formatted like we saw in class"""
        
        return self.data



