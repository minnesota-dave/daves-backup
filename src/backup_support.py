
import os
import sys
import gnupg
import time
import calendar
import datetime
import tarfile
import gzip
import mimetypes
import filecmp
import re
import pprint
import fnmatch
import glob

import backup_conf
import time_extra as te




class BackUp_Set():


   def __init__(self, backup_time, create_new_backup_set=False):
#      print "\n backup  / type is   '%s'  /  '%s'\n" % ( backup_time, type(backup_time) )
#      self.epoch_time    = str( int( round( calendar.timegm( backup_time ) ) ) )
      self.epoch_time    = str( int( round( backup_time ) ) )
      self.backup_set_directory      = backup_conf.config['base_directory'] + '/' + backup_conf.config['backup_location_reference'] + '/' + self.epoch_time
      self.backup_set_full_directory = self.backup_set_directory + '/' + self.epoch_time
#      print "\n  backup_set_dir   '%s'\n" % self.backup_set_directory
      self.incrementals  = []
      self.latest_backup = None

      if create_new_backup_set:
         self._create_new_backup_set()
      else:
         self._load_backup_set()

#      print "JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ"
#      dddddd = backup_conf.config['base_directory'] + '/' + backup_conf.config['backup_location_reference'] + '/' + '1381392600'
#      for item in os.listdir(self.backup_set_directory):
#         if re.match('^(\d+)$', item):
#            print "DIR   /   item     '%s'  /  '%s'" % ( self.backup_set_directory, item)


#############################################################################
#   TBD   Start Here
   def _create_new_backup_set(self):
      if os.path.exists(self.backup_set_directory):
         print "ERROR:  Backup set directory already exists  '%s'" % self.backup_set_directory
         sys.exit()
      else:
         os.makedirs(self.backup_set_full_directory)


   def _load_backup_set(self):
      if not os.path.exists(self.backup_set_directory):
         print "ERROR:  Backup set directory does not exist  '%s'" % self.backup_set_directory
         sys.exit()
      elif not os.path.exists(self.backup_set_full_directory):
         print "ERROR:  Backup set FULL directory does not exist  '%s'" % self.backup_set_full_directory
         sys.exit()
      else:
         print "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW"
         for item in sorted( os.listdir(self.backup_set_directory) ):
            if re.match('^(\d+)$', item):
               backup_dir_path = self.backup_set_directory + '/' + item
               self.incrementals.append(backup_dir_path)
               print "DIR   /   item     '%s'  /  '%s'" % ( self.backup_set_directory, item)
               self.latest_backup = backup_dir_path
         print
         for item in self.incrementals:
            print "backup_dir     '%s'" % item

#############################################################################


   def __float__(self):

      num_out = None

      try:
         float(self.epoch_time)
         num_out = float(self.epoch_time)
      except ValueError:
         try:
            long(self.epoch_time)
            num_out = long(self.epoch_time)
         except ValueError:
            try:
               int(self.epoch_time)
               num_out = int(self.epoch_time)
            except ValueError:
               num_out = None

      return( num_out )


   def __repr__(self):

      return( str(int(round(self.epoch_time))) )


   def __cmp__(self, other):

      if self < other:
         return -1
      elif self > other:
         return 1
      else:
         return 0


   def __lt__(self, other):

      if self < other:
         return True
      else:
         return False


   def __le__(self, other):

      if self <= other:
         return True
      else:
         return False


   def __eq__(self, other):

      if self == other:
         return True
      else:
         return False


   def __ne__(self, other):

      if self != other:
         return True
      else:
         return False


   def __gt__(self, other):

      if self > other:
         return True
      else:
         return False


   def __ge__(self, other):

      if self >= other:
         return True
      else:
         return False


   def __nonzero__(self):

      if self:
         return True
      else:
         return False


   def __add__(self, other):

      return( self + other )


   def __sub__(self, other):

      return( self - other )


   def __mul__(self, other):

      return( self * other )


   def __floordiv__(self, other):

      return( self // other )


   def __mod__(self, other):

      return( self % other )


   def __divmod__(self, a, b):

      return( divmod(a, b) )


   def __iadd__(self, other):

      return( self + other )


   def __isub__(self, other):

      return( self - other )


   def __imul__(self, other):

      return( self * other )


   def __idiv__(self, other):

      return( self / other )


   def __ifloordiv__(self, other):

      return( self // other )


   def __imod__(self, other):

      return( self % other )


   def __neg__(self):

      return( -self )


   def __pos__(self):

      return( +self )


   def __abs__(self):

      return( abs(self) )








class Back_Up():


   def __init__(self, time_input):  # units are struct_time in UTC
      self.struct_time_current_gmt                   = time_input
      self.epoch_time_current                        = calendar.timegm(self.struct_time_current_gmt)  # seconds since the epoch
      self.backup_full                               = ''
      self.backup_status                             = {}
      self.dir_name_base                             = ''
#      self.dir_time_base                             = ''
      self.dir_name                                  = ''
#      self.dir_time                                  = ''
      self.previous_backup                           = []
      self.backup_offset_from_midnight_in_seconds    = self.convert_backup_hour_minute_to_seconds(backup_conf.config['backup_time_of_day'])
      self.seconds_per_day                           = 60 * 60 * 24
      self.backup_times                              = {}
      self.universal_reference_date                  = 1388563200.0   # Arbitrarily selected epoch time ( This translates to date ->  'Wed Jan  1 00:00:00 2014' )
      self.most_recent_scheduled_backup_before_today = None
      self.very_next_scheduled_backup_after_today    = None
      self.te                                        = te.time_extra()


   def create_names(self):

      dow    = time.strftime("%a", self.struct_time_current_gmt)
      month  = time.strftime("%b", self.struct_time_current_gmt)
      dom    = time.strftime("%d", self.struct_time_current_gmt)
      year   = time.strftime("%Y", self.struct_time_current_gmt)
      hour   = time.strftime("%H", self.struct_time_current_gmt)
      minute = time.strftime("%M", self.struct_time_current_gmt)
      second = time.strftime("%S", self.struct_time_current_gmt)
      zone   = time.strftime("%Z", self.struct_time_current_gmt)

      self.dir_name_base = dow + '_' + month + '_' + dom + '_' + year
      self.dir_name = self.dir_name_base + '_' + 'GMT'
      if self.backup_full:
         self.dir_name += '___Full'
      else:
         self.dir_name += '___Incremental'

#      self.dir_time_base = hour + '_' + minute + '_' + second
#      self.dir_time = self.dir_time_base + '_' + 'GMT'
#      if self.backup_full:
#         self.dir_time += '___Full'
#      else:
#         self.dir_time += '___Incremental'


   def convert_backup_hour_minute_to_seconds(self, hh_mm):
      """This returns the number of seconds after midnight at which the
      backup is to occur.  This is just an offset in seconds from midnight.
      This is NOT and epoch seconds number."""

      (hour, minute) = hh_mm.rsplit('_')
      if ( int(hour) < 0 )  or  ( int(hour) > 23 ):
         return None
      if ( int(minute) < 0 )  or  ( int(minute) > 59 ):
         return None

      return( ( int(hour) * 3600 ) + ( int(minute) * 60 ) )


   def convert_date_to_backup_timeofday_in_epoch(self, date_time):
      """Accepts either a struct_time object or epoch seconds.  This returns
      backup time in epoch seconds."""

      epoch_first_of_day = self.te.truncate_any_time_to_first_epoch_of_day(date_time)
      backup_time_for_day_in_epoch = epoch_first_of_day + self.backup_offset_from_midnight_in_seconds
      if self.te.difference_of_days(backup_time_for_day_in_epoch, epoch_first_of_day) != 0:
         backup_time_for_day_in_epoch = self.te.truncate_any_time_to_last_epoch_of_day(epoch_first_of_day)

      return( backup_time_for_day_in_epoch )


   def initialize_backup_report_file(self, run_file, version, date, author ):
      """Initializes file: backup_report___INITIALIZED___.py."""


      program = {
                 'program_name'    : run_file,
                 'program_version' : version,
                 'program_date'    : date,
                 'program_author'  : author
                }


      config_file = '/dir_1/dir_2/some_user_name/backup_report.py',

      config_pretty = 'backup_report___INITIALIZED___.py'
      fh_01 = open(config_pretty, 'w')


      fh_01.write("\n\n")
      fh_01.write('program = ')
      pprint.pprint(program, fh_01, indent=4, width=80)
      fh_01.write("\n\n")
      fh_01.write('config_file = ')
      pprint.pprint(config_file, fh_01, indent=4, width=80)
      fh_01.close()


      # Make the pretty print even 'prettier'
      fh_01 = open(config_pretty, 'r')
      file_contents = fh_01.read()
      new_line_added_00 = re.sub('\{', '{\n ', file_contents) # add new line
      new_line_added_01 = re.sub('\}', '\n}', new_line_added_00)   # add new line
      fh_01.close()


      fh_01 = open(config_pretty, 'w')
      fh_01.write(new_line_added_01)
      fh_01.close()


   def generate_backup_times(self, start_time, frequency, frequency_unit, backup_type_is_full=True):
      """First  Argument:  Either a struct_time object or epoch seconds
         Second Argument:  Positive integer representing the number of time units (days, months, quarters) between backups
         Third  Argument:  Time unit for the previous argument (days, months, quarters)
         Forth  Argument:  True for FULL backup
                           False for incremental backup
                           defaults to True (FULL)

         This populates the 'self.backup_times' dictionary with the backup times
         where the key is the backup time in epoch seconds and the value is
         the backup type, FULL or incremental.
      """

      next_backup_time = self.te.truncate_any_time_to_first_epoch_of_day(start_time)
      if frequency_unit  ==  'days':
         for day in range(-int(2*366/frequency),int(2*366/frequency) ):
            current_backup_time = self.convert_date_to_backup_timeofday_in_epoch(next_backup_time)
            if backup_type_is_full:
               self.backup_times[current_backup_time] = 'FULL'
            elif current_backup_time not in self.backup_times:
               self.backup_times[current_backup_time] = 'incremental'
            next_backup_time = self.te.increment_day_by_n_days(current_backup_time, frequency)
      elif frequency_unit  ==  'months':
         for month in range(-24,24): # add one month margin on top of the year
            current_backup_time = self.convert_date_to_backup_timeofday_in_epoch(next_backup_time)
            if backup_type_is_full:
               self.backup_times[current_backup_time] = 'FULL'
            elif current_backup_time not in self.backup_times:
               self.backup_times[current_backup_time] = 'incremental'

            next_backup_time = self.te.increment_day_by_n_months(current_backup_time, 1)
      elif frequency_unit  ==  'quarters':
         for quarter in range(-8,8): # add one quarter margin on top of the year
            current_backup_time = self.convert_date_to_backup_timeofday_in_epoch(next_backup_time)
            if backup_type_is_full:
               self.backup_times[current_backup_time] = 'FULL'
            elif current_backup_time not in self.backup_times:
               self.backup_times[current_backup_time] = 'incremental'

            next_backup_time = self.te.increment_day_by_n_months(current_backup_time, 3)


   def set_backup_status(self):

      # generate full backup dates
      if   backup_conf.config['full_backup_frequency'][0] == 'daily':

         # Generate times for FULL backups
         self.generate_backup_times(self.struct_time_current_gmt, 1, 'days', True)


      elif backup_conf.config['full_backup_frequency'][0] == 'dow':


         # Generate next available time for a FULL backup
         next_occurrence_of_dow = self.te.increment_day_to_next_occurrence_of_day_of_week( self.struct_time_current_gmt, backup_conf.config['full_backup_frequency'][1] )

         # Generate times for FULL backups
         self.generate_backup_times(next_occurrence_of_dow, 7, 'days', True)

         # Generate times for incremental backups
         if backup_conf.config['incremental_frequency'][0] == 'daily':
            self.generate_backup_times(next_occurrence_of_dow, 1, 'days', False)
         elif backup_conf.config['incremental_frequency'][0] == 'dow':
            day_of_week_local = self.te.increment_day_to_next_occurrence_of_day_of_week( next_occurrence_of_dow, backup_conf.config['incremental_frequency'][1] )
            self.generate_backup_times(day_of_week_local, 7, 'days', False)


      elif backup_conf.config['full_backup_frequency'][0] == 'biweekly':


         # Standardize the biweekly backups so its start week is fully deterministic and set by the user
         offset_from_universal_date_reference = self.te.difference_of_days(self.struct_time_current_gmt, self.universal_reference_date)


         biweekly_start_date_01 = None
         if ( offset_from_universal_date_reference % 14 ) > 6:
            biweekly_start_date_01 = self.te.increment_day_by_n_days(self.struct_time_current_gmt, -7)
         else:
            biweekly_start_date_01 = self.struct_time_current_gmt

         biweekly_start_date_02 = biweekly_start_date_01
         if backup_conf.config['full_backup_frequency'][2]:
            biweekly_start_date_02 = self.te.increment_day_by_n_days(biweekly_start_date_01, -7)




         # Generate next available time for a FULL backup
         next_occurrence_of_dow = self.te.increment_day_to_next_occurrence_of_day_of_week( biweekly_start_date_02, backup_conf.config['full_backup_frequency'][1] )

         # Generate times for FULL backups
         self.generate_backup_times(next_occurrence_of_dow, 14, 'days', True)


         # Generate times for incremental backups
         if backup_conf.config['incremental_frequency'][0] == 'daily':
            self.generate_backup_times(next_occurrence_of_dow, 1, 'days', False)
         elif backup_conf.config['incremental_frequency'][0] == 'dow':
            day_of_week_local = self.te.increment_day_to_next_occurrence_of_day_of_week( next_occurrence_of_dow, backup_conf.config['incremental_frequency'][1] )
            self.generate_backup_times(day_of_week_local, 7, 'days', False)
         elif backup_conf.config['incremental_frequency'][0] == 'biweekly':
            week_offset = self.te.increment_day_by_n_days(next_occurrence_of_dow, 7)
            self.generate_backup_times(week_offset, 14, 'days', False)


      elif backup_conf.config['full_backup_frequency'][0] == 'dom':

         # Generate next available time for a FULL backup
         next_monthly_occurrence = None
         if backup_conf.config['full_backup_frequency'][1] >= 28: # backups are at the end of the month
            next_monthly_occurrence = self.te.get_last_day_of_month(self.struct_time_current_gmt)
         else:
            if backup_conf.config['full_backup_frequency'][1] >= self.te.get_day_of_month(self.struct_time_current_gmt):
               next_monthly_occurrence = self.te.get_day_of_current_month(self.struct_time_current_gmt, backup_conf.config['full_backup_frequency'][1])
            else:
               a_day_in_next_month = self.te.increment_day_by_n_months(self.struct_time_current_gmt, 1)
               next_monthly_occurrence = self.te.get_day_of_current_month(a_day_in_next_month, backup_conf.config['full_backup_frequency'][1])
         self.generate_backup_times(next_monthly_occurrence, 1, 'months', True)



         # Generate times for incremental backups
         if backup_conf.config['incremental_frequency'][0] == 'daily':
            self.generate_backup_times(next_monthly_occurrence, 1, 'days', False)

         elif backup_conf.config['incremental_frequency'][0] == 'dow':

            # Generate next available time for an incremental backup
            next_occurrence_of_dow = self.te.increment_day_to_next_occurrence_of_day_of_week( self.struct_time_current_gmt, backup_conf.config['incremental_frequency'][1] )
            self.generate_backup_times(next_occurrence_of_dow, 7, 'days', False)

         elif backup_conf.config['incremental_frequency'][0] == 'biweekly':

            # Generate next available time for an incremental backup
            next_occurrence_of_dow = self.te.increment_day_to_next_occurrence_of_day_of_week( self.struct_time_current_gmt, backup_conf.config['incremental_frequency'][1] )
            self.generate_backup_times(next_occurrence_of_dow, 14, 'days', False)

         elif backup_conf.config['incremental_frequency'][0] == 'dom':

            # Generate next available time for an incremental backup
            half_the_number_of_days_in_a_month = 15

            half_month_offset = self.te.increment_day_by_n_days(next_monthly_occurrence, half_the_number_of_days_in_a_month)

            self.generate_backup_times(half_month_offset, 1, 'months', False)


      elif backup_conf.config['full_backup_frequency'][0] == 'quarterly':

         # Generate next available time for a FULL backup
         next_quarterly_occurrence = None

         quarter_first_day = self.te.get_first_day_of_quarter(self.struct_time_current_gmt)
         quarter_last_day  = self.te.get_last_day_of_quarter(self.struct_time_current_gmt)

         if ( self.te.difference_of_days(quarter_first_day, self.struct_time_current_gmt) == 0 )  and  (backup_conf.config['full_backup_frequency'][1] == 'first'):
            next_quarterly_occurrence = self.struct_time_current_gmt
         elif ( self.te.difference_of_days(quarter_last_day, self.struct_time_current_gmt) == 0 )  and  (backup_conf.config['full_backup_frequency'][1] == 'last'):
            next_quarterly_occurrence = self.struct_time_current_gmt
         elif backup_conf.config['full_backup_frequency'][1] == 'last':
            next_quarterly_occurrence = quarter_last_day
         else:
            next_quarterly_occurrence = self.te.increment_day_by_n_days(quarter_last_day, 1)

         self.generate_backup_times(next_quarterly_occurrence, 1, 'quarters', True)





         # Generate times for incremental backups
         if backup_conf.config['incremental_frequency'][0] == 'daily':
            self.generate_backup_times(next_quarterly_occurrence, 1, 'days', False)

         elif backup_conf.config['incremental_frequency'][0] == 'dow':

            # Generate next available time for an incremental backup
            next_occurrence_of_dow = self.te.increment_day_to_next_occurrence_of_day_of_week( self.struct_time_current_gmt, backup_conf.config['incremental_frequency'][1] )
            self.generate_backup_times(next_occurrence_of_dow, 7, 'days', False)

         elif backup_conf.config['incremental_frequency'][0] == 'biweekly':

            # Generate next available time for an incremental backup
            next_occurrence_of_dow = self.te.increment_day_to_next_occurrence_of_day_of_week( self.struct_time_current_gmt, backup_conf.config['incremental_frequency'][1] )
            self.generate_backup_times(next_occurrence_of_dow, 14, 'days', False)

         elif backup_conf.config['incremental_frequency'][0] == 'dom':

            next_monthly_occurrence = None

            first_monthly_increment_day = self.te.get_day_of_current_month(quarter_first_day, backup_conf.config['incremental_frequency'][1])
            if first_monthly_increment_day:
               next_monthly_occurrence = first_monthly_increment_day
            else:
               next_monthly_occurrence = self.te.get_last_day_of_month(quarter_first_day)

            self.generate_backup_times(next_monthly_occurrence, 1, 'months', False)


      print
      print
      for epoch_time in sorted( self.backup_times ):
#         if self.backup_times[epoch_time] == 'FULL':
#            print "  %s   %s   %s" % ( time.asctime(time.gmtime(epoch_time)), self.backup_times[epoch_time], epoch_time )
#         else:
#            print "  %s       %s   %s" % ( time.asctime(time.gmtime(epoch_time)), self.backup_times[epoch_time], epoch_time )

         if epoch_time  <  self.te.date_to_epoch(self.struct_time_current_gmt):
#            print " Earlier     '%s'   '%s'" % ( epoch_time, self.te.date_to_epoch(self.struct_time_current_gmt) )
            self.most_recent_scheduled_backup_before_today  = ( epoch_time, self.backup_times[epoch_time] )
         if epoch_time  >  self.te.date_to_epoch(self.struct_time_current_gmt):
            if not self.very_next_scheduled_backup_after_today:
#               print " later       '%s'   '%s'" % ( epoch_time, self.te.date_to_epoch(self.struct_time_current_gmt) )
               self.very_next_scheduled_backup_after_today   = ( epoch_time, self.backup_times[epoch_time] )
      print


#      print " Earlier     '%s'" % ( self.most_recent_scheduled_backup_before_today[0] )
#      print " later       '%s'" % ( self.very_next_scheduled_backup_after_today  )



      if backup_conf.config['enable_backups']:
         backup_status_file = backup_conf.config['base_directory'] + '/backup_status.txt'
         if os.path.exists(backup_status_file):
            fh_02 = open(backup_status_file, "r")
            status = fh_02.readlines()
            for entry in status:
               entry = entry.strip() # eliminate leading/trailing whitespace
               entry = re.sub(' +', ' ', entry) # reduce consecutive spaces to a single space
               split_in_two = entry.rsplit(' ')
               split_in_two[1] = re.sub('_+', '_', split_in_two[1]) # reduce consecutive '_' to a single '_'
               xxxxx = split_in_two[1].rsplit('_')
               self.previous_backup.append(xxxxx)
               fh_02.close()




         else:
            self.backup_status['prev_backup_type_is_full'] = True
            self.backup_status['prev_backup_date']         = ''
#            self.backup_full   = True



   def set_backup_type(self, backup_full=True):
      if backup_full:
         self.backup_full = True
      else:
         self.backup_full = False
      self.create_names()
      return( True )


   def get_dir_name(self):
      return( self.dir_name )


#   def get_backup_hhmmss(self):
#      return( self.dir_time )


   def is_backup_scheduled_now(self):

      all_existing_backups = {}

      print
      most_recent_backup = None
      reference_backup_dir = backup_conf.config['base_directory'] + '/' + backup_conf.config['backup_location_reference']
      backup_sets        = []
      backup_dirs_in_set = []
      latest_backup_set  = ''
      latest_backup      = ''
      for epoch_dir in sorted( os.listdir(reference_backup_dir) ):
         if re.match('^(\d+)$', epoch_dir):
            backup_sets.append(epoch_dir)
            backup_dir = reference_backup_dir + '/' + epoch_dir
            backup_dirs_in_set = []
            if len(backup_dirs_in_set) != 0:
               print " list has not been successfully emptied for backup set '%s'" % epoch_dir
               sys.exit()
            for backup_instance in sorted( os.listdir(backup_dir) ):
               if re.match('^(\d+)$', backup_instance):
                  backup_dirs_in_set.append(backup_instance)


                  all_existing_backups[backup_instance] = ''
                  latest_backup      = backup_instance
#                  print "Existing Backup    '%s'    '%s'    '%s'" % ( epoch, backup_type, self.te.date_to_datestring(epoch) )


            # No backups found in backup set
            if len(backup_dirs_in_set)  ==  0:
               print "ERROR:  No backup epoch directories found in backup set '%s'" % epoch_dir
            else:
               # No backups found in backup set
               if backup_dirs_in_set[0]  !=  epoch_dir:
                  print "ERROR:  There is no matching epoch dir in the lower dir for the epoch dir of the backup set '%s'" % epoch_dir
               else:
                  latest_backup_set = int(epoch_dir)


      # Return value field descriptions
#     return( do_backup_now, backup_type, backup_set_epoch, backup_epoch, backup_set_does_exist )
#                |                 |            |                |                |
#                |                 |            |                |                |
#                |                 |            |                |                |
#                |                 |            |                |               True - > backup set specified in this list currently exists
#                |                 |            |                |               False -> backup set specified in this list currently does NOT exist
#                |                 |            |                |
#                |                 |            |               Epoch time for full/incremental backup within this backup set
#                |                 |            |
#                |                 |           Epoch time for backup set
#                |                 |
#                |                Backup type, 'FULL' or 'incremental'
#                |
#               True  -> backup schedule call for backup to be done now
#               False -> backup schedule call for backup to NOT be done now



      # No backup sets found
      if len(backup_sets)  ==  0:
         print "ERROR:  No backup epoch directories found in backup set '%s'" % latest_backup_set
         return( True, 'FULL', self.epoch_time_current, self.epoch_time_current, False )
      else:
#         if str(int(round(self.most_recent_scheduled_backup_before_today[0])))  not in  all_existing_backups:
         if str(int(round(self.most_recent_scheduled_backup_before_today[0])))  >  latest_backup:
#            print "Backup is to be done.  present / backup   '%s' / '%s'    '%s'    '%s'" % ( self.te.date_to_datestring(self.struct_time_current_gmt), self.te.date_to_datestring(self.most_recent_scheduled_backup_before_today[0]), self.te.date_to_epoch(self.most_recent_scheduled_backup_before_today[0]), int(round(self.most_recent_scheduled_backup_before_today[0])) )
            return( True, self.most_recent_scheduled_backup_before_today[1], latest_backup_set, self.most_recent_scheduled_backup_before_today[0], True )
         else:
            return( False, self.most_recent_scheduled_backup_before_today[1], latest_backup_set, self.most_recent_scheduled_backup_before_today[0], True )








#*****************************************************************************

def UniversalDiff(obj_1, obj_2):


   # Determine File Types
   (xxxx_1, yyyy_1) = mimetypes.guess_type(obj_1)
   (xxxx_2, yyyy_2) = mimetypes.guess_type(obj_2)

   if (xxxx_1 != xxxx_2)  or  (yyyy_1 != yyyy_2):
      return(False)

   if os.path.islink(obj_1)  and  (not os.path.islink(obj_2) ):
         return( False )
   elif ( not os.path.islink(obj_1) )  and  os.path.islink(obj_2):
         return( False )


   if os.path.islink(obj_1)  and  os.path.islink(obj_2):
      if os.path.abspath(obj_1)  !=  os.path.abspath(obj_2):
         return( False )

      if os.path.isfile(obj_1)  and  ( not os.path.isfile(obj_2) ):
         return( False )
      elif os.path.isdir(obj_1)  and  ( not os.path.isdir(obj_2) ):
         return( False )
      elif ( not os.path.isfile(obj_1) )  and  ( not os.path.isdir(obj_1) ):
         if os.path.isfile(obj_2)  or  os.path.isdir(obj_2):
            return( False )

   elif os.path.isfile(obj_1)  and  os.path.isfile(obj_2):



      if ( os.path.getsize(obj_1)  !=  0 )  or  ( os.path.getsize(obj_2)  !=  0 ):


         if is_pair_of_tar_files(obj_1, obj_2):
            if not walk_tar_file(obj_1, obj_2):
               return( False )
         else:
            if not filecmp.cmp(obj_1, obj_2):
               return( False )
   elif os.path.isdir(obj_1)  and  os.path.isdir(obj_2):
      all_files_1 = []
      for root_1, dirs_1, files_1 in os.walk(obj_1):
         for name_1 in files_1:
            file_name_1 = os.path.join(root_1, name_1)
            all_files_1.append(file_name_1)

      all_files_2 = []
      for root_2, dirs_2, files_2 in os.walk(obj_2):
         for name_2 in files_2:
            file_name_2 = os.path.join(root_2, name_2)
            all_files_2.append(file_name_2)

      if len(all_files_1)  !=  len(all_files_2):
         print "DIFFERENT_000   directory walk sizes are different"
         return( False )

      for ii_00 in range(0,len(all_files_1) ):
         if is_pair_of_tar_files(all_files_1[ii_00], all_files_2[ii_00]):
            if not walk_tar_file(all_files_1[ii_00], all_files_2[ii_00]):
               return( False )
         else:
            if not UniversalDiff(all_files_1[ii_00], all_files_2[ii_00]):
               return( False )
   else:
      print "\n\nCurrent directory is '%s'" % os.getcwd()
#      if os.path.exists(obj_1):
#         print "File '%s' does exist" % (obj_1)
#      else:
#         print "File '%s' does NOT exist" % (obj_1)
#      if os.path.exists(obj_2):
#         print "File '%s' does exist" % (obj_2)
#      else:
#         print "File '%s' does NOT exist" % (obj_2)
      print "\n\n  Thing_1 / Thing_2   '%s'  /  '%s'\n\n" % (type(obj_1), type(obj_2) )
      print "MARKER_000   '%s'   '%s'\n" %  ( obj_1, obj_2 )

      print "The two inputs are expected to be a pair of existing files, directories or links"
      return( False )

   return( True )

#*****************************************************************************

def is_pair_of_tar_files(obj_1, obj_2):

   # Determine File Types
   (xxxx_1, yyyy_1) = mimetypes.guess_type(obj_1)
   (xxxx_2, yyyy_2) = mimetypes.guess_type(obj_2)

   if ( xxxx_1  !=  xxxx_2 )  or  ( yyyy_1  !=  yyyy_2 ):
      return(False)

   if (xxxx_1 == 'application/x-tar')  and  (xxxx_2 == 'application/x-tar'):
      return(True)
   else:
      return(False)

#*****************************************************************************

def walk_tar_file(obj_1, obj_2):


   # Determine File Types
   (xxxx_1, yyyy_1) = mimetypes.guess_type(obj_1)
   (xxxx_2, yyyy_2) = mimetypes.guess_type(obj_2)

   if ( xxxx_1  !=  xxxx_2 )  or  ( yyyy_1  !=  yyyy_2 ):
      return(False)

   if ( not tarfile.is_tarfile(obj_1) )  or  ( not tarfile.is_tarfile(obj_2) ):
      return(False)

   tar_1 = tarfile.open(name=obj_1, mode='r',)
   tar_2 = tarfile.open(name=obj_2, mode='r',)


   tar_files_1 = tar_1.getnames()
   tar_files_2 = tar_2.getnames()

   if len(tar_files_1)  !=  len(tar_files_2):
      print "DIFFERENT_000   tar extracted lists have different numbers of files"
      return( False )


   for ii_00 in range(0,len(tar_files_2) ):
      if is_pair_of_tar_files(tar_files_1[ii_00], tar_files_2[ii_00]):
         if not walk_tar_file(tar_files_1[ii_00], tar_files_2[ii_00]):
            return( False )
      else:
         if not UniversalDiff(tar_files_1[ii_00], tar_files_2[ii_00]):
            return( False )

   return( True )

#*****************************************************************************

