

import os
import tarfile




class tarfile_support():


   def create_gziped_tar_file(self, file_name, file_list, file_modification_filter):
      """Accepts a file name.  A second file is created with a '.tar.gz'
      file extension.  If the 'file_modification_filter' is a valid epoch
      time, then only files having a modification time greater than or equal
      to that time are tar'ed.  If 'file_modification_filter' is anything
      else, then all files are tar'ed."""

      number_of_tar_items = len(file_list)
      tar_backup = tarfile.open(name=file_name, mode='w:gz',)
      item_cnt = 0
      for item in file_list:
         item_cnt += 1

         # Either a FULL backup or an incremental backup where the file modification date is greater than or equal to the epoch input argument
         if (   file_modification_filter.__class__.__name__ != 'float' )  or  ( ( file_modification_filter.__class__.__name__ == 'float' )  and  ( os.path.getmtime(item)  >=  file_modification_filter ) ):

            if item  ==  os.path.abspath(item):
               print  "ERROR: path must not be an absolute full path  '%s'" % item
               return( False )
            elif not item  ==  os.path.normpath(item):
               print  "ERROR: path is not minimally collapsed  '%s'" % item
               return( False )
            elif  os.path.ismount(item):
               print  "ERROR: path is a mount point  '%s'" % item
               return( False )
            elif  ( not os.path.islink(item) )  and  ( not os.path.isfile(item) )  and  ( not os.path.isdir(item) ):
               print  "Path is neither a FILE, DIRECTORY nor LINK  '%s'" % item
            elif  ( os.path.islink(item) )  and  ( not os.path.isfile(item) )  and  ( not os.path.isdir(item) ):
               print  "Path link goes nowhere  '%s'" % item
            else:
               tar_backup.add(item)

      tar_backup.close()

      if item_cnt == number_of_tar_items:
         return( True )
      else:
         print  "ERROR: Not all items from list were successfully tar'ed"
         return( False )


   def is_number(self, string_in):
      try:
         float(string_in) # for int, long and float
      except ValueError:
         return False

      return True

