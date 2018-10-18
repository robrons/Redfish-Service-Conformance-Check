##################################################################################################
# File: TEST_manager.py 
# Description: Redfish service conformance check tool. This module contains assertions for 
# EventService
#
# Verified/operational Python revisions (Mac OS) :
#       3.4.3
#
# Initial code released : 09/2018
#   Robin Ronson ~ Texas Tech University
##################################################################################################
import sys
from schema import SchemaModel
from collections import OrderedDict
from xml.dom import minidom
import re
import rf_utility
import datetime
import xml.etree.ElementTree as ET
import urllib

# map python 2 vs 3 imports
if (sys.version_info < (3, 0)):
    # Python 2
    Python3 = False
    from urlparse import urlparse
    from StringIO import StringIO
    from httplib import HTTPSConnection, HTTPConnection, HTTPResponse
    import urllib
    import urllib2
    from urllib import urlopen
else:
    # Python 3
    Python3 = True
    from urllib.parse import urlparse
    from io import StringIO
    from http.client import HTTPSConnection, HTTPConnection, HTTPResponse
    from urllib.request import urlopen


import ssl
import re
import json
import argparse
import base64
import datetime
import types
import socket
import select
import os
import os
from collections import OrderedDict
import time

##################################################################################################
# Description: The value of this property shall be a link to a collection of type
# EthernetInterfaceCollection
# Name: Assertion_MANA111(self, log)
##################################################################################################
def Assertion_MANA111(self, log):

    log.AssertionID = 'MANA111'
    assertion_status =  log.PASS
    log.assertion_log('BEGIN_ASSERTION', None)

    relative_uris = self.relative_uris
    authorization = 'on'
    rq_headers = self.request_headers()

    try:
        json_payload_get, headers, status = self.http_GET(relative_uris['Root Service_Managers_Members_1_EthernetInterfaces_Members_1'], rq_headers, authorization)

        print(json.dumps(json_payload_get, indent=4, sort_keys=True))
        
    except:
        assertion_status = log.WARN        
        log.assertion_log('line', "Managers property is absent.")
        return (assertion_status)

# run(self, log):
# Takes sut obj and logger obj
###################################################################################################
def run(self, log):
    assertion_status = Assertion_MANA111(self,log)
