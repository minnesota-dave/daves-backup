

import time
import calendar




class time_extra():


   def __init__(self):
      self.seconds_per_day  = 60 * 60 * 24


   def truncate_any_time_to_first_epoch_of_day(self, date_time):
      """Accepts either a struct_time object or epoch seconds.  It returns the
      very first epoch time (seconds) of the corresponding calendar day."""

      day_xx = date_time
      if day_xx.__class__.__name__  !=  'struct_time':
         day_xx = time.gmtime(date_time)

      month  = time.strftime("%b", day_xx)
      dom    = time.strftime("%d", day_xx)
      year   = time.strftime("%Y", day_xx)
      start_of_day = time.strptime(dom + ' ' + month + ' ' + year, "%d %b %Y")
      first_epoch_of_day = calendar.timegm(start_of_day)
      return( first_epoch_of_day )


   def truncate_any_time_to_last_epoch_of_day(self, date_time):
      """Accepts either a struct_time object or epoch seconds.  It returns the
      very last epoch time (seconds) of the corresponding calendar day."""

      epoch = self.truncate_any_time_to_first_epoch_of_day(date_time)
      epoch_in_middle_of_next_day = epoch + self.seconds_per_day * 1.5 # Next day plus half day for margin
      first_epoch_of_next_day = self.truncate_any_time_to_first_epoch_of_day(epoch_in_middle_of_next_day)
      last_epoch_of_day = first_epoch_of_next_day - 1

      return( last_epoch_of_day )


   def difference_of_days(self, date_time_1, date_time_2):
      """Accepts either a struct_time object or epoch seconds for either argument.
      The first argument can be in epoch seconds and the second can be a struct_time
      object.  It returns the integer in days of 'date_time_1 - date_time_2'.  If date_time_2
      is greater than date_time_1, then a negative integer will be returned.  If both
      arguments are different epoch seconds but both occur in the same day, then
      zero will be returned."""

      epoch_1 = self.truncate_any_time_to_first_epoch_of_day(date_time_1)
      epoch_2 = self.truncate_any_time_to_first_epoch_of_day(date_time_2)

      epoch_diff = 0
      if epoch_1 > epoch_2:
         epoch_diff = int( ( epoch_1 + (self.seconds_per_day/2) - epoch_2 ) / self.seconds_per_day )
      elif epoch_2 > epoch_1:
         epoch_diff = -1 * int( ( epoch_2 + (self.seconds_per_day/2) - epoch_1 ) / self.seconds_per_day )

      return( epoch_diff )


   def get_day_of_month(self, date_time):
      """Accepts either a struct_time object or epoch seconds.  It returns
      the integer day of month, 1-31."""

      day_xx = date_time
      if day_xx.__class__.__name__  !=  'struct_time':
         day_xx = time.gmtime(date_time)

      return( time.strftime("%d", day_xx) )


   def get_month(self, date_time, format_is_decimal=True):
      """Accepts either a struct_time object or epoch seconds.  It returns
      either as a decimal (1-12) or a three character abbreviations
      (Jan, Feb, etc.)."""

      day_xx = date_time
      if day_xx.__class__.__name__  !=  'struct_time':
         day_xx = time.gmtime(date_time)

      if format_is_decimal:
         return( time.strftime("%m", day_xx) )
      else:
         return( time.strftime("%b", day_xx) )


   def get_year(self, date_time):
      """Accepts either a struct_time object or epoch seconds.  It returns
      the full decimal year (2011, 2014, etc.)."""

      day_xx = date_time
      if day_xx.__class__.__name__  !=  'struct_time':
         day_xx = time.gmtime(date_time)

      return( time.strftime("%Y", day_xx) )


   def difference_of_months(self, date_time_1, date_time_2):
      """Accepts either a struct_time object or epoch seconds for either
      argument.  The first argument can be in epoch seconds and the second
      can be a struct_time object.  It returns the integer in months of
      'date_time_1 - date_time_2'.  If the month containing date_time_2 is
      greater than the month containing date_time_1, then a negative integer
      will be returned.  If both arguments are different epoch seconds but
      both occur in the same month, then zero will be returned."""

      month_1 = int( self.get_month(date_time_1) )
      month_2 = int( self.get_month(date_time_2) )

      year_1 = int( self.get_year(date_time_1) )
      year_2 = int( self.get_year(date_time_2) )

      return( ( ( year_1 - year_2 ) * 12 )  +  ( month_1 - month_2 ) )


   def get_the_integer_last_day_of_month(self, date_time):
      """Accepts either a struct_time object or epoch seconds.  It returns
      the integer last day of month."""

      day_xx = date_time
      if day_xx.__class__.__name__  !=  'struct_time':
         day_xx = time.gmtime(date_time)

      month  = time.strftime("%b", day_xx)
      year   = time.strftime("%Y", day_xx)

      last_day_of_month = None
      for day_num in range(28,32):

         try:
            start_of_day = time.strptime( str(day_num) + ' ' + month + ' ' + year, "%d %b %Y")
            last_day_of_month = day_num
         except IOError:
            last_day_of_month = day_num - 1
            break
         except ValueError:
            last_day_of_month = day_num - 1
            break
         except ImportError:
            last_day_of_month = day_num - 1
            break
         except EOFError:
            last_day_of_month = day_num - 1
            break
         except KeyboardInterrupt:
            last_day_of_month = day_num - 1
            break
         except:
            last_day_of_month = day_num - 1
            break

      return( last_day_of_month )


   def increment_day_to_next_occurrence_of_day_of_week(self, date_time, dow):
      """Accepts either a struct_time object or epoch seconds.  It returns the
      the time in the appropriate format of the next available corresponding
      calendar day."""

      if len(dow) == 0:
         print "No day_of_week given, one of 'Mon', Tue, etc. expected."
         return( None )

      days_of_week = {
                      'Sun' : True,
                      'Mon' : True,
                      'Tue' : True,
                      'Wed' : True,
                      'Thu' : True,
                      'Fri' : True,
                      'Sat' : True
                     }

      days_of_week_numeric = {
                      '0' : True,
                      '1' : True,
                      '2' : True,
                      '3' : True,
                      '4' : True,
                      '5' : True,
                      '6' : True
                     }

      # If dow entered as integer, convert it to string
      dow_i = None
      if dow not in days_of_week:
         dow_i = str( int(dow) )
      else:
         dow_i = dow


      if ( dow_i not in days_of_week )  and  ( dow_i not in days_of_week_numeric ):
         print "Incorrect argument given for day_of_week, one of 'Mon', Tue, etc. expected   '%s'" % dow_i
         return( None )

      next_epoch = self.truncate_any_time_to_first_epoch_of_day(date_time)
      count_offset_in_days = 0
      for day_cnt in range(0,7):
         if ( dow_i == time.strftime("%a", time.gmtime(next_epoch)) )  or  ( dow_i == time.strftime("%w", time.gmtime(next_epoch)) ):
            break
         epoch_increment_by_day = self.increment_day_by_n_days(next_epoch, 1)
         next_epoch = epoch_increment_by_day
         count_offset_in_days += 1

      return( self.increment_day_by_n_days(date_time, count_offset_in_days) )


   def normalize_date_format(self, date_time_in, date_time_reference):
      """TBD"""

      day_input_format = 'struct_time'
      if date_time_in.__class__.__name__  !=  'struct_time':
         day_input_format = 'epoch'

      day_ref_format = 'struct_time'
      if date_time_reference.__class__.__name__  !=  'struct_time':
         day_ref_format = 'epoch'


      formatted_date = None
      if day_input_format  ==  day_ref_format:
         formatted_date = date_time_in
      elif day_ref_format  ==  'struct_time':
         formatted_date = time.gmtime(date_time_in)
      else:
         formatted_date = calendar.timegm(date_time_in)

      return( formatted_date )


   def set_date_timeofday_to_reference(self, date_time_in, date_time_reference):
      """This only adjusts the time_of_day of date_time_in.  It does NOT
      change its format.  If it comes in as epoch, it goes out, time
      adjusted, as epoch."""

      first_epoch_of_day     = self.truncate_any_time_to_first_epoch_of_day(date_time_in)
      first_epoch_of_day_ref = self.truncate_any_time_to_first_epoch_of_day(date_time_reference)

      epoch_delta = None
      if date_time_reference.__class__.__name__  !=  'struct_time':
         epoch_delta = date_time_reference - first_epoch_of_day_ref
      else:
         epoch_delta = calendar.timegm(date_time_reference) - first_epoch_of_day_ref

      new_day_epoch_00 = first_epoch_of_day + epoch_delta
      if self.difference_of_days( new_day_epoch_00, first_epoch_of_day)  !=  0:
         new_day_epoch_00 = self.truncate_any_time_to_last_epoch_of_day( first_epoch_of_day )

      new_day_epoch = self.normalize_date_format(new_day_epoch_00, date_time_in)

      return( new_day_epoch )


   def increment_day_by_n_days(self, date_time, num_days):
      """Accepts either a struct_time object or epoch seconds for the first
      argument and an integer for the second.  This works for integers
      positive, negative and even zero for which there is of course no affect.
      If the argument is a struct_time object, then epoch seconds is returned
      for the nth day where the epoch seconds is the very first epoch time for
      that day.  If the argument given is epoch seconds, then an epoch seconds
      is returned where the time of day is the same as the incoming argument."""

      epoch_first_of_day = self.truncate_any_time_to_first_epoch_of_day(date_time)
      epoch_offset = epoch_first_of_day + self.seconds_per_day * (num_days + 0.5) # Add half day for margin in case of leap seconds at the transition at day-to-day boundaries
      new_epoch_first_of_day = self.truncate_any_time_to_first_epoch_of_day(epoch_offset)

      new_epoch_01 = self.set_date_timeofday_to_reference(new_epoch_first_of_day, date_time)
      new_epoch = self.normalize_date_format(new_epoch_01, date_time)

      return( new_epoch )


   def increment_day_by_n_months(self, date_time, num_months):
      """Accepts either a struct_time object or epoch seconds for the first
      argument and an integer for the second.  This works for integers
      positive, negative and even zero for which there is of course no affect.
      If the argument is a struct_time object, then epoch seconds is returned
      for the nth day where the epoch seconds is the very first epoch time for
      that day.  If the argument given is epoch seconds, then an epoch seconds
      is returned where the time of day is the same as the incoming argument."""


      num_years            =  num_months / 12
      if ( num_months < 0 ):
         num_years += 1
         if  (abs(num_months) % 12  ==  0):
            num_years -= 1
      num_months_remainder = abs(num_months) % 12
      if num_months < 0:
         num_months_remainder *= -1

      day_xx = date_time
      if day_xx.__class__.__name__  !=  'struct_time':
         day_xx = time.gmtime(date_time)

      month_start  = time.strftime("%m", day_xx)
      dom_start    = time.strftime("%d", day_xx)
      year_start   = time.strftime("%Y", day_xx)


      start_day_is_last_day_of_month = False
      if int(dom_start)  ==  self.get_the_integer_last_day_of_month(date_time):
         start_day_is_last_day_of_month = True


      dom_end    = int(dom_start)
      year_end   = int(year_start) + num_years
      month_end  = int(month_start) + num_months_remainder
      if month_end > 12:
         year_end += 1
         month_end -= 12
      elif month_end < 1:
         year_end -= 1
         month_end += 12

      # Get any epoch for the month.  To assure this epoch is
      # valid, the first day of the month is chosen.
      start_of_day_end = time.strptime('01' + ' ' + str(month_end) + ' ' + str(year_end), "%d %m %Y")


      last_day_of_month_end = self.get_the_integer_last_day_of_month(start_of_day_end)
      dom_end_01 = dom_end
      if int(dom_end)  >  last_day_of_month_end:
         dom_end_01 = str(last_day_of_month_end)
      if start_day_is_last_day_of_month:
         dom_end_01 = str(last_day_of_month_end)


      start_of_day_end_01 = time.strptime(str(dom_end_01) + ' ' + str(month_end) + ' ' + str(year_end), "%d %m %Y")


      new_data_time_final_00 = self.set_date_timeofday_to_reference(start_of_day_end_01, date_time)
      new_data_time_final = self.normalize_date_format(new_data_time_final_00, date_time)


      return( new_data_time_final )


   def get_last_day_of_month(self, date_time):
      """Accepts either a struct_time object or epoch seconds.  It returns
      the last day of month in the same format as the incoming argument."""

      day_xx = date_time
      if day_xx.__class__.__name__  !=  'struct_time':
         day_xx = time.gmtime(date_time)

      month  = time.strftime("%b", day_xx)
      year   = time.strftime("%Y", day_xx)

      dom = str( self.get_the_integer_last_day_of_month(date_time) )

      start_of_day_last_day_of_month = time.strptime(dom + ' ' + month + ' ' + year, "%d %b %Y")


      last_day_of_month_epoch = self.set_date_timeofday_to_reference(start_of_day_last_day_of_month, date_time)
      first_day_of_month_final = self.normalize_date_format(last_day_of_month_epoch, date_time)

      return( first_day_of_month_final )


   def get_day_of_current_month(self, date_time, dom):
      """
      First Argument:  Accepts either a struct_time object or epoch seconds.
      Second Argument: Integer day of month specified by user
      It returns the user specified day of month in the same format as the
      incoming date_time."""


      # DOM requested for this month exceeds the number of days in month.
      if dom > self.get_the_integer_last_day_of_month(date_time):
         return( None )


      day_xx = date_time
      if day_xx.__class__.__name__  !=  'struct_time':
         day_xx = time.gmtime(date_time)

      month  = time.strftime("%m", day_xx)
      year   = time.strftime("%Y", day_xx)
      start_of_day = time.strptime(str(dom) + ' ' + month + ' ' + year, "%d %m %Y")


      current_day_00 = self.set_date_timeofday_to_reference(start_of_day, date_time)
      current_day = self.normalize_date_format(current_day_00, date_time)

      return( current_day )


   def get_first_day_of_month(self, date_time):
      """Accepts either a struct_time object or epoch seconds.  It returns
      the first day of month in the same format as the incoming date_time."""


      day_in_previous_month = self.increment_day_by_n_months(date_time, -1)

      last_day_of_previous_month = self.get_the_integer_last_day_of_month(day_in_previous_month)


      day_xx = day_in_previous_month
      if day_xx.__class__.__name__  !=  'struct_time':
         day_xx = time.gmtime(day_in_previous_month)

      month  = time.strftime("%m", day_xx)
      dom    = time.strftime("%d", day_xx)
      year   = time.strftime("%Y", day_xx)
      start_of_day = time.strptime(str(last_day_of_previous_month) + ' ' + month + ' ' + year, "%d %m %Y")
      first_epoch_of_day_on_last_day_of_month = calendar.timegm(start_of_day)


      first_day_of_month = self.increment_day_by_n_days(first_epoch_of_day_on_last_day_of_month, 1)

      first_day_of_month_01 = self.set_date_timeofday_to_reference(first_day_of_month, date_time)
      first_day_of_month_final = self.normalize_date_format(first_day_of_month_01, date_time)

      return( first_day_of_month_final )


   def date_to_epoch(self, date_time):
      """Accepts either a struct_time object or epoch seconds.  It returns
      the date as an integer epoch time."""

      epoch_out = date_time
      if date_time.__class__.__name__  ==  'struct_time':
         epoch_out = calendar.timegm(date_time)

      return( epoch_out )


   def date_to_struct_time(self, date_time):
      """Accepts either a struct_time object or epoch seconds.  It returns
      the date as a struct_time object."""

      struct_time_out = date_time
      if date_time.__class__.__name__  !=  'struct_time':
         struct_time_out = time.gmtime(float(date_time))

      return( struct_time_out )


   def date_to_datestring(self, date_time):
      """Accepts either a struct_time object or epoch seconds.  It returns
      the date as a string in format from time.asctime(),
      (Mon Sep 30 00:12:52 2013)."""

      date_string_out = None
      if date_time.__class__.__name__  ==  'struct_time':
         date_string_out = time.asctime(time.gmtime(calendar.timegm(date_time)))
      else:
         date_string_out = time.asctime(time.gmtime(float(date_time)))

      return( date_string_out )


   def get_first_day_of_quarter(self, date_time):
      """Accepts either a struct_time object or epoch seconds.  It returns
      the first day of the calendar quarter in the same format as the
      incoming date_time."""


      current_month = int( self.get_month(date_time) )
      first_day_of_quarter_00 = None
      if ( current_month % 3 )  ==  1:
         first_day_of_quarter_00 = self.get_first_day_of_month(date_time)

      elif ( current_month % 3 )  ==  2:
         previous_month = self.increment_day_by_n_months(date_time, -1)
         first_day_of_quarter_00 = self.get_first_day_of_month(previous_month)

      else:
         current_month_minus_two_months = self.increment_day_by_n_months(date_time, -2)
         first_day_of_quarter_00 = self.get_first_day_of_month(current_month_minus_two_months)


      first_day_of_quarter_01 = self.set_date_timeofday_to_reference(first_day_of_quarter_00, date_time)
      first_day_of_quarter = self.normalize_date_format(first_day_of_quarter_01, date_time)

      return( first_day_of_quarter )


   def get_last_day_of_quarter(self, date_time):
      """Accepts either a struct_time object or epoch seconds.  It returns
      the last day of the calendar quarter in the same format as the
      incoming date_time."""

      first_day_of_quarter = self.get_first_day_of_quarter(date_time)
      advance_two_months = self.increment_day_by_n_months(first_day_of_quarter, 2)
      last_day_of_quarter_00 = self.get_last_day_of_month(advance_two_months)


      last_day_of_quarter_01 = self.set_date_timeofday_to_reference(last_day_of_quarter_00, date_time)
      last_day_of_quarter = self.normalize_date_format(last_day_of_quarter_01, date_time)


      return( last_day_of_quarter )


