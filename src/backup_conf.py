


config = {









'program' : {
            'program_name'    : 'backup.py',
            'program_author'  : 'David McAllister',
            'program_version' : '1.0',
            'program_date'    : 'some_date'
          },




'backup_sets' : {
            1378973400 : {
                          'type'        : 'FULL',
                          'result'      : 'good',
                          'atomic'      : 'yes',
                          'backup_time' : 'Sun Sep 22 08:35:49 PDT 2013',
                          'file_path'   : 'local_backup/1378973400/1378973400/1378973400.tar.gz.gpg',
                          'sha1'        : '11f91948c0e8d60fdb0b7ebdbfb4aee106d945af'
                         },

            1379232600 : {
                          'type'        : 'incremental',
                          'result'      : 'good',
                          'atomic'      : 'yes',
                          'backup_time' : 'Sun Sep 22 08:35:49 PDT 2013',
                          'file_path'   : 'local_backup/1378973400/1379232600/1379232600.tar.gz.gpg',
                          'sha1'        : '11f91948c0e8d60fdb0b7ebdbfb4aee106d945af'
                         },

            1379837400 : {
                          'type'        : 'incremental',
                          'result'      : 'good',
                          'atomic'      : 'yes',
                          'backup_time' : 'Sun Sep 22 08:35:49 PDT 2013',
                          'file_path'   : 'local_backup/1378973400/1379837400/1379837400.tar.gz.gpg',
                          'sha1'        : '11f91948c0e8d60fdb0b7ebdbfb4aee106d945af'
                         },
          },


















   #*****************************************************************************
   #*****************************************************************************
   # Company Name
   'company_name' : 'XYZ Company',

   # Backup Owner's Name
   'owner_name' : 'David McAllister',

   # Backup Owner's Address
   'owner_address' : '1831 Evergreen Lane, Shakopee, MN 55379',

   # Backup Owner's Email addresses for notification purposes
   # Priority is from first to last, althoug all will be notified
   # with application broadcasts
   'backup_owner_email_addreses' : [
                                    'perldave@gmail.com',
                                    'david.mcallister@asicanalytic.com'
                                   ],

   # Backup Owner's Email addresses for notification purposes
   # Priority is from first to last, althoug all will be notified
   # with application broadcasts
   'backup_owner_phone_numbers' : {
                                   'cell' : '952-445-9242',
                                   'home' : '952-715-0360'
                                  },

   # Unique and abitrary name selected by the user to identify this backup set
   'backup_group_name' : 'some_abritrary_user_selected_label',

   # Email address used for GPG encryption
   'gpg_email' : 'xxx@somedomain.com',
   #*****************************************************************************
   #*****************************************************************************



   #*****************************************************************************
   #*****************************************************************************
   # Starting point to locate all files and directories to be backed up
   'base_directory' : '/home/david',
   #*****************************************************************************
   #*****************************************************************************




   #*****************************************************************************
   #*****************************************************************************
   'enable_backups' : True, # Enter False to disable any and all backups from being made
                            # This has has the highest priority of all in this application.
                            # This is basically an ON/OFF switch for the entire application.
   #*****************************************************************************
   #*****************************************************************************




   #*****************************************************************************
   #*****************************************************************************
   #   ********   Full backups have priority over incremental   ********
   #   ********   UNCOMMENT ONE OF:                             ********
   #   ********   Set value as appropriate.                     ********
   #
   #'full_backup_frequency' : [ 'daily',      ''      ],  # daily
   #'full_backup_frequency' : [ 'dow',        'Sat'   ],  # day_of_week  ( Sun, Mon, Tue, Wed, Thu, Fri, Sat )
   'full_backup_frequency' : [ 'biweekly',   'Thu',   True   ],  # day_of_BIweek ( Sun, Mon, Tue, Wed, Thu, Fri, Sat ),  True for one date independent 1-week offset, False for no offset
   #'full_backup_frequency' : [ 'dom',        14       ],  # day_of_month ( 1-31 ) For short months, numbers exceeding the number of days in a month get truncated to the last day of the month
   #'full_backup_frequency' : [ 'quarterly',  'first' ],  # first or last day of calendar quarter
   #
   #*****************************************************************************
   #*****************************************************************************




   #*****************************************************************************
   #*****************************************************************************
   #   ********   Enter the maximum number of incremental backups after a full backup                 ********
   #   ********   Once the maximum is reached, a full backup is performed.                            ********
   #   ********   If set to a non-zero value, this has priority of the incremental frequency below.   ********
   'max_incrementals' : 5, # Enter 0 if there is no maximum
   #*****************************************************************************
   #*****************************************************************************




   #*****************************************************************************
   #*****************************************************************************
   #   ********   UNCOMMENT ONE OF:           ********
   #   ********   Set value as appropriate.   ********
   #
   #'incremental_frequency' : [ 'none',      ''      ],  # No incremental backups
   #'incremental_frequency' : [ 'daily',     ''      ],  # daily
   'incremental_frequency' : [ 'dow',       'Sun'   ],  # day_of_week  ( Sun, Mon, Tue, Wed, Thu, Fri, Sat )
   #'incremental_frequency' : [ 'biweekly',  'Wed'   ],  # day_of_BIweek ( Sun, Mon, Tue, Wed, Thu, Fri, Sat )
   #'incremental_frequency' : [ 'dom',       28       ],  # day_of_month ( 1-28 or last )
                                                         # if the full frequency is also 'dom', then the incremental frequency
                                                         # is 15 days after the full backup date
   #'number_of_incrementals_per_full_backup_period' : 3,
   #
   #*****************************************************************************
   #*****************************************************************************




   #*****************************************************************************
   #*****************************************************************************
   'backup_time_of_day' : '01_10',  # time_of_day: format is hh_mm ( military time )
   #*****************************************************************************
   #*****************************************************************************




   #*****************************************************************************
   #*****************************************************************************
   # List of files and directories to be backed up.
   # Their location is relative to the base_directory specified above.
   'files_dirs' : {
                   'dummy_xxx'             : True,  # True means encrypt first, then backup
                   'dummy.py'              : True,  # False means no encryption
                   'benchmarks.py'         : True,
                   'file_count.py'         : True,
                   'grep_a_file.py_xxx.py' : True,
                   'grep_a_file.py'        : True,
                   'grep_a_file_01.py'     : False,
                   'scratch.py'            : True,
                   'grep_a_file_02.py'     : True,
                   'unit_test.py'          : True,
                   'backup.py'             : True,
                   'backup_conf.py'        : True,
                   'fredddd.py'            : True,
                   'duuud'                 : True,
                   'yyyyyyyyy'             : True,
                   'zzzzzzzzz'             : True,
                   'rrrrrrrrrrr'           : True,
                   'wwwwwww'               : True
                  },
   #*****************************************************************************
   #*****************************************************************************




   #*****************************************************************************
   #*****************************************************************************
   # Backup locations
   # Their location is relative to the base_directory specified above.
   'backup_location_reference' :  'local_backup', # One and ONLY one entry must be the 'REFERENCE_BACKUP' directory
                                                  # against which subsequent backup directories are checked.
                                                  # This should be a local drive to ensure that backup to this
                                                  # directory does not depend upon a network connection.

   'backup_location_others' : [
                               'Dropbox/backups',
                               'Dropbox/backups_01'
                              ]
   #*****************************************************************************
   #*****************************************************************************


         }
