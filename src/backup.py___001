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








#print gpg.list_keys()
#print "\n#####   '%s'   #########\n" % len(gpg.list_keys())
#print gpg.list_keys(True)
#print "\n#####   '%s'   #########\n" % len(gpg.list_keys(True))



#file_name           = '/home/david/dummy_xxx/filexxx.txt'
#file_name_encrypted = '/home/david/dummy_xxx/filexxx_encrypted'
#fh_00 = open(file_name, "rb")
#encrypted_ascii_data = gpg.encrypt_file(fh_00, 'david.mcallister@asicanalytic.com', always_trust=True, output=file_name_encrypted)
#fh_00.close()


#fh_00 = open(file_name_encrypted, "rb")
#decrypted_data = gpg.decrypt_file(fh_00)

#print "\niiiiiiiiiiiiiiiiiiiiiiiiiiii\n"
#print decrypted_data
#print "\niiiiiiiiiiiiiiiiiiiiiiiiiiii\n"

#fh_00.close()


te = te.time_extra()
es = es.encrypt_support()
ts = ts.tarfile_support()



parser = argparse.ArgumentParser(description="Run Backup Program")
group_1 = parser.add_mutually_exclusive_group()
group_1.add_argument("-v", "--verbose",     action="store_true")
group_1.add_argument("-q", "--quiet",       action="store_true")
group_2 = parser.add_mutually_exclusive_group()
group_2.add_argument("-f", "--full",        action="store_true")
group_2.add_argument("-i", "--incremental", action="store_true")



parser.add_argument("-r", "--backup_report", type=str, help="Path to backup report file, (backup_report.py)")
args = parser.parse_args()

if args.backup_report:
   if not os.path.exists(args.backup_report):
      print "backup reports file does not exist.  File 'backup_report.py is expexted.  Run this program without any options to create a new backup_report.py file.   '%s'" % args.backup_report
      sys.exit()
else:
   print "Set the path for the config file INSIDE the newly created backup_report.py and then re-run this script using the --backup_report option."
   backup_obj.initialize_backup_report_file( __file__, __version__, __date__, __author__ )






if args.quiet:
   print "{}".format( os.path.basename(args.backup_report) )
elif args.verbose:
   print "Full Path {}".format( os.path.abspath(args.backup_report) )
else:
   print args.backup_report





def main():

   struct_time_start = time.gmtime()

#Origgg   backup_obj = backup_support.Back_Up(struct_time_start)
#Origgg   backup_obj.set_backup_type(True)
#Origgg   backup_obj.set_backup_status()




#Origgg   ( do_backup_now, backup_type, backup_set_epoch, backup_epoch, backup_set_does_exist ) = backup_obj.is_backup_scheduled_now()
#Origgg#   print "\nTTTYYYPPPEEE    '%s'    '%s'    '%s'\n" %  ( do_backup_now, backup_epoch, backup_type )
#Origgg
#Origgg   create_new_backup_set = False
#Origgg   if args.full: # Create new backup set
#Origgg      # Create new 'FULL'
#Origgg      create_new_backup_set = True
#Origgg      tttttttt = backup_support.BackUp_Set(struct_time_start, create_new_backup_set)
#Origgg
#Origgg      print "TTTTTTTTTTTT   %s" % struct_time_start
#Origgg   elif args.incremental: # Create new backup set
#Origgg      if backup_set_does_exist:
#Origgg         # Create new 'incremental' from latest backup set
#Origgg         get_existing_backup_set = backup_support.BackUp_Set(backup_set_epoch, create_new_backup_set)
#Origgg      else: # An incremental cannot be done since no backup sets exist.  A full backup will be done instead.
#Origgg         # Create new 'FULL'
#Origgg         create_new_backup_set = True
#Origgg         tttttttt = backup_support.BackUp_Set(struct_time_start, create_new_backup_set)
#Origgg
#Origgg      print "TTTTTTTTTTTT   %s" % struct_time_start
#Origgg   elif do_backup_now:
#Origgg      if backup_type  ==  'FULL': # Create new backup set
#Origgg         if backup_set_epoch  !=  backup_epoch:
#Origgg            print "ERROR:  At FULL backups, backup_set_epoch and backup_epoch should be the same epoch  '%s' / '%s'" % ( backup_set_epoch, backup_epoch )
#Origgg
#Origgg         # Create new 'FULL'
#Origgg         create_new_backup_set = True
#Origgg         tttttttt = backup_support.BackUp_Set(backup_set_epoch, create_new_backup_set)
#Origgg
#Origgg      else: # backup is incremental
#Origgg         if backup_set_does_exist:
#Origgg            # Create new 'incremental' from latest backup set
#Origgg            get_existing_backup_set = backup_support.BackUp_Set(backup_set_epoch, create_new_backup_set)
#Origgg         else: # An incremental cannot be done since no backup sets exist.  A full backup will be done instead.
#Origgg            # Create new 'FULL'
#Origgg            create_new_backup_set = True
#Origgg            tttttttt = backup_support.BackUp_Set(backup_set_epoch, create_new_backup_set)
#   else:
#      print "RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR"
#      tttttttt = backup_support.BackUp_Set(1381392600, False)

# Questions
#   1) Are there backups before this?
#   2) What is the most recent backup set?
#   3) Do any backup sets exist?
#   4) Is the backup to be done now?
#   5) Is the backup go-ahead coming from the schedule or from manual override?
#   6) What is the epoch time of the backup to be run?
#   7) What is the type of backup?



# Backup schedule
# Record of backups made
# Every Backup
#   - file 1
#       - file is python code containing backup options as a dictionary
#       - file name contains backup date / time
#   - file 2
#       - for each repository backup report
#
# where
#               - repo location(s)
# what
#               - program name / author / date / version
#               - backed up file/dirs
# when
#               - backup date / time
# how
# why
# results
#               - successful yes / no
#               - atomic yes / no

#   print "\n\n"
#   print " This running program is executing this file"
#   print "    Running program:   %s" % os.path.abspath(sys.argv[0])
#   print "    This file:         %s" % os.path.abspath(__file__)
#   print "\n\n"


#f = open('binaryfile.bin')
#h = hashlib.sha1()
#h.update(f.read())
#hash = h.hexdigest()
#f.close()


#   Algorithm
#    start program
#       reads current time
#       reads latest back config_file and report_file
#       if (config file changed) or (no config file found) or (manual start) or (SHA1's of most recent backup set have changed)
#          ->  backup FULL
#          check atomic
#          notify owners if issues arose
#          dump latest config file
#          dump backup report (include SHA1s of current backup set)
#       else
#          is this a valid backup date
#             if backup type FULL
#                ->  backup FULL
#                check atomic
#                notify owners if issues arose
#                dump latest config file
#                dump backup report (include SHA1s of current backup set)
#             elif backup type incremental
#                ->  backup incremental
#                check atomic
#                notify owners if issues arose
#                dump latest config file
#                dump backup report (include SHA1s of current backup set)


# ******************   RETRIEVE NEXT BACKUP TIME / TYPE   ******************

#   print "\n\n\n FILE_NAME   '%s'\n" % backup_obj.get_dir_name()




   ###########################################################################
   ###########################################################################
   ########################                            #######################
   ########################   CREATE BACKUP TAR FILE   #######################
   ########################                            #######################
   ###########################################################################
   ###########################################################################
#Origgg   sha1_codes = {}
#Origgg   tar_file_basename = backup_obj.get_dir_name() + '.tar.gz'
#Origgg   tmp_tar_file_basename = '/tmp/' + tar_file_basename
#Origgg   backup_is_atomic = False
#Origgg   for ii_001 in range(0,5): # Try for several iterations to increase chances of achieving an atomic backup.
#Origgg                             # An atomic backup will only fail if one or more files are changing during the
#Origgg                             # tar operation.  If both consecutive tar files are recursively identical, then
#Origgg                             # the backup is atomic.
#Origgg      for tar_file in [tar_file_basename, tmp_tar_file_basename]:
#Origgg         #ts.create_gziped_tar_file( tar_file, backup_conf.config['files_dirs'], te.date_to_epoch(time.gmtime()) )
#Origgg         if not ts.create_gziped_tar_file( tar_file, backup_conf.config['files_dirs'], None ):
#Origgg            sys.exit()
#Origgg
#Origgg      if backup_support.UniversalDiff(tar_file_basename, tmp_tar_file_basename):
#Origgg         backup_is_atomic = True
#Origgg         sha1_codes[tar_file_basename] = es.calc_sha1_for_file( tar_file_basename )
#Origgg         break
#Origgg
#Origgg   if not backup_is_atomic:
#Origgg      logging.warning("Backup performed, but it is not atomic.  Some files were being modified while the backup was taking place.")




   ###########################################################################
   ###########################################################################
   #######################                             #######################
   #######################   ENCRYPT BACKUP TAR FILE   #######################
   #######################                             #######################
   ###########################################################################
   ###########################################################################
#Origgg   tar_file_encrypted = tar_file_basename +'.gpg'
#Origgg   es.gpg_encrypt_file(tar_file_basename, tar_file_encrypted, 'david.mcallister@asicanalytic.com', '/home/david/.gnupg')
#Origgg   sha1_codes[tar_file_encrypted] = es.calc_sha1_for_file( tar_file_encrypted )



   ###########################################################################
   ###########################################################################
   #######################                              ######################
   #######################   PRINT BACKUP REPORT FILE   ######################
   #######################                              ######################
   ###########################################################################
   ###########################################################################
#   # pretty print
#   config_pretty = backup_obj.get_dir_name() + '.py'
#   fh_01 = open(config_pretty, 'w')
#   fh_01.write('config = ')
#   pprint.pprint(backup_conf.config, fh_01)
#   fh_01.close()




#Origgg   config_yaml = backup_obj.get_dir_name() + '.yaml'
#Origgg   fh_config_file = open(config_yaml,'w')
#Origgg   yaml_all_00 = yaml.dump(backup_conf.config,  fh_config_file,  line_break=True, default_flow_style=False, indent = 8)
#Origgg   fh_config_file.close()
#Origgg
#Origgg   fh_yaml_in = open(config_yaml, 'r')
#Origgg   whatever = yaml.safe_load(fh_yaml_in)
#Origgg   fh_yaml_in.close()




   ###########################################################################
   ###########################################################################
   ##########################                        #########################
   ##########################   WRITE BACKUP FILES   #########################
   ##########################                        #########################
   ###########################################################################
   ###########################################################################
#Origgg   all_backup_dirs = [ backup_conf.config['backup_location_reference'] ] + backup_conf.config['backup_location_others']
#Origgg   for backup_dir in all_backup_dirs:
#Origgg      backup_dir_full = backup_dir + '/' + backup_obj.get_dir_name()
#Origgg      if os.path.exists(backup_dir_full):
#Origgg         logging.error("Backup directory already exists  '%s'" % (backup_dir_full))
#Origgg
#Origgg      sub_dir = backup_dir_full + '/' + 'backup'
#Origgg      if not os.path.exists(sub_dir):
#Origgg         os.makedirs(sub_dir)
#Origgg      tar_file_destination = sub_dir + '/' + tar_file_encrypted
#Origgg      shutil.copyfile(tar_file_encrypted, tar_file_destination)
#Origgg      if not filecmp.cmp(tar_file_encrypted, tar_file_destination):
#Origgg         logging.warning("Tar file not copied successfully  '%s'" % tar_file_destination)



# ******************   CALCULATE NEXT BACKUP TIME / TYPE   ******************



   return( True )

if __name__ == "__main__":
   main()



