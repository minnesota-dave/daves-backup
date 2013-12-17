#!/usr/bin/python

import os

__version__  = '1.0'
__date__     = '2013-09-21'
__author__   = 'David McAllister'


print
print " FILE:      %s" % os.path.basename(__file__)
print " VERSION:   %s" % __version__
print " DATE:      %s" % __date__
#print " DATE_TIME: %s" % __datetime__
print " AUTHOR:    %s" % __author__
print


import sys
import tarfile
import logging
import shutil
import filecmp
import pprint
import hashlib
import time
import argparse
import yaml
import re

#import sys
#import time
#import datetime
#import pickle
#import textwrap

import backup_conf
import backup_support
import time_extra      as te
import encrypt_support as es
import tarfile_support as ts










te = te.time_extra()
es = es.encrypt_support()
ts = ts.tarfile_support()






print "\n\nCurrent directory is '%s'\n\n" % os.getcwd()



def touch( fname, times=None):
   with file( fname, 'a'):
      return_val = os.utime( fname, times)


touch_file_name_00 = "/home/david/daves-backup/src/MARKER_0000000000000000000000000000"
#touch( touch_file_name_00 )





def main():

   struct_time_start = time.gmtime()


# Get input
   #- run backup full
   #- run backup incremental
   #- run backup auto
   #- get most recent backup
   #- get next scheduled backup




   return( True )

if __name__ == "__main__":
   main()

