
import unittest
import sys
import backup_support
import backup
import time
import calendar

#import backup_conf
import time_extra as te

class Test_xxx(unittest.TestCase):
   def setUp(self):
      pass


   def test_yyy(self):
      self.assertTrue( 'a' == 'a' )



      self.assertFalse( backup_support.UniversalDiff('/home/david/aaaa_xxx.tar.gz', '/home/david/bbbb_xxx.tar.gz') )
      self.assertFalse( backup_support.UniversalDiff('/home/david/aaaa.tar', '/home/david/bbbb.tar') )
      self.assertTrue(  backup_support.UniversalDiff('/home/david/aaaa/file_3.gz', '/home/david/bbbb/file_3.gz') )
      self.assertTrue(  backup_support.UniversalDiff('/home/david/aaaa/file_1', '/home/david/bbbb/file_1') )
      self.assertFalse( backup_support.UniversalDiff('/home/david/aaaa', '/home/david/bbbb') )


      self.assertTrue( backup.main() )


   def tearDown(self):
      pass


class Test_yyy(unittest.TestCase):
   def setUp(self):
      self.backup_obj = backup_support.Back_Up(time.gmtime())
      self.te         = te.time_extra()
      self.seconds_per_day  = self.backup_obj.seconds_per_day

      self.times_1  = [
                       1379377097.0,     # time.gmtime(),
                       1368404660.0,     # calendar.timegm(time.gmtime()) - self.seconds_per_day * 126.72,
                       1386911606.0,     # calendar.timegm(time.gmtime()) + self.seconds_per_day * 87,
                       1039746409.0,     # calendar.timegm(time.gmtime()) - self.seconds_per_day * 10.77*365,
                       1484129600.0,     # calendar.timegm(time.gmtime()) + self.seconds_per_day * 3.32*365,
                       1000961010.0,     # calendar.timegm(time.gmtime()) - self.seconds_per_day *    12*365,
                       1442473661.0      # calendar.timegm(time.gmtime()) + self.seconds_per_day * 2*365
                      ]

      self.times_2  = [
                       1379401200.0,     # time.gmtime(),
                       1379669700.88,    # calendar.timegm(time.gmtime()) + self.seconds_per_day * 3.1417,
                       1369378601.0,     # calendar.timegm(time.gmtime()) - self.seconds_per_day * 116,
                       1396680705.0,     # calendar.timegm(time.gmtime()) + self.seconds_per_day * 0.548*365,
                       1360308007.0,     # calendar.timegm(time.gmtime()) - self.seconds_per_day * 0.605*365,
                       1757831200.0,     # calendar.timegm(time.gmtime()) + self.seconds_per_day *    12*365,
                       1316329223.0      # calendar.timegm(time.gmtime()) - self.seconds_per_day * 2*365
                      ]

      self.times_1_epoch_first  = [
                                   1379376000.0,
                                   1368403200.0,
                                   1386892800.0,
                                   1039737600.0,
                                   1484092800.0,
                                   1000944000.0,
                                   1442448000.0
                                  ]

      self.times_2_epoch_first  = [
                                   1379376000.0,
                                   1379635200.0,
                                   1369353600.0,
                                   1396656000.0,
                                   1360281600.0,
                                   1757808000.0,
                                   1316304000.0
                                  ]


   def test_convert_backup_hour_minute_to_seconds(self):
      hh_mm_set = {
                   '00_00' : 0,
                   '02_16' : 8160,
                   '23_59' : 86340
                  }
      for hh_mm in hh_mm_set:
         self.assertEqual( hh_mm_set[hh_mm], self.backup_obj.convert_backup_hour_minute_to_seconds(hh_mm) )


   def test_increment_day_by_n_months(self):
      data_set = [ #month_step reference_time   reference_date                 new_date
                  ['-26',  1311027829,  'Mon Jul 18 22:23:49 2011',  'Mon Jul 18 22:23:49 2011'],
                  ['-25',  1313706229,  'Thu Aug 18 22:23:49 2011',  'Thu Aug 18 22:23:49 2011'],
                  ['-24',  1316384629,  'Sun Sep 18 22:23:49 2011',  'Sun Sep 18 22:23:49 2011'],
                  ['-23',  1318976629,  'Tue Oct 18 22:23:49 2011',  'Tue Oct 18 22:23:49 2011'],
                  ['-22',  1321655029,  'Fri Nov 18 23:23:49 2011',  'Fri Nov 18 22:23:49 2011'],
                  ['-21',  1324247029,  'Sun Dec 18 23:23:49 2011',  'Sun Dec 18 22:23:49 2011'],
                  ['-20',  1326925429,  'Wed Jan 18 23:23:49 2012',  'Wed Jan 18 22:23:49 2012'],
                  ['-19',  1329603829,  'Sat Feb 18 23:23:49 2012',  'Sat Feb 18 22:23:49 2012'],
                  ['-18',  1332109429,  'Sun Mar 18 22:23:49 2012',  'Sun Mar 18 22:23:49 2012'],
                  ['-17',  1334787829,  'Wed Apr 18 22:23:49 2012',  'Wed Apr 18 22:23:49 2012'],
                  ['-16',  1337379829,  'Fri May 18 22:23:49 2012',  'Fri May 18 22:23:49 2012'],
                  ['-15',  1340058229,  'Mon Jun 18 22:23:49 2012',  'Mon Jun 18 22:23:49 2012'],
                  ['-14',  1342650229,  'Wed Jul 18 22:23:49 2012',  'Wed Jul 18 22:23:49 2012'],
                  ['-13',  1345328629,  'Sat Aug 18 22:23:49 2012',  'Sat Aug 18 22:23:49 2012'],
                  ['-12',  1348007029,  'Tue Sep 18 22:23:49 2012',  'Tue Sep 18 22:23:49 2012'],
                  ['-11',  1350599029,  'Thu Oct 18 22:23:49 2012',  'Thu Oct 18 22:23:49 2012'],
                  ['-10',  1353277429,  'Sun Nov 18 23:23:49 2012',  'Sun Nov 18 22:23:49 2012'],
                  [ '-9',  1355869429,  'Tue Dec 18 23:23:49 2012',  'Tue Dec 18 22:23:49 2012'],
                  [ '-8',  1358547829,  'Fri Jan 18 23:23:49 2013',  'Fri Jan 18 22:23:49 2013'],
                  [ '-7',  1361226229,  'Mon Feb 18 23:23:49 2013',  'Mon Feb 18 22:23:49 2013'],
                  [ '-6',  1363645429,  'Mon Mar 18 22:23:49 2013',  'Mon Mar 18 22:23:49 2013'],
                  [ '-5',  1366323829,  'Thu Apr 18 22:23:49 2013',  'Thu Apr 18 22:23:49 2013'],
                  [ '-4',  1368915829,  'Sat May 18 22:23:49 2013',  'Sat May 18 22:23:49 2013'],
                  [ '-3',  1371594229,  'Tue Jun 18 22:23:49 2013',  'Tue Jun 18 22:23:49 2013'],
                  [ '-2',  1374186229,  'Thu Jul 18 22:23:49 2013',  'Thu Jul 18 22:23:49 2013'],
                  [ '-1',  1376864629,  'Sun Aug 18 22:23:49 2013',  'Sun Aug 18 22:23:49 2013'],
                  [  '0',  1379543029,  'Wed Sep 18 22:23:49 2013',  'Wed Sep 18 22:23:49 2013'],
                  [  '1',  1382135029,  'Fri Oct 18 22:23:49 2013',  'Fri Oct 18 22:23:49 2013'],
                  [  '2',  1384813429,  'Mon Nov 18 23:23:49 2013',  'Mon Nov 18 22:23:49 2013'],
                  [  '3',  1387405429,  'Wed Dec 18 23:23:49 2013',  'Wed Dec 18 22:23:49 2013'],
                  [  '4',  1390083829,  'Sat Jan 18 23:23:49 2014',  'Sat Jan 18 22:23:49 2014'],
                  [  '5',  1392762229,  'Tue Feb 18 23:23:49 2014',  'Tue Feb 18 22:23:49 2014'],
                  [  '6',  1395181429,  'Tue Mar 18 22:23:49 2014',  'Tue Mar 18 22:23:49 2014'],
                  [  '7',  1397859829,  'Fri Apr 18 22:23:49 2014',  'Fri Apr 18 22:23:49 2014'],
                  [  '8',  1400451829,  'Sun May 18 22:23:49 2014',  'Sun May 18 22:23:49 2014'],
                  [  '9',  1403130229,  'Wed Jun 18 22:23:49 2014',  'Wed Jun 18 22:23:49 2014'],
                  [ '10',  1405722229,  'Fri Jul 18 22:23:49 2014',  'Fri Jul 18 22:23:49 2014'],
                  [ '11',  1408400629,  'Mon Aug 18 22:23:49 2014',  'Mon Aug 18 22:23:49 2014'],
                  [ '12',  1411079029,  'Thu Sep 18 22:23:49 2014',  'Thu Sep 18 22:23:49 2014'],
                  [ '13',  1413671029,  'Sat Oct 18 22:23:49 2014',  'Sat Oct 18 22:23:49 2014'],
                  [ '14',  1416349429,  'Tue Nov 18 23:23:49 2014',  'Tue Nov 18 22:23:49 2014'],
                  [ '15',  1418941429,  'Thu Dec 18 23:23:49 2014',  'Thu Dec 18 22:23:49 2014'],
                  [ '16',  1421619829,  'Sun Jan 18 23:23:49 2015',  'Sun Jan 18 22:23:49 2015'],
                  [ '17',  1424298229,  'Wed Feb 18 23:23:49 2015',  'Wed Feb 18 22:23:49 2015'],
                  [ '18',  1426717429,  'Wed Mar 18 22:23:49 2015',  'Wed Mar 18 22:23:49 2015'],
                  [ '19',  1429395829,  'Sat Apr 18 22:23:49 2015',  'Sat Apr 18 22:23:49 2015'],
                  [ '20',  1431987829,  'Mon May 18 22:23:49 2015',  'Mon May 18 22:23:49 2015'],
                  [ '21',  1434666229,  'Thu Jun 18 22:23:49 2015',  'Thu Jun 18 22:23:49 2015'],
                  [ '22',  1437258229,  'Sat Jul 18 22:23:49 2015',  'Sat Jul 18 22:23:49 2015'],
                  [ '23',  1439936629,  'Tue Aug 18 22:23:49 2015',  'Tue Aug 18 22:23:49 2015'],
                  [ '24',  1442615029,  'Fri Sep 18 22:23:49 2015',  'Fri Sep 18 22:23:49 2015'],
                  [ '25',  1445207029,  'Sun Oct 18 22:23:49 2015',  'Sun Oct 18 22:23:49 2015'],
                  [ '26',  1447885429,  'Wed Nov 18 23:23:49 2015',  'Wed Nov 18 22:23:49 2015']
                 ]


      data_set_end_of_month_00 = [
                 #month_step reference_time   reference_date                 new_date
                  ['-26',  1262301829,  'Mon Jul 18 22:23:49 2011',  'Thu Dec 31 23:23:49 2009'],
                  ['-25',  1264980229,  'Thu Aug 18 22:23:49 2011',  'Sun Jan 31 23:23:49 2010'],
                  ['-24',  1267399429,  'Sun Sep 18 22:23:49 2011',  'Sun Feb 28 23:23:49 2010'],
                  ['-23',  1270077829,  'Tue Oct 18 22:23:49 2011',  'Wed Mar 31 23:23:49 2010'],
                  ['-22',  1272669829,  'Fri Nov 18 22:23:49 2011',  'Fri Apr 30 23:23:49 2010'],
                  ['-21',  1275348229,  'Sun Dec 18 22:23:49 2011',  'Mon May 31 23:23:49 2010'],
                  ['-20',  1277940229,  'Wed Jan 18 22:23:49 2012',  'Wed Jun 30 23:23:49 2010'],
                  ['-19',  1280618629,  'Sat Feb 18 22:23:49 2012',  'Sat Jul 31 23:23:49 2010'],
                  ['-18',  1283297029,  'Sun Mar 18 22:23:49 2012',  'Tue Aug 31 23:23:49 2010'],
                  ['-17',  1285889029,  'Wed Apr 18 22:23:49 2012',  'Thu Sep 30 23:23:49 2010'],
                  ['-16',  1288567429,  'Fri May 18 22:23:49 2012',  'Sun Oct 31 23:23:49 2010'],
                  ['-15',  1291159429,  'Mon Jun 18 22:23:49 2012',  'Tue Nov 30 23:23:49 2010'],
                  ['-14',  1293837829,  'Wed Jul 18 22:23:49 2012',  'Fri Dec 31 23:23:49 2010'],
                  ['-13',  1296516229,  'Sat Aug 18 22:23:49 2012',  'Mon Jan 31 23:23:49 2011'],
                  ['-12',  1298935429,  'Tue Sep 18 22:23:49 2012',  'Mon Feb 28 23:23:49 2011'],
                  ['-11',  1301613829,  'Thu Oct 18 22:23:49 2012',  'Thu Mar 31 23:23:49 2011'],
                  ['-10',  1304205829,  'Sun Nov 18 22:23:49 2012',  'Sat Apr 30 23:23:49 2011'],
                  [ '-9',  1306884229,  'Tue Dec 18 22:23:49 2012',  'Tue May 31 23:23:49 2011'],
                  [ '-8',  1309476229,  'Fri Jan 18 22:23:49 2013',  'Thu Jun 30 23:23:49 2011'],
                  [ '-7',  1312154629,  'Mon Feb 18 22:23:49 2013',  'Sun Jul 31 23:23:49 2011'],
                  [ '-6',  1314833029,  'Mon Mar 18 22:23:49 2013',  'Wed Aug 31 23:23:49 2011'],
                  [ '-5',  1317425029,  'Thu Apr 18 22:23:49 2013',  'Fri Sep 30 23:23:49 2011'],
                  [ '-4',  1320103429,  'Sat May 18 22:23:49 2013',  'Mon Oct 31 23:23:49 2011'],
                  [ '-3',  1322695429,  'Tue Jun 18 22:23:49 2013',  'Wed Nov 30 23:23:49 2011'],
                  [ '-2',  1325373829,  'Thu Jul 18 22:23:49 2013',  'Sat Dec 31 23:23:49 2011'],
                  [ '-1',  1328052229,  'Sun Aug 18 22:23:49 2013',  'Tue Jan 31 23:23:49 2012'],
                  [  '0',  1330557829,  'Wed Sep 18 22:23:49 2013',  'Wed Feb 29 23:23:49 2012'],
                  [  '1',  1333236229,  'Fri Oct 18 22:23:49 2013',  'Sat Mar 31 23:23:49 2012'],
                  [  '2',  1335828229,  'Mon Nov 18 22:23:49 2013',  'Mon Apr 30 23:23:49 2012'],
                  [  '3',  1338506629,  'Wed Dec 18 22:23:49 2013',  'Thu May 31 23:23:49 2012'],
                  [  '4',  1341098629,  'Sat Jan 18 22:23:49 2014',  'Sat Jun 30 23:23:49 2012'],
                  [  '5',  1343777029,  'Tue Feb 18 22:23:49 2014',  'Tue Jul 31 23:23:49 2012'],
                  [  '6',  1346455429,  'Tue Mar 18 22:23:49 2014',  'Fri Aug 31 23:23:49 2012'],
                  [  '7',  1349047429,  'Fri Apr 18 22:23:49 2014',  'Sun Sep 30 23:23:49 2012'],
                  [  '8',  1351725829,  'Sun May 18 22:23:49 2014',  'Wed Oct 31 23:23:49 2012'],
                  [  '9',  1354317829,  'Wed Jun 18 22:23:49 2014',  'Fri Nov 30 23:23:49 2012'],
                  [ '10',  1356996229,  'Fri Jul 18 22:23:49 2014',  'Mon Dec 31 23:23:49 2012'],
                  [ '11',  1359674629,  'Mon Aug 18 22:23:49 2014',  'Thu Jan 31 23:23:49 2013'],
                  [ '12',  1362093829,  'Thu Sep 18 22:23:49 2014',  'Thu Feb 28 23:23:49 2013'],
                  [ '13',  1364772229,  'Sat Oct 18 22:23:49 2014',  'Sun Mar 31 23:23:49 2013'],
                  [ '14',  1367364229,  'Tue Nov 18 22:23:49 2014',  'Tue Apr 30 23:23:49 2013'],
                  [ '15',  1370042629,  'Thu Dec 18 22:23:49 2014',  'Fri May 31 23:23:49 2013'],
                  [ '16',  1372634629,  'Sun Jan 18 22:23:49 2015',  'Sun Jun 30 23:23:49 2013'],
                  [ '17',  1375313029,  'Wed Feb 18 22:23:49 2015',  'Wed Jul 31 23:23:49 2013'],
                  [ '18',  1377991429,  'Wed Mar 18 22:23:49 2015',  'Sat Aug 31 23:23:49 2013'],
                  [ '19',  1380583429,  'Sat Apr 18 22:23:49 2015',  'Mon Sep 30 23:23:49 2013'],
                  [ '20',  1383261829,  'Mon May 18 22:23:49 2015',  'Thu Oct 31 23:23:49 2013'],
                  [ '21',  1385853829,  'Thu Jun 18 22:23:49 2015',  'Sat Nov 30 23:23:49 2013'],
                  [ '22',  1388532229,  'Sat Jul 18 22:23:49 2015',  'Tue Dec 31 23:23:49 2013'],
                  [ '23',  1391210629,  'Tue Aug 18 22:23:49 2015',  'Fri Jan 31 23:23:49 2014'],
                  [ '24',  1393629829,  'Fri Sep 18 22:23:49 2015',  'Fri Feb 28 23:23:49 2014'],
                  [ '25',  1396308229,  'Sun Oct 18 22:23:49 2015',  'Mon Mar 31 23:23:49 2014'],
                  [ '26',  1398900229,  'Wed Nov 18 22:23:49 2015',  'Wed Apr 30 23:23:49 2014']






                 ]


      data_set_end_of_month_01 = [
                 #month_step reference_time   reference_date                 new_date
                  ['-26',  1322695429,  'Wed Nov 30 23:23:49 2011',  'Wed Nov 30 23:23:49 2011'],
                  ['-25',  1325373829,  'Sat Dec 31 23:23:49 2011',  'Sat Dec 31 23:23:49 2011'],
                  ['-24',  1328052229,  'Tue Jan 31 23:23:49 2012',  'Tue Jan 31 23:23:49 2012'],
                  ['-23',  1330557829,  'Wed Feb 29 23:23:49 2012',  'Wed Feb 29 23:23:49 2012'],
                  ['-22',  1333236229,  'Sat Mar 31 22:23:49 2012',  'Sat Mar 31 23:23:49 2012'],
                  ['-21',  1335828229,  'Mon Apr 30 22:23:49 2012',  'Mon Apr 30 23:23:49 2012'],
                  ['-20',  1338506629,  'Thu May 31 22:23:49 2012',  'Thu May 31 23:23:49 2012'],
                  ['-19',  1341098629,  'Sat Jun 30 22:23:49 2012',  'Sat Jun 30 23:23:49 2012'],
                  ['-18',  1343777029,  'Tue Jul 31 22:23:49 2012',  'Tue Jul 31 23:23:49 2012'],
                  ['-17',  1346455429,  'Fri Aug 31 22:23:49 2012',  'Fri Aug 31 23:23:49 2012'],
                  ['-16',  1349047429,  'Sun Sep 30 22:23:49 2012',  'Sun Sep 30 23:23:49 2012'],
                  ['-15',  1351725829,  'Wed Oct 31 22:23:49 2012',  'Wed Oct 31 23:23:49 2012'],
                  ['-14',  1354317829,  'Fri Nov 30 23:23:49 2012',  'Fri Nov 30 23:23:49 2012'],
                  ['-13',  1356996229,  'Mon Dec 31 23:23:49 2012',  'Mon Dec 31 23:23:49 2012'],
                  ['-12',  1359674629,  'Thu Jan 31 23:23:49 2013',  'Thu Jan 31 23:23:49 2013'],
                  ['-11',  1362093829,  'Thu Feb 28 23:23:49 2013',  'Thu Feb 28 23:23:49 2013'],
                  ['-10',  1364772229,  'Sun Mar 31 22:23:49 2013',  'Sun Mar 31 23:23:49 2013'],
                  [ '-9',  1367364229,  'Tue Apr 30 22:23:49 2013',  'Tue Apr 30 23:23:49 2013'],
                  [ '-8',  1370042629,  'Fri May 31 22:23:49 2013',  'Fri May 31 23:23:49 2013'],
                  [ '-7',  1372634629,  'Sun Jun 30 22:23:49 2013',  'Sun Jun 30 23:23:49 2013'],
                  [ '-6',  1375313029,  'Wed Jul 31 22:23:49 2013',  'Wed Jul 31 23:23:49 2013'],
                  [ '-5',  1377991429,  'Sat Aug 31 22:23:49 2013',  'Sat Aug 31 23:23:49 2013'],
                  [ '-4',  1380583429,  'Mon Sep 30 22:23:49 2013',  'Mon Sep 30 23:23:49 2013'],
                  [ '-3',  1383261829,  'Thu Oct 31 22:23:49 2013',  'Thu Oct 31 23:23:49 2013'],
                  [ '-2',  1385853829,  'Sat Nov 30 23:23:49 2013',  'Sat Nov 30 23:23:49 2013'],
                  [ '-1',  1388532229,  'Tue Dec 31 23:23:49 2013',  'Tue Dec 31 23:23:49 2013'],
                  [  '0',  1391210629,  'Fri Jan 31 23:23:49 2014',  'Fri Jan 31 23:23:49 2014'],
                  [  '1',  1393629829,  'Fri Feb 28 23:23:49 2014',  'Fri Feb 28 23:23:49 2014'],
                  [  '2',  1396308229,  'Mon Mar 31 22:23:49 2014',  'Mon Mar 31 23:23:49 2014'],
                  [  '3',  1398900229,  'Wed Apr 30 22:23:49 2014',  'Wed Apr 30 23:23:49 2014'],
                  [  '4',  1401578629,  'Sat May 31 22:23:49 2014',  'Sat May 31 23:23:49 2014'],
                  [  '5',  1404170629,  'Mon Jun 30 22:23:49 2014',  'Mon Jun 30 23:23:49 2014'],
                  [  '6',  1406849029,  'Thu Jul 31 22:23:49 2014',  'Thu Jul 31 23:23:49 2014'],
                  [  '7',  1409527429,  'Sun Aug 31 22:23:49 2014',  'Sun Aug 31 23:23:49 2014'],
                  [  '8',  1412119429,  'Tue Sep 30 22:23:49 2014',  'Tue Sep 30 23:23:49 2014'],
                  [  '9',  1414797829,  'Fri Oct 31 22:23:49 2014',  'Fri Oct 31 23:23:49 2014'],
                  [ '10',  1417389829,  'Sun Nov 30 23:23:49 2014',  'Sun Nov 30 23:23:49 2014'],
                  [ '11',  1420068229,  'Wed Dec 31 23:23:49 2014',  'Wed Dec 31 23:23:49 2014'],
                  [ '12',  1422746629,  'Sat Jan 31 23:23:49 2015',  'Sat Jan 31 23:23:49 2015'],
                  [ '13',  1425165829,  'Sat Feb 28 23:23:49 2015',  'Sat Feb 28 23:23:49 2015'],
                  [ '14',  1427844229,  'Tue Mar 31 22:23:49 2015',  'Tue Mar 31 23:23:49 2015'],
                  [ '15',  1430436229,  'Thu Apr 30 22:23:49 2015',  'Thu Apr 30 23:23:49 2015'],
                  [ '16',  1433114629,  'Sun May 31 22:23:49 2015',  'Sun May 31 23:23:49 2015'],
                  [ '17',  1435706629,  'Tue Jun 30 22:23:49 2015',  'Tue Jun 30 23:23:49 2015'],
                  [ '18',  1438385029,  'Fri Jul 31 22:23:49 2015',  'Fri Jul 31 23:23:49 2015'],
                  [ '19',  1441063429,  'Mon Aug 31 22:23:49 2015',  'Mon Aug 31 23:23:49 2015'],
                  [ '20',  1443655429,  'Wed Sep 30 22:23:49 2015',  'Wed Sep 30 23:23:49 2015'],
                  [ '21',  1446333829,  'Sat Oct 31 22:23:49 2015',  'Sat Oct 31 23:23:49 2015'],
                  [ '22',  1448925829,  'Mon Nov 30 23:23:49 2015',  'Mon Nov 30 23:23:49 2015'],
                  [ '23',  1451604229,  'Thu Dec 31 23:23:49 2015',  'Thu Dec 31 23:23:49 2015'],
                  [ '24',  1454282629,  'Sun Jan 31 23:23:49 2016',  'Sun Jan 31 23:23:49 2016'],
                  [ '25',  1456788229,  'Mon Feb 29 23:23:49 2016',  'Mon Feb 29 23:23:49 2016'],
                  [ '26',  1459466629,  'Thu Mar 31 22:23:49 2016',  'Thu Mar 31 23:23:49 2016']
                 ]


      data_set_end_of_month_02 = [
                 #month_step reference_time   reference_date                 new_date
                  [ '-26',  1356996229,  'Mon Dec 31 23:23:49 2012',  'Mon Dec 31 23:23:49 2012'],
                  [ '-25',  1359674629,  'Thu Jan 31 23:23:49 2013',  'Thu Jan 31 23:23:49 2013'],
                  [ '-24',  1362093829,  'Thu Feb 28 23:23:49 2013',  'Thu Feb 28 23:23:49 2013'],
                  [ '-23',  1364772229,  'Sun Mar 31 22:23:49 2013',  'Sun Mar 31 23:23:49 2013'],
                  [ '-22',  1367364229,  'Tue Apr 30 22:23:49 2013',  'Tue Apr 30 23:23:49 2013'],
                  [ '-21',  1370042629,  'Fri May 31 22:23:49 2013',  'Fri May 31 23:23:49 2013'],
                  [ '-20',  1372634629,  'Sun Jun 30 22:23:49 2013',  'Sun Jun 30 23:23:49 2013'],
                  [ '-19',  1375313029,  'Wed Jul 31 22:23:49 2013',  'Wed Jul 31 23:23:49 2013'],
                  [ '-18',  1377991429,  'Sat Aug 31 22:23:49 2013',  'Sat Aug 31 23:23:49 2013'],
                  [ '-17',  1380583429,  'Mon Sep 30 22:23:49 2013',  'Mon Sep 30 23:23:49 2013'],
                  [ '-16',  1383261829,  'Thu Oct 31 22:23:49 2013',  'Thu Oct 31 23:23:49 2013'],
                  [ '-15',  1385853829,  'Sat Nov 30 23:23:49 2013',  'Sat Nov 30 23:23:49 2013'],
                  [ '-14',  1388532229,  'Tue Dec 31 23:23:49 2013',  'Tue Dec 31 23:23:49 2013'],
                  [ '-13',  1391210629,  'Fri Jan 31 23:23:49 2014',  'Fri Jan 31 23:23:49 2014'],
                  [ '-12',  1393629829,  'Fri Feb 28 23:23:49 2014',  'Fri Feb 28 23:23:49 2014'],
                  [ '-11',  1396308229,  'Mon Mar 31 22:23:49 2014',  'Mon Mar 31 23:23:49 2014'],
                  [ '-10',  1398900229,  'Wed Apr 30 22:23:49 2014',  'Wed Apr 30 23:23:49 2014'],
                  [  '-9',  1401578629,  'Sat May 31 22:23:49 2014',  'Sat May 31 23:23:49 2014'],
                  [  '-8',  1404170629,  'Mon Jun 30 22:23:49 2014',  'Mon Jun 30 23:23:49 2014'],
                  [  '-7',  1406849029,  'Thu Jul 31 22:23:49 2014',  'Thu Jul 31 23:23:49 2014'],
                  [  '-6',  1409527429,  'Sun Aug 31 22:23:49 2014',  'Sun Aug 31 23:23:49 2014'],
                  [  '-5',  1412119429,  'Tue Sep 30 22:23:49 2014',  'Tue Sep 30 23:23:49 2014'],
                  [  '-4',  1414797829,  'Fri Oct 31 22:23:49 2014',  'Fri Oct 31 23:23:49 2014'],
                  [  '-3',  1417389829,  'Sun Nov 30 23:23:49 2014',  'Sun Nov 30 23:23:49 2014'],
                  [  '-2',  1420068229,  'Wed Dec 31 23:23:49 2014',  'Wed Dec 31 23:23:49 2014'],
                  [  '-1',  1422746629,  'Sat Jan 31 23:23:49 2015',  'Sat Jan 31 23:23:49 2015'],
                  [   '0',  1425165829,  'Sat Feb 28 23:23:49 2015',  'Sat Feb 28 23:23:49 2015'],
                  [   '1',  1427844229,  'Tue Mar 31 22:23:49 2015',  'Tue Mar 31 23:23:49 2015'],
                  [   '2',  1430436229,  'Thu Apr 30 22:23:49 2015',  'Thu Apr 30 23:23:49 2015'],
                  [   '3',  1433114629,  'Sun May 31 22:23:49 2015',  'Sun May 31 23:23:49 2015'],
                  [   '4',  1435706629,  'Tue Jun 30 22:23:49 2015',  'Tue Jun 30 23:23:49 2015'],
                  [   '5',  1438385029,  'Fri Jul 31 22:23:49 2015',  'Fri Jul 31 23:23:49 2015'],
                  [   '6',  1441063429,  'Mon Aug 31 22:23:49 2015',  'Mon Aug 31 23:23:49 2015'],
                  [   '7',  1443655429,  'Wed Sep 30 22:23:49 2015',  'Wed Sep 30 23:23:49 2015'],
                  [   '8',  1446333829,  'Sat Oct 31 22:23:49 2015',  'Sat Oct 31 23:23:49 2015'],
                  [   '9',  1448925829,  'Mon Nov 30 23:23:49 2015',  'Mon Nov 30 23:23:49 2015'],
                  [  '10',  1451604229,  'Thu Dec 31 23:23:49 2015',  'Thu Dec 31 23:23:49 2015'],
                  [  '11',  1454282629,  'Sun Jan 31 23:23:49 2016',  'Sun Jan 31 23:23:49 2016'],
                  [  '12',  1456788229,  'Mon Feb 29 23:23:49 2016',  'Mon Feb 29 23:23:49 2016'],
                  [  '13',  1459466629,  'Thu Mar 31 22:23:49 2016',  'Thu Mar 31 23:23:49 2016'],
                  [  '14',  1462058629,  'Sat Apr 30 22:23:49 2016',  'Sat Apr 30 23:23:49 2016'],
                  [  '15',  1464737029,  'Tue May 31 22:23:49 2016',  'Tue May 31 23:23:49 2016'],
                  [  '16',  1467329029,  'Thu Jun 30 22:23:49 2016',  'Thu Jun 30 23:23:49 2016'],
                  [  '17',  1470007429,  'Sun Jul 31 22:23:49 2016',  'Sun Jul 31 23:23:49 2016'],
                  [  '18',  1472685829,  'Wed Aug 31 22:23:49 2016',  'Wed Aug 31 23:23:49 2016'],
                  [  '19',  1475277829,  'Fri Sep 30 22:23:49 2016',  'Fri Sep 30 23:23:49 2016'],
                  [  '20',  1477956229,  'Mon Oct 31 22:23:49 2016',  'Mon Oct 31 23:23:49 2016'],
                  [  '21',  1480548229,  'Wed Nov 30 23:23:49 2016',  'Wed Nov 30 23:23:49 2016'],
                  [  '22',  1483226629,  'Sat Dec 31 23:23:49 2016',  'Sat Dec 31 23:23:49 2016'],
                  [  '23',  1485905029,  'Tue Jan 31 23:23:49 2017',  'Tue Jan 31 23:23:49 2017'],
                  [  '24',  1488324229,  'Tue Feb 28 23:23:49 2017',  'Tue Feb 28 23:23:49 2017'],
                  [  '25',  1491002629,  'Fri Mar 31 22:23:49 2017',  'Fri Mar 31 23:23:49 2017'],
                  [  '26',  1493594629,  'Sun Apr 30 22:23:49 2017',  'Sun Apr 30 23:23:49 2017']
                 ]

      time_in = 1379543029.0
      for month_step in data_set:

         # Check against output epoch time
         self.assertEqual( month_step[1], self.te.increment_day_by_n_months(time_in, int(month_step[0]) ) )
         self.assertEqual( month_step[1], calendar.timegm( self.te.increment_day_by_n_months(time.gmtime(time_in), int(month_step[0])) ) )

         # Check against output date_time string
         self.assertEqual( month_step[3], time.asctime(time.gmtime( self.te.increment_day_by_n_months(time_in, int(month_step[0])) )) )
         self.assertEqual( month_step[3], time.asctime(time.gmtime( calendar.timegm( self.te.increment_day_by_n_months(time.gmtime(time_in), int(month_step[0])) ) ) ) )


       # Example 1 of End Of Month
      time_xxx = 1329607429.0 + 11 * self.seconds_per_day
      for month_step in data_set_end_of_month_00:
         self.assertEqual( month_step[1], self.te.increment_day_by_n_months(time_xxx, int(month_step[0]) ) )
         self.assertEqual( month_step[3], time.asctime(time.gmtime( self.te.increment_day_by_n_months(time_xxx, int(month_step[0])) ) ) )

       # Example 2 of End Of Month
      time_xxx = 1390087429.0 + 13 * self.seconds_per_day
      for month_step in data_set_end_of_month_01:
         self.assertEqual( month_step[1], self.te.increment_day_by_n_months(time_xxx, int(month_step[0]) ) )
         self.assertEqual( month_step[3], time.asctime(time.gmtime( self.te.increment_day_by_n_months(time_xxx, int(month_step[0])) ) ) )

       # Example 3 of End Of Month
      time_xxx = 1424301829.0 + 10 * self.seconds_per_day
      for month_step in data_set_end_of_month_02:

#         print " first  /  second    '%s',  %s,  '%s',  '%s'" % ( month_step[0], self.te.increment_day_by_n_months(time_xxx, int(month_step[0]) ), time.asctime(time.gmtime( month_step[1] )), time.asctime(time.gmtime( self.te.increment_day_by_n_months(time_xxx, int(month_step[0])) ) ) )
#         print "\n\n"
#         print " first  /  second    '%s',  %s,  '%s',  '%s'" % ( month_step[0], time.asctime(time.gmtime( month_step[1] )), month_step[2], time.asctime(time.gmtime( self.te.increment_day_by_n_months(time_in, int(month_step[0])) )) )

         self.assertEqual( month_step[1], self.te.increment_day_by_n_months(time_xxx, int(month_step[0]) ) )
         self.assertEqual( month_step[3], time.asctime(time.gmtime( self.te.increment_day_by_n_months(time_xxx, int(month_step[0])) ) ) )


   def test_increment_day_by_n_days(self):
      time_in = time.gmtime()
      for day_step in range(-400,-400):
         for time_input in [time_in, calendar.timegm(time_in)]:
            incremented_time = self.te.increment_day_by_n_days(time_input, day_step)

            input_epoch_first_of_day  = self.te.truncate_any_time_to_first_epoch_of_day(time_input)
            offset_epoch_first_of_day = self.te.truncate_any_time_to_first_epoch_of_day(incremented_time)

            num_day_offset_a = ( offset_epoch_first_of_day - input_epoch_first_of_day ) / self.seconds_per_day
            num_day_offset_c = num_day_offset_a
            if num_day_offset_a < 0:
               num_day_offset_c = num_day_offset_a - 0.5
            num_day_offset_b = int( num_day_offset_c )
            self.assertEqual( day_step, num_day_offset_b )


   def test_convert_date_to_backup_timeofday_in_epoch(self):
      time_in = time.gmtime()
      for time_input in [time_in, calendar.timegm(time_in)]:

         day_xx = time_input
         if day_xx.__class__.__name__  !=  'struct_time':
            day_xx = time.gmtime(time_input)

         month  = time.strftime("%b", day_xx)
         dom    = time.strftime("%d", day_xx)
         year   = time.strftime("%Y", day_xx)
         start_of_day = time.strptime(dom + ' ' + month + ' ' + year, "%d %b %Y")
         first_epoch_of_day = calendar.timegm(start_of_day)

         epoch_with_time_of_day_offset = first_epoch_of_day  +  self.backup_obj.backup_offset_from_midnight_in_seconds

         self.assertEqual( epoch_with_time_of_day_offset, self.backup_obj.convert_date_to_backup_timeofday_in_epoch(time_in) )


   def test_difference_of_days(self):
      for time_1 in self.times_1:
         time_1_mod = time_1
         if time_1.__class__.__name__ != 'struct_time':
            time_1_mod = time.gmtime(time_1)

         month_1  = time.strftime("%b", time_1_mod)
         dom_1    = time.strftime("%d", time_1_mod)
         year_1   = time.strftime("%Y", time_1_mod)
         start_of_day_1 = time.strptime(dom_1 + ' ' + month_1 + ' ' + year_1, "%d %b %Y")
         first_epoch_of_day_1 = calendar.timegm(start_of_day_1)

         for time_2 in self.times_2:
            time_2_mod = time_2
            if time_2.__class__.__name__ != 'struct_time':
               time_2_mod = time.gmtime(time_2)

            month_2  = time.strftime("%b", time_2_mod)
            dom_2    = time.strftime("%d", time_2_mod)
            year_2   = time.strftime("%Y", time_2_mod)
            start_of_day_2 = time.strptime(dom_2 + ' ' + month_2 + ' ' + year_2, "%d %b %Y")
            first_epoch_of_day_2 = calendar.timegm(start_of_day_2)

            day_delta = round( ( first_epoch_of_day_1  -  first_epoch_of_day_2 ) / self.seconds_per_day )

            self.assertEqual(day_delta, self.te.difference_of_days(time_1, time_2) )


   def test_difference_of_months(self):
      for time_1 in self.times_1:
         time_1_mod = time_1
         if time_1.__class__.__name__ != 'struct_time':
            time_1_mod = time.gmtime(time_1)

         month_1  = time.strftime("%m", time_1_mod)
         dom_1    = time.strftime("%d", time_1_mod)
         year_1   = time.strftime("%Y", time_1_mod)
         start_of_day_1 = time.strptime(dom_1 + ' ' + month_1 + ' ' + year_1, "%d %m %Y")
         first_epoch_of_day_1 = calendar.timegm(start_of_day_1)

         for time_2 in self.times_2:
            time_2_mod = time_2
            if time_2.__class__.__name__ != 'struct_time':
               time_2_mod = time.gmtime(time_2)

            month_2  = time.strftime("%m", time_2_mod)
            dom_2    = time.strftime("%d", time_2_mod)
            year_2   = time.strftime("%Y", time_2_mod)
            start_of_day_2 = time.strptime(dom_2 + ' ' + month_2 + ' ' + year_2, "%d %m %Y")
            first_epoch_of_day_2 = calendar.timegm(start_of_day_2)

            mon_1_int  = int(month_1)
            mon_2_int  = int(month_2)
            year_1_int = int(year_1)
            year_2_int = int(year_2)
            day_delta = ( year_1_int - year_2_int) * 12 + ( mon_1_int - mon_2_int )
            self.assertEqual(day_delta, self.te.difference_of_months(time_1, time_2) )


   def test_truncate_any_time_to_first_epoch_of_day(self):
      times_list  = self.times_1
      times_list += self.times_2

      epochs_list  = self.times_1_epoch_first
      epochs_list += self.times_2_epoch_first

#      print "\n\n"
      for index in range( 0, len(times_list) ):

#         print " first  /  second    %s    %s       %s    %s" % ( times_list[index], epochs_list[index], time.asctime(time.gmtime(   times_list[index]   )), time.asctime(time.gmtime(epochs_list[index])) )

         self.assertEqual( self.te.truncate_any_time_to_first_epoch_of_day( times_list[index] ),  epochs_list[index] )


   def test_get_day_of_month(self):
      test_data = {
                   1464995170.43  : 03,
                   1467307573.28  : 30,
                   1469619976.13  : 27,
                   1471932378.98  : 23,
                   1474244781.83  : 19,
                   1476557184.68  : 15,
                   1478869587.53  : 11,
                   1481181990.38  :  8,
                   1483494393.23  :  4,
                   1485806796.08  : 30,
                   1488119198.93  : 26,
                   1490431601.78  : 25,
                   1492744004.63  : 21,
                   1495056407.48  : 17,
                   1497368810.33  : 13,
                   1499681213.18  : 10,
                   1501993616.03  :  6,
                   1504306018.88  :  1
                  }
      for item in sorted( test_data ):
         time_struct_time = time.gmtime(item)
#         print "\n   epoch  \  dom   '%s'  \  '%s'\n" % (item, test_data[item])

         self.assertEqual( test_data[item], int(self.te.get_day_of_month( item ) ) )
         self.assertEqual( test_data[item], int(self.te.get_day_of_month( time_struct_time ) ) )


   def test_get_month(self):
      test_data = {
                   1464995170.43  : ['06', 'Jun'],
                   1467307573.28  : ['06', 'Jun'],
                   1469619976.13  : ['07', 'Jul'],
                   1471932378.98  : ['08', 'Aug'],
                   1474244781.83  : ['09', 'Sep'],
                   1476557184.68  : ['10', 'Oct'],
                   1478869587.53  : ['11', 'Nov'],
                   1481181990.38  : ['12', 'Dec'],
                   1483494393.23  : ['01', 'Jan'],
                   1485806796.08  : ['01', 'Jan'],
                   1488119198.93  : ['02', 'Feb'],
                   1490431601.78  : ['03', 'Mar'],
                   1492744004.63  : ['04', 'Apr'],
                   1495056407.48  : ['05', 'May'],
                   1497368810.33  : ['06', 'Jun'],
                   1499681213.18  : ['07', 'Jul'],
                   1501993616.03  : ['08', 'Aug'],
                   1504306018.88  : ['09', 'Sep']
                  }

      for item in sorted( test_data ):
         time_struct_time = time.gmtime(item)
         for time_00 in [item, time_struct_time]:
            self.assertEqual( test_data[item][0], self.te.get_month( time_00 ) )
            self.assertEqual( test_data[item][0], self.te.get_month( time_00, True ) )
            self.assertEqual( test_data[item][1], self.te.get_month( time_00, False ) )


   def test_get_year(self):
      test_data = {
                    903127110.38  : '1998',
                    939287916.08  : '1999',
                    956949498.98  : '2000',
                   1106217527.48  : '2005',
                   1142378333.18  : '2006',
                   1178539138.88  : '2007',
                   1227736721.78  : '2008',
                   1245398304.68  : '2009',
                   1299220693.28  : '2011',
                   1575472496.03  : '2019',
                   1579259661.83  : '2020',
                   1633919690.33  : '2021',
                   1683117273.23  : '2023',
                   1763850856.13  : '2025',
                   1908494078.93  : '2030',
                   1944654884.63  : '2031',
                   1962316467.53  : '2032',
                   2074586050.43  : '2035'
                  }

      for item in sorted( test_data ):
         time_struct_time = time.gmtime(item)
         for time_00 in [item, time_struct_time]:
            self.assertEqual( test_data[item], self.te.get_year( time_00 ) )


   def test_truncate_any_time_to_last_epoch_of_day(self):
      test_data = {
                    903127110.38  :  903139199.0,
                    939287916.08  :  939340799.0,
                    956949498.98  :  956966399.0,
                   1106217527.48  : 1106265599.0,
                   1142378333.18  : 1142380799.0,
                   1178539138.88  : 1178582399.0,
                   1227736721.78  : 1227743999.0,
                   1245398304.68  : 1245455999.0,
                   1299220693.28  : 1299283199.0,
                   1575472496.03  : 1575503999.0,
                   1579259661.83  : 1579305599.0,
                   1633919690.33  : 1633996799.0,
                   1683117273.23  : 1683158399.0,
                   1763850856.13  : 1763855999.0,
                   1908494078.93  : 1908575999.0,
                   1944654884.63  : 1944691199.0,
                   1962316467.53  : 1962316799.0,
                   2074586050.43  : 2074636799.0
                  }

#      print "\n\n"
      for item in sorted( test_data ):
         time_struct_time = time.gmtime(item)

#         print " first  /  second    %s" % ( self.te.truncate_any_time_to_last_epoch_of_day( item ) )

         for time_00 in [item, time_struct_time]:
            self.assertEqual( test_data[item], self.te.truncate_any_time_to_last_epoch_of_day( time_00 ) )


   def test_increment_day_to_next_occurrence_of_day_of_week(self):
      test_data = {
                     51655110.38    :  ['Fri',    52173510.38,    52173510],    #    'Sat'            6
                    109453137.239   :  ['Wed',   109453137.239,  109453137],    #    'Wed'            0
                    167251164.097   :  ['Thu',   167596764.097,  167596764],    #    'Sun'            4
                    225049190.956   :  ['Fri',   225135590.956,  225135590],    #    'Thu'            1
                    282847217.814   :  ['Sat',   283279217.814,  283279217],    #    'Mon'            5
                    340645244.673   :  ['Mon',   340904444.673,  340904444],    #    'Fri'            3
                    398443271.531   :  ['Fri',   398702471.531,  398702471],    #    'Tue'            3
                    456241298.39    :  ['Thu',   456673298.39,   456673298],    #    'Sat'            5
                    514039325.249   :  ['Sun',   514384925.249,  514384925],    #    'Wed'            4
                    571837352.107   :  ['Thu',   572182952.107,  572182952],    #    'Sun'            4
                    629635378.966   :  ['Tue',   630067378.966,  630067378],    #    'Thu'            5
                    687433405.824   :  ['Tue',   687519805.824,  687519805],    #    'Mon'            1
                    745231432.683   :  ['Sun',   745404232.683,  745404232],    #    'Fri'            2
                    803029459.541   :  ['Sat',   803375059.541,  803375059],    #    'Tue'            4
                    860827486.4     :  ['Wed',   861173086.4,    861173086],    #    'Fri'            5
                    918625513.259   :  ['Sat',   918884713.259,  918884713],    #    'Tue'            4
                    976423540.117   :  ['Mon',   976509940.117,  976509940],    #    'Sat'            2
                   1034221566.98    :  ['Mon',  1034567166.98,  1034567166],    #    'Wed'            5
                   1092019593.83    :  ['Tue',  1092105993.83,  1092105993],    #    'Sun'            2
                   1149817620.69    :  ['Mon',  1150076820.69,  1150076820],    #    'Thu'            4
                   1207615647.55    :  ['Thu',  1207788447.55,  1207788447],    #    'Mon'            3
                   1265413674.41    :  ['Thu',  1265932074.41,  1265932074],    #    'Fri'            6
                   1323211701.27    :  ['Sun',  1323643701.27,  1323643701],    #    'Tue'            5
                   1381009728.13    :  ['Wed',  1381355328.13,  1381355328],    #    'Sat'            4
                   1438807754.99    :  ['Mon',  1439239754.99,  1439239754],    #    'Wed'            5
                   1496605781.84    :  ['Fri',  1497037781.84,  1497037781],    #    'Sun'            5
                   1554403808.7     :  ['Wed',  1554922208.7,   1554922208],    #    'Thu'            6
                   1612201835.56    :  ['Sat',  1612633835.56,  1612633835],    #    'Mon'            5
                   1669999862.42    :  ['Sun',  1670172662.42,  1670172662],    #    'Fri'            2
                   1727797889.28    :  ['Sun',  1728229889.28,  1728229889],    #    'Tue'            5
                   1785595916.14    :  ['Wed',  1785941516.14,  1785941516],    #    'Sat'            4
                   1843393943.0     :  ['Tue',  1843912343.0,   1843912343],    #    'Wed'            6
                   1901191969.85    :  ['Fri',  1901623969.85,  1901623969],    #    'Sun'            5
                   1958989996.71    :  ['Tue',  1959421996.71,  1959421996],    #    'Thu'            5
                   2016788023.57    :  ['Sat',  2017220023.57,  2017220023]     #    'Mon'            5
                  }

      for item in sorted( test_data ):
         time_struct_time = time.gmtime(item)

#         print " first  /  second    %s,  %s" % ( self.te.increment_day_to_next_occurrence_of_day_of_week( item, test_data[item][0] ), self.te.increment_day_to_next_occurrence_of_day_of_week( calendar.timegm(time_struct_time), test_data[item][0] ) )

         self.assertEqual( test_data[item][1], self.te.increment_day_to_next_occurrence_of_day_of_week( item, test_data[item][0] ) )
         self.assertEqual( test_data[item][2], self.te.increment_day_to_next_occurrence_of_day_of_week( calendar.timegm(time_struct_time), test_data[item][0] ) )


   def test_get_the_integer_last_day_of_month(self):
      test_data = {
                     51655110.38    :  31,
                    109453137.239   :  30,
                    167251164.097   :  30,
                    225049190.956   :  28,
                    282847217.814   :  31,
                    340645244.673   :  31,
                    398443271.531   :  31,
                    456241298.39    :  30,
                    514039325.249   :  30,
                    571837352.107   :  29,
                    629635378.966   :  31,
                    687433405.824   :  31,
                    745231432.683   :  31,
                    803029459.541   :  30,
                    860827486.4     :  30,
                    918625513.259   :  28,
                    976423540.117   :  31,
                   1034221566.98    :  31,
                   1092019593.83    :  31,
                   1149817620.69    :  30,
                   1207615647.55    :  30,
                   1265413674.41    :  28,
                   1323211701.27    :  31,
                   1381009728.13    :  31,
                   1438807754.99    :  31,
                   1496605781.84    :  30,
                   1554403808.7     :  30,
                   1612201835.56    :  28,
                   1669999862.42    :  31,
                   1727797889.28    :  31,
                   1785595916.14    :  31,
                   1843393943.0     :  31,
                   1901191969.85    :  31,
                   1958989996.71    :  31,
                   2016788023.57    :  30
                  }

      for item in sorted( test_data ):
         time_struct_time = time.gmtime(item)
         self.assertEqual( test_data[item], self.te.get_the_integer_last_day_of_month( item ) )
         self.assertEqual( test_data[item], self.te.get_the_integer_last_day_of_month( calendar.timegm(time_struct_time) ) )


   def test_get_first_day_of_month(self):
      test_data = {
                     51655110.38   :  [  49927110.38,     'Sat Aug 21 20:38:30 1971',    'Sun Aug  1 20:38:30 1971'],
                    109453137.239  :  [ 107811537.239,    'Wed Jun 20 19:38:57 1973',    'Fri Jun  1 19:38:57 1973'],
                    167251164.097  :  [ 165609564.097,    'Sun Apr 20 18:39:24 1975',    'Tue Apr  1 18:39:24 1975'],
                    225049190.956  :  [ 223666790.956,    'Thu Feb 17 17:39:50 1977',    'Tue Feb  1 17:39:50 1977'],
                    282847217.814  :  [ 281378417.814,    'Mon Dec 18 16:40:17 1978',    'Fri Dec  1 16:40:17 1978'],
                    340645244.673  :  [ 339262844.673,    'Fri Oct 17 15:40:44 1980',    'Wed Oct  1 15:40:44 1980'],
                    398443271.531  :  [ 397060871.531,    'Tue Aug 17 14:41:11 1982',    'Sun Aug  1 14:41:11 1982'],
                    456241298.39   :  [ 454945298.39,     'Sat Jun 16 13:41:38 1984',    'Fri Jun  1 13:41:38 1984'],
                    514039325.249  :  [ 512743325.249,    'Wed Apr 16 12:42:05 1986',    'Tue Apr  1 12:42:05 1986'],
                    571837352.107  :  [ 570714152.107,    'Sun Feb 14 11:42:32 1988',    'Mon Feb  1 11:42:32 1988'],
                    629635378.966  :  [ 628512178.966,    'Thu Dec 14 10:42:58 1989',    'Fri Dec  1 10:42:58 1989'],
                    687433405.824  :  [ 686310205.824,    'Mon Oct 14 09:43:25 1991',    'Tue Oct  1 09:43:25 1991'],
                    745231432.683  :  [ 744194632.683,    'Fri Aug 13 08:43:52 1993',    'Sun Aug  1 08:43:52 1993'],
                    803029459.541  :  [ 801992659.541,    'Tue Jun 13 07:44:19 1995',    'Thu Jun  1 07:44:19 1995'],
                    860827486.4    :  [ 859877086.4,      'Sat Apr 12 06:44:46 1997',    'Tue Apr  1 06:44:46 1997'],
                    918625513.259  :  [ 917847913.259,    'Wed Feb 10 05:45:13 1999',    'Mon Feb  1 05:45:13 1999'],
                    976423540.117  :  [ 975645940.117,    'Sun Dec 10 04:45:40 2000',    'Fri Dec  1 04:45:40 2000'],
                   1034221566.98   :  [1033443966.98,     'Thu Oct 10 03:46:06 2002',    'Tue Oct  1 03:46:06 2002'],
                   1092019593.83   :  [1091328393.83,     'Mon Aug  9 02:46:33 2004',    'Sun Aug  1 02:46:33 2004'],
                   1149817620.69   :  [1149126420.69,     'Fri Jun  9 01:47:00 2006',    'Thu Jun  1 01:47:00 2006'],
                   1207615647.55   :  [1207010847.55,     'Tue Apr  8 00:47:27 2008',    'Tue Apr  1 00:47:27 2008'],
                   1265413674.41   :  [1265068074.41,     'Fri Feb  5 23:47:54 2010',    'Mon Feb  1 23:47:54 2010'],
                   1323211701.27   :  [1322779701.27,     'Tue Dec  6 22:48:21 2011',    'Thu Dec  1 22:48:21 2011'],
                   1381009728.13   :  [1380664128.13,     'Sat Oct  5 21:48:48 2013',    'Tue Oct  1 21:48:48 2013'],
                   1438807754.99   :  [1438462154.99,     'Wed Aug  5 20:49:14 2015',    'Sat Aug  1 20:49:14 2015'],
                   1496605781.84   :  [1496346581.84,     'Sun Jun  4 19:49:41 2017',    'Thu Jun  1 19:49:41 2017'],
                   1554403808.7    :  [1554144608.7,      'Thu Apr  4 18:50:08 2019',    'Mon Apr  1 18:50:08 2019'],
                   1612201835.56   :  [1612201835.56,     'Mon Feb  1 17:50:35 2021',    'Mon Feb  1 17:50:35 2021'],
                   1669999862.42   :  [1669913462.42,     'Fri Dec  2 16:51:02 2022',    'Thu Dec  1 16:51:02 2022'],
                   1727797889.28   :  [1727797889.28,     'Tue Oct  1 15:51:29 2024',    'Tue Oct  1 15:51:29 2024'],
                   1785595916.14   :  [1785595916.14,     'Sat Aug  1 14:51:56 2026',    'Sat Aug  1 14:51:56 2026'],
                   1843393943.0    :  [1840801943.0,      'Wed May 31 13:52:23 2028',    'Mon May  1 13:52:23 2028'],
                   1901191969.85   :  [1898599969.85,     'Sun Mar 31 12:52:49 2030',    'Fri Mar  1 12:52:49 2030'],
                   1958989996.71   :  [1956570796.71,     'Thu Jan 29 11:53:16 2032',    'Thu Jan  1 11:53:16 2032'],
                   2016788023.57   :  [2014455223.57,     'Mon Nov 28 10:53:43 2033',    'Tue Nov  1 10:53:43 2033']
                  }


      for data_list in sorted( test_data ):
         time_struct_time = time.gmtime(data_list)

         # Check with epoch time as input
         first_day_in_month = self.te.get_first_day_of_month( data_list )
#         print " first  /  second    '%s,  %s,  '%s'" % (first_day_in_month, time.asctime(time.gmtime(data_list)), time.asctime(time.gmtime(first_day_in_month)) )
         self.assertEqual( first_day_in_month,                            test_data[data_list][0] )
         self.assertEqual( time.asctime(time.gmtime(data_list)),          test_data[data_list][1] )
         self.assertEqual( time.asctime(time.gmtime(first_day_in_month)), test_data[data_list][2] )

         # Check with 'struct_time' object as input
         if round(test_data[data_list][0])  ==  int(test_data[data_list][0]):
            self.assertEqual( round(test_data[data_list][0]), self.te.get_first_day_of_month( calendar.timegm(time_struct_time) ) )
         else:
            self.assertEqual(   int(test_data[data_list][0]), self.te.get_first_day_of_month( calendar.timegm(time_struct_time) ) )


   def test_get_last_day_of_month(self):
      test_data = {
                     51655110.38   :  [  52519110,  'Sat Aug 21 20:38:30 1971',  'Tue Aug 31 20:38:30 1971'],
                    109453137.239  :  [ 110317137,  'Wed Jun 20 19:38:57 1973',  'Sat Jun 30 19:38:57 1973'],
                    167251164.097  :  [ 168115164,  'Sun Apr 20 18:39:24 1975',  'Wed Apr 30 18:39:24 1975'],
                    225049190.956  :  [ 225999590,  'Thu Feb 17 17:39:50 1977',  'Mon Feb 28 17:39:50 1977'],
                    282847217.814  :  [ 283970417,  'Mon Dec 18 16:40:17 1978',  'Sun Dec 31 16:40:17 1978'],
                    340645244.673  :  [ 341854844,  'Fri Oct 17 15:40:44 1980',  'Fri Oct 31 15:40:44 1980'],
                    398443271.531  :  [ 399652871,  'Tue Aug 17 14:41:11 1982',  'Tue Aug 31 14:41:11 1982'],
                    456241298.39   :  [ 457450898,  'Sat Jun 16 13:41:38 1984',  'Sat Jun 30 13:41:38 1984'],
                    514039325.249  :  [ 515248925,  'Wed Apr 16 12:42:05 1986',  'Wed Apr 30 12:42:05 1986'],
                    571837352.107  :  [ 573133352,  'Sun Feb 14 11:42:32 1988',  'Mon Feb 29 11:42:32 1988'],
                    629635378.966  :  [ 631104178,  'Thu Dec 14 10:42:58 1989',  'Sun Dec 31 10:42:58 1989'],
                    687433405.824  :  [ 688902205,  'Mon Oct 14 09:43:25 1991',  'Thu Oct 31 09:43:25 1991'],
                    745231432.683  :  [ 746786632,  'Fri Aug 13 08:43:52 1993',  'Tue Aug 31 08:43:52 1993'],
                    803029459.541  :  [ 804498259,  'Tue Jun 13 07:44:19 1995',  'Fri Jun 30 07:44:19 1995'],
                    860827486.4    :  [ 862382686,  'Sat Apr 12 06:44:46 1997',  'Wed Apr 30 06:44:46 1997'],
                    918625513.259  :  [ 920180713,  'Wed Feb 10 05:45:13 1999',  'Sun Feb 28 05:45:13 1999'],
                    976423540.117  :  [ 978237940,  'Sun Dec 10 04:45:40 2000',  'Sun Dec 31 04:45:40 2000'],
                   1034221566.98   :  [1036035966,  'Thu Oct 10 03:46:06 2002',  'Thu Oct 31 03:46:06 2002'],
                   1092019593.83   :  [1093920393,  'Mon Aug  9 02:46:33 2004',  'Tue Aug 31 02:46:33 2004'],
                   1149817620.69   :  [1151632020,  'Fri Jun  9 01:47:00 2006',  'Fri Jun 30 01:47:00 2006'],
                   1207615647.55   :  [1209516447,  'Tue Apr  8 00:47:27 2008',  'Wed Apr 30 00:47:27 2008'],
                   1265413674.41   :  [1267400874,  'Fri Feb  5 23:47:54 2010',  'Sun Feb 28 23:47:54 2010'],
                   1323211701.27   :  [1325371701,  'Tue Dec  6 22:48:21 2011',  'Sat Dec 31 22:48:21 2011'],
                   1381009728.13   :  [1383256128,  'Sat Oct  5 21:48:48 2013',  'Thu Oct 31 21:48:48 2013'],
                   1438807754.99   :  [1441054154,  'Wed Aug  5 20:49:14 2015',  'Mon Aug 31 20:49:14 2015'],
                   1496605781.84   :  [1498852181,  'Sun Jun  4 19:49:41 2017',  'Fri Jun 30 19:49:41 2017'],
                   1554403808.7    :  [1556650208,  'Thu Apr  4 18:50:08 2019',  'Tue Apr 30 18:50:08 2019'],
                   1612201835.56   :  [1614534635,  'Mon Feb  1 17:50:35 2021',  'Sun Feb 28 17:50:35 2021'],
                   1669999862.42   :  [1672505462,  'Fri Dec  2 16:51:02 2022',  'Sat Dec 31 16:51:02 2022'],
                   1727797889.28   :  [1730389889,  'Tue Oct  1 15:51:29 2024',  'Thu Oct 31 15:51:29 2024'],
                   1785595916.14   :  [1788187916,  'Sat Aug  1 14:51:56 2026',  'Mon Aug 31 14:51:56 2026'],
                   1843393943.0    :  [1843393943,  'Wed May 31 13:52:23 2028',  'Wed May 31 13:52:23 2028'],
                   1901191969.85   :  [1901191969,  'Sun Mar 31 12:52:49 2030',  'Sun Mar 31 12:52:49 2030'],
                   1958989996.71   :  [1959162796,  'Thu Jan 29 11:53:16 2032',  'Sat Jan 31 11:53:16 2032'],
                   2016788023.57   :  [2016960823,  'Mon Nov 28 10:53:43 2033',  'Wed Nov 30 10:53:43 2033']
                  }

      for data_list in sorted( test_data ):
         time_struct_time = time.gmtime(data_list)

         # Check with epoch time as input
         last_day_in_month = self.te.get_last_day_of_month( data_list )

#         print " first  /  second    %s,  '%s',  '%s'" % (last_day_in_month, time.asctime(time.gmtime(data_list)), time.asctime(time.gmtime(last_day_in_month)) )

         self.assertEqual( last_day_in_month,                            test_data[data_list][0] )
         self.assertEqual( time.asctime(time.gmtime(data_list)),         test_data[data_list][1] )
         self.assertEqual( time.asctime(time.gmtime(last_day_in_month)), test_data[data_list][2] )

         # Check with 'struct_time' object as input
         if round(test_data[data_list][0])  ==  int(test_data[data_list][0]):
            self.assertEqual( round(test_data[data_list][0]), self.te.get_last_day_of_month( calendar.timegm(time_struct_time) ) )
         else:
            self.assertEqual(   int(test_data[data_list][0]), self.te.get_last_day_of_month( calendar.timegm(time_struct_time) ) )


   def test_normalize_date_format(self):

      time_a_in_struct_time_format = time.gmtime()
      time_a_in_epoch_format       = calendar.timegm(time_a_in_struct_time_format)

      time_b_in_struct_time_format = time.gmtime()
      time_b_in_epoch_format       = calendar.timegm(time_b_in_struct_time_format)

      day_a = self.te.normalize_date_format(time_a_in_struct_time_format, time_b_in_struct_time_format)
      self.assertEqual( 'struct_time', day_a.__class__.__name__  )

      day_b = self.te.normalize_date_format(time_a_in_struct_time_format, time_b_in_epoch_format)
      self.assertEqual( 'int', day_b.__class__.__name__  )

      day_c = self.te.normalize_date_format(time_a_in_epoch_format, time_b_in_struct_time_format)
      self.assertEqual( 'struct_time', day_c.__class__.__name__  )

      day_d = self.te.normalize_date_format(time_a_in_epoch_format, time_b_in_epoch_format)
      self.assertEqual( 'int', day_d.__class__.__name__  )


   def test_get_day_of_current_month(self):

      test_data_xxx = {
                       109453137.239   :  {
                          1  :    ['Wed Jun 20 19:38:57 1973',    'Fri Jun  1 19:38:57 1973'],
                         14  :    ['Wed Jun 20 19:38:57 1973',    'Thu Jun 14 19:38:57 1973'],
                         27  :    ['Wed Jun 20 19:38:57 1973',    'Wed Jun 27 19:38:57 1973'],
                         28  :    ['Wed Jun 20 19:38:57 1973',    'Thu Jun 28 19:38:57 1973'],
                         29  :    ['Wed Jun 20 19:38:57 1973',    'Fri Jun 29 19:38:57 1973'],
                         30  :    ['Wed Jun 20 19:38:57 1973',    'Sat Jun 30 19:38:57 1973'],
                         31  :    ['Wed Jun 20 19:38:57 1973',    None],
                               },
                       225049190.956   :  {
                          1  :    ['Thu Feb 17 17:39:50 1977',    'Tue Feb  1 17:39:50 1977'],
                         14  :    ['Thu Feb 17 17:39:50 1977',    'Mon Feb 14 17:39:50 1977'],
                         27  :    ['Thu Feb 17 17:39:50 1977',    'Sun Feb 27 17:39:50 1977'],
                         28  :    ['Thu Feb 17 17:39:50 1977',    'Mon Feb 28 17:39:50 1977'],
                         29  :    ['Thu Feb 17 17:39:50 1977',    None],
                         30  :    ['Thu Feb 17 17:39:50 1977',    None],
                         31  :    ['Thu Feb 17 17:39:50 1977',    None],
                               },
                       282847217.814   :  {
                          1  :    ['Mon Dec 18 16:40:17 1978',    'Fri Dec  1 16:40:17 1978'],
                         14  :    ['Mon Dec 18 16:40:17 1978',    'Thu Dec 14 16:40:17 1978'],
                         27  :    ['Mon Dec 18 16:40:17 1978',    'Wed Dec 27 16:40:17 1978'],
                         28  :    ['Mon Dec 18 16:40:17 1978',    'Thu Dec 28 16:40:17 1978'],
                         29  :    ['Mon Dec 18 16:40:17 1978',    'Fri Dec 29 16:40:17 1978'],
                         30  :    ['Mon Dec 18 16:40:17 1978',    'Sat Dec 30 16:40:17 1978'],
                         31  :    ['Mon Dec 18 16:40:17 1978',    'Sun Dec 31 16:40:17 1978'],
                               },
                       571837352.107   :  {
                          1  :    ['Sun Feb 14 11:42:32 1988',    'Mon Feb  1 11:42:32 1988'],
                         14  :    ['Sun Feb 14 11:42:32 1988',    'Sun Feb 14 11:42:32 1988'],
                         27  :    ['Sun Feb 14 11:42:32 1988',    'Sat Feb 27 11:42:32 1988'],
                         28  :    ['Sun Feb 14 11:42:32 1988',    'Sun Feb 28 11:42:32 1988'],
                         29  :    ['Sun Feb 14 11:42:32 1988',    'Mon Feb 29 11:42:32 1988'],
                         30  :    ['Sun Feb 14 11:42:32 1988',    None],
                         31  :    ['Sun Feb 14 11:42:32 1988',    None],
                               },
                       918625513.259   :  {
                          1  :    ['Wed Feb 10 05:45:13 1999',    'Mon Feb  1 05:45:13 1999'],
                         14  :    ['Wed Feb 10 05:45:13 1999',    'Sun Feb 14 05:45:13 1999'],
                         27  :    ['Wed Feb 10 05:45:13 1999',    'Sat Feb 27 05:45:13 1999'],
                         28  :    ['Wed Feb 10 05:45:13 1999',    'Sun Feb 28 05:45:13 1999'],
                         29  :    ['Wed Feb 10 05:45:13 1999',    None],
                         30  :    ['Wed Feb 10 05:45:13 1999',    None],
                         31  :    ['Wed Feb 10 05:45:13 1999',    None],
                               },
                       1092019593.83   :  {
                          1  :    ['Mon Aug  9 02:46:33 2004',    'Sun Aug  1 02:46:33 2004'],
                         14  :    ['Mon Aug  9 02:46:33 2004',    'Sat Aug 14 02:46:33 2004'],
                         27  :    ['Mon Aug  9 02:46:33 2004',    'Fri Aug 27 02:46:33 2004'],
                         28  :    ['Mon Aug  9 02:46:33 2004',    'Sat Aug 28 02:46:33 2004'],
                         29  :    ['Mon Aug  9 02:46:33 2004',    'Sun Aug 29 02:46:33 2004'],
                         30  :    ['Mon Aug  9 02:46:33 2004',    'Mon Aug 30 02:46:33 2004'],
                         31  :    ['Mon Aug  9 02:46:33 2004',    'Tue Aug 31 02:46:33 2004'],
                               },
                       1207615647.55   :  {
                          1  :    ['Tue Apr  8 00:47:27 2008',    'Tue Apr  1 00:47:27 2008'],
                         14  :    ['Tue Apr  8 00:47:27 2008',    'Mon Apr 14 00:47:27 2008'],
                         27  :    ['Tue Apr  8 00:47:27 2008',    'Sun Apr 27 00:47:27 2008'],
                         28  :    ['Tue Apr  8 00:47:27 2008',    'Mon Apr 28 00:47:27 2008'],
                         29  :    ['Tue Apr  8 00:47:27 2008',    'Tue Apr 29 00:47:27 2008'],
                         30  :    ['Tue Apr  8 00:47:27 2008',    'Wed Apr 30 00:47:27 2008'],
                         31  :    ['Tue Apr  8 00:47:27 2008',    None],
                               },
                       1265413674.41   :  {
                          1  :    ['Fri Feb  5 23:47:54 2010',    'Mon Feb  1 23:47:54 2010'],
                         14  :    ['Fri Feb  5 23:47:54 2010',    'Sun Feb 14 23:47:54 2010'],
                         27  :    ['Fri Feb  5 23:47:54 2010',    'Sat Feb 27 23:47:54 2010'],
                         28  :    ['Fri Feb  5 23:47:54 2010',    'Sun Feb 28 23:47:54 2010'],
                         29  :    ['Fri Feb  5 23:47:54 2010',    None],
                         30  :    ['Fri Feb  5 23:47:54 2010',    None],
                         31  :    ['Fri Feb  5 23:47:54 2010',    None],
                               },
                       1612201835.56   :  {
                          1  :    ['Mon Feb  1 17:50:35 2021',    'Mon Feb  1 17:50:35 2021'],
                         14  :    ['Mon Feb  1 17:50:35 2021',    'Sun Feb 14 17:50:35 2021'],
                         27  :    ['Mon Feb  1 17:50:35 2021',    'Sat Feb 27 17:50:35 2021'],
                         28  :    ['Mon Feb  1 17:50:35 2021',    'Sun Feb 28 17:50:35 2021'],
                         29  :    ['Mon Feb  1 17:50:35 2021',    None],
                         30  :    ['Mon Feb  1 17:50:35 2021',    None],
                         31  :    ['Mon Feb  1 17:50:35 2021',    None],
                               },
                       1727797889.28   :  {
                          1  :    ['Tue Oct  1 15:51:29 2024',    'Tue Oct  1 15:51:29 2024'],
                         14  :    ['Tue Oct  1 15:51:29 2024',    'Mon Oct 14 15:51:29 2024'],
                         27  :    ['Tue Oct  1 15:51:29 2024',    'Sun Oct 27 15:51:29 2024'],
                         28  :    ['Tue Oct  1 15:51:29 2024',    'Mon Oct 28 15:51:29 2024'],
                         29  :    ['Tue Oct  1 15:51:29 2024',    'Tue Oct 29 15:51:29 2024'],
                         30  :    ['Tue Oct  1 15:51:29 2024',    'Wed Oct 30 15:51:29 2024'],
                         31  :    ['Tue Oct  1 15:51:29 2024',    'Thu Oct 31 15:51:29 2024'],
                               },
                       1843393943.0   :  {
                          1  :    ['Wed May 31 13:52:23 2028',    'Mon May  1 13:52:23 2028'],
                         14  :    ['Wed May 31 13:52:23 2028',    'Sun May 14 13:52:23 2028'],
                         27  :    ['Wed May 31 13:52:23 2028',    'Sat May 27 13:52:23 2028'],
                         28  :    ['Wed May 31 13:52:23 2028',    'Sun May 28 13:52:23 2028'],
                         29  :    ['Wed May 31 13:52:23 2028',    'Mon May 29 13:52:23 2028'],
                         30  :    ['Wed May 31 13:52:23 2028',    'Tue May 30 13:52:23 2028'],
                         31  :    ['Wed May 31 13:52:23 2028',    'Wed May 31 13:52:23 2028'],
                               },
                       1901191969.85   :  {
                          1  :    ['Sun Mar 31 12:52:49 2030',    'Fri Mar  1 12:52:49 2030'],
                         14  :    ['Sun Mar 31 12:52:49 2030',    'Thu Mar 14 12:52:49 2030'],
                         27  :    ['Sun Mar 31 12:52:49 2030',    'Wed Mar 27 12:52:49 2030'],
                         28  :    ['Sun Mar 31 12:52:49 2030',    'Thu Mar 28 12:52:49 2030'],
                         29  :    ['Sun Mar 31 12:52:49 2030',    'Fri Mar 29 12:52:49 2030'],
                         30  :    ['Sun Mar 31 12:52:49 2030',    'Sat Mar 30 12:52:49 2030'],
                         31  :    ['Sun Mar 31 12:52:49 2030',    'Sun Mar 31 12:52:49 2030'],
                               },
                       1958989996.71   :  {
                          1  :    ['Thu Jan 29 11:53:16 2032',    'Thu Jan  1 11:53:16 2032'],
                         14  :    ['Thu Jan 29 11:53:16 2032',    'Wed Jan 14 11:53:16 2032'],
                         27  :    ['Thu Jan 29 11:53:16 2032',    'Tue Jan 27 11:53:16 2032'],
                         28  :    ['Thu Jan 29 11:53:16 2032',    'Wed Jan 28 11:53:16 2032'],
                         29  :    ['Thu Jan 29 11:53:16 2032',    'Thu Jan 29 11:53:16 2032'],
                         30  :    ['Thu Jan 29 11:53:16 2032',    'Fri Jan 30 11:53:16 2032'],
                         31  :    ['Thu Jan 29 11:53:16 2032',    'Sat Jan 31 11:53:16 2032'],
                               },
                       2016788023.57   :  {
                          1  :    ['Mon Nov 28 10:53:43 2033',    'Tue Nov  1 10:53:43 2033'],
                         14  :    ['Mon Nov 28 10:53:43 2033',    'Mon Nov 14 10:53:43 2033'],
                         27  :    ['Mon Nov 28 10:53:43 2033',    'Sun Nov 27 10:53:43 2033'],
                         28  :    ['Mon Nov 28 10:53:43 2033',    'Mon Nov 28 10:53:43 2033'],
                         29  :    ['Mon Nov 28 10:53:43 2033',    'Tue Nov 29 10:53:43 2033'],
                         30  :    ['Mon Nov 28 10:53:43 2033',    'Wed Nov 30 10:53:43 2033'],
                         31  :    ['Mon Nov 28 10:53:43 2033',    None],
                               },
                       }

      for epoch_time in sorted( test_data_xxx ):
         data_list = test_data_xxx[epoch_time]
         for dom in test_data_xxx[epoch_time]:

            day_a = self.te.get_day_of_current_month(epoch_time, dom)
            self.assertEqual( time.asctime(time.gmtime(epoch_time)), test_data_xxx[epoch_time][dom][0] )
            if not day_a:
               self.assertEqual( day_a,             test_data_xxx[epoch_time][dom][1] )
            else:
               self.assertEqual( time.asctime(time.gmtime(day_a)), test_data_xxx[epoch_time][dom][1] )


   def test_get_first_day_of_quarter(self):
      test_data = {
                      51655110.38   :  ['Sat Aug 21 20:38:30 1971',  'Thu Jul  1 20:38:30 1971'],
                     109453137.239  :  ['Wed Jun 20 19:38:57 1973',  'Sun Apr  1 19:38:57 1973'],
                     167251164.097  :  ['Sun Apr 20 18:39:24 1975',  'Tue Apr  1 18:39:24 1975'],
                     225049190.956  :  ['Thu Feb 17 17:39:50 1977',  'Sat Jan  1 17:39:50 1977'],
                     282847217.814  :  ['Mon Dec 18 16:40:17 1978',  'Sun Oct  1 16:40:17 1978'],
                     340645244.673  :  ['Fri Oct 17 15:40:44 1980',  'Wed Oct  1 15:40:44 1980'],
                     398443271.531  :  ['Tue Aug 17 14:41:11 1982',  'Thu Jul  1 14:41:11 1982'],
                     456241298.39   :  ['Sat Jun 16 13:41:38 1984',  'Sun Apr  1 13:41:38 1984'],
                     514039325.249  :  ['Wed Apr 16 12:42:05 1986',  'Tue Apr  1 12:42:05 1986'],
                     571837352.107  :  ['Sun Feb 14 11:42:32 1988',  'Fri Jan  1 11:42:32 1988'],
                     629635378.966  :  ['Thu Dec 14 10:42:58 1989',  'Sun Oct  1 10:42:58 1989'],
                     687433405.824  :  ['Mon Oct 14 09:43:25 1991',  'Tue Oct  1 09:43:25 1991'],
                     745231432.683  :  ['Fri Aug 13 08:43:52 1993',  'Thu Jul  1 08:43:52 1993'],
                     803029459.541  :  ['Tue Jun 13 07:44:19 1995',  'Sat Apr  1 07:44:19 1995'],
                     860827486.4    :  ['Sat Apr 12 06:44:46 1997',  'Tue Apr  1 06:44:46 1997'],
                     918625513.259  :  ['Wed Feb 10 05:45:13 1999',  'Fri Jan  1 05:45:13 1999'],
                     976423540.117  :  ['Sun Dec 10 04:45:40 2000',  'Sun Oct  1 04:45:40 2000'],
                    1034221566.98   :  ['Thu Oct 10 03:46:06 2002',  'Tue Oct  1 03:46:06 2002'],
                    1092019593.83   :  ['Mon Aug  9 02:46:33 2004',  'Thu Jul  1 02:46:33 2004'],
                    1149817620.69   :  ['Fri Jun  9 01:47:00 2006',  'Sat Apr  1 01:47:00 2006'],
                    1207615647.55   :  ['Tue Apr  8 00:47:27 2008',  'Tue Apr  1 00:47:27 2008'],
                    1265413674.41   :  ['Fri Feb  5 23:47:54 2010',  'Fri Jan  1 23:47:54 2010'],
                    1323211701.27   :  ['Tue Dec  6 22:48:21 2011',  'Sat Oct  1 22:48:21 2011'],
                    1381009728.13   :  ['Sat Oct  5 21:48:48 2013',  'Tue Oct  1 21:48:48 2013'],
                    1438807754.99   :  ['Wed Aug  5 20:49:14 2015',  'Wed Jul  1 20:49:14 2015'],
                    1496605781.84   :  ['Sun Jun  4 19:49:41 2017',  'Sat Apr  1 19:49:41 2017'],
                    1554403808.7    :  ['Thu Apr  4 18:50:08 2019',  'Mon Apr  1 18:50:08 2019'],
                    1612201835.56   :  ['Mon Feb  1 17:50:35 2021',  'Fri Jan  1 17:50:35 2021'],
                    1669999862.42   :  ['Fri Dec  2 16:51:02 2022',  'Sat Oct  1 16:51:02 2022'],
                    1727797889.28   :  ['Tue Oct  1 15:51:29 2024',  'Tue Oct  1 15:51:29 2024'],
                    1785595916.14   :  ['Sat Aug  1 14:51:56 2026',  'Wed Jul  1 14:51:56 2026'],
                    1843393943.0    :  ['Wed May 31 13:52:23 2028',  'Sat Apr  1 13:52:23 2028'],
                    1901191969.85   :  ['Sun Mar 31 12:52:49 2030',  'Tue Jan  1 12:52:49 2030'],
                    1958989996.71   :  ['Thu Jan 29 11:53:16 2032',  'Thu Jan  1 11:53:16 2032'],
                    2016788023.57   :  ['Mon Nov 28 10:53:43 2033',  'Sat Oct  1 10:53:43 2033']
                  }

      for data_list in sorted( test_data ):
         # Check with epoch time as input
         last_day_in_quarter = self.te.get_first_day_of_quarter( data_list )
#         print " first  /  second    '%s,  %s" % (time.asctime(time.gmtime( data_list )), time.asctime(time.gmtime( last_day_in_quarter )) )

         self.assertEqual( time.asctime(time.gmtime( data_list )),           test_data[data_list][0] )
         self.assertEqual( time.asctime(time.gmtime( last_day_in_quarter )), test_data[data_list][1] )

         # Check with 'struct_time' object as input
         last_day_in_quarter = self.te.get_first_day_of_quarter( time.gmtime(data_list) )
         self.assertEqual( time.asctime(time.gmtime( calendar.timegm(last_day_in_quarter) )), test_data[data_list][1] )


   def test_get_last_day_of_quarter(self):
      test_data = {
                      51655110.38   :  ['Sat Aug 21 20:38:30 1971',  'Thu Sep 30 20:38:30 1971'],
                     109453137.239  :  ['Wed Jun 20 19:38:57 1973',  'Sat Jun 30 19:38:57 1973'],
                     167251164.097  :  ['Sun Apr 20 18:39:24 1975',  'Mon Jun 30 18:39:24 1975'],
                     225049190.956  :  ['Thu Feb 17 17:39:50 1977',  'Thu Mar 31 17:39:50 1977'],
                     282847217.814  :  ['Mon Dec 18 16:40:17 1978',  'Sun Dec 31 16:40:17 1978'],
                     340645244.673  :  ['Fri Oct 17 15:40:44 1980',  'Wed Dec 31 15:40:44 1980'],
                     398443271.531  :  ['Tue Aug 17 14:41:11 1982',  'Thu Sep 30 14:41:11 1982'],
                     456241298.39   :  ['Sat Jun 16 13:41:38 1984',  'Sat Jun 30 13:41:38 1984'],
                     514039325.249  :  ['Wed Apr 16 12:42:05 1986',  'Mon Jun 30 12:42:05 1986'],
                     571837352.107  :  ['Sun Feb 14 11:42:32 1988',  'Thu Mar 31 11:42:32 1988'],
                     629635378.966  :  ['Thu Dec 14 10:42:58 1989',  'Sun Dec 31 10:42:58 1989'],
                     687433405.824  :  ['Mon Oct 14 09:43:25 1991',  'Tue Dec 31 09:43:25 1991'],
                     745231432.683  :  ['Fri Aug 13 08:43:52 1993',  'Thu Sep 30 08:43:52 1993'],
                     803029459.541  :  ['Tue Jun 13 07:44:19 1995',  'Fri Jun 30 07:44:19 1995'],
                     860827486.4    :  ['Sat Apr 12 06:44:46 1997',  'Mon Jun 30 06:44:46 1997'],
                     918625513.259  :  ['Wed Feb 10 05:45:13 1999',  'Wed Mar 31 05:45:13 1999'],
                     976423540.117  :  ['Sun Dec 10 04:45:40 2000',  'Sun Dec 31 04:45:40 2000'],
                    1034221566.98   :  ['Thu Oct 10 03:46:06 2002',  'Tue Dec 31 03:46:06 2002'],
                    1092019593.83   :  ['Mon Aug  9 02:46:33 2004',  'Thu Sep 30 02:46:33 2004'],
                    1149817620.69   :  ['Fri Jun  9 01:47:00 2006',  'Fri Jun 30 01:47:00 2006'],
                    1207615647.55   :  ['Tue Apr  8 00:47:27 2008',  'Mon Jun 30 00:47:27 2008'],
                    1265413674.41   :  ['Fri Feb  5 23:47:54 2010',  'Wed Mar 31 23:47:54 2010'],
                    1323211701.27   :  ['Tue Dec  6 22:48:21 2011',  'Sat Dec 31 22:48:21 2011'],
                    1381009728.13   :  ['Sat Oct  5 21:48:48 2013',  'Tue Dec 31 21:48:48 2013'],
                    1438807754.99   :  ['Wed Aug  5 20:49:14 2015',  'Wed Sep 30 20:49:14 2015'],
                    1496605781.84   :  ['Sun Jun  4 19:49:41 2017',  'Fri Jun 30 19:49:41 2017'],
                    1554403808.7    :  ['Thu Apr  4 18:50:08 2019',  'Sun Jun 30 18:50:08 2019'],
                    1612201835.56   :  ['Mon Feb  1 17:50:35 2021',  'Wed Mar 31 17:50:35 2021'],
                    1669999862.42   :  ['Fri Dec  2 16:51:02 2022',  'Sat Dec 31 16:51:02 2022'],
                    1727797889.28   :  ['Tue Oct  1 15:51:29 2024',  'Tue Dec 31 15:51:29 2024'],
                    1785595916.14   :  ['Sat Aug  1 14:51:56 2026',  'Wed Sep 30 14:51:56 2026'],
                    1843393943.0    :  ['Wed May 31 13:52:23 2028',  'Fri Jun 30 13:52:23 2028'],
                    1901191969.85   :  ['Sun Mar 31 12:52:49 2030',  'Sun Mar 31 12:52:49 2030'],
                    1958989996.71   :  ['Thu Jan 29 11:53:16 2032',  'Wed Mar 31 11:53:16 2032'],
                    2016788023.57   :  ['Mon Nov 28 10:53:43 2033',  'Sat Dec 31 10:53:43 2033']
                  }

      for data_list in sorted( test_data ):
         # Check with epoch time as input
         last_day_in_quarter = self.te.get_last_day_of_quarter( data_list )


#         print " first  /  second    '%s',  '%s'" % ( time.asctime(time.gmtime(data_list)), time.asctime(time.gmtime( last_day_in_quarter )) )


         self.assertEqual( time.asctime(time.gmtime(data_list)),              test_data[data_list][0] )
         self.assertEqual( time.asctime(time.gmtime( last_day_in_quarter )),  test_data[data_list][1] )

         # Check with 'struct_time' object as input
         last_day_in_quarter = self.te.get_last_day_of_quarter( time.gmtime(data_list) )
         self.assertEqual( time.asctime(time.gmtime( calendar.timegm(last_day_in_quarter) )), test_data[data_list][1] )


   def test_set_date_timeofday_to_reference(self):

      time_baseline = 1034221566.98

      for time_factor in [ 45.3423, 0.675, 77.1077, 32.5, 53.47945]:
         for sign_factor in [ -1, 1 ]:


            # time_0 is in epoch seconds format
            # time_n is in epoch seconds format
            time_0 = time_baseline
            time_n = time_0 + self.seconds_per_day * time_factor * sign_factor
            self.assertNotEqual( time_0, time_n )
            num_days_different = self.te.difference_of_days(time_n, time_0)
            incremented_time = self.te.increment_day_by_n_days(time_0, num_days_different)
            self.assertEqual(    0, self.te.difference_of_days(incremented_time, time_n) )
            self.assertNotEqual( incremented_time, time_n )
            new_epoch_02 = self.te.set_date_timeofday_to_reference(incremented_time, time_n)
            self.assertEqual(    new_epoch_02, time_n )


            # time_0 is in 'struct_time' object format
            # time_n is in epoch seconds format
            time_0 = time.gmtime(time_baseline)
            time_n = calendar.timegm(time_0) + self.seconds_per_day * time_factor * sign_factor
            self.assertNotEqual( calendar.timegm(time_0), time_n )
            num_days_different = self.te.difference_of_days(time_n, calendar.timegm(time_0))
            incremented_time = self.te.increment_day_by_n_days(calendar.timegm(time_0), num_days_different)
            self.assertEqual(    0, self.te.difference_of_days(incremented_time, time_n) )
            self.assertNotEqual( incremented_time, time_n )
            new_epoch_02 = self.te.set_date_timeofday_to_reference(incremented_time, time_n)
            self.assertEqual(    new_epoch_02, time_n )


            # time_0 is in epoch seconds format
            # time_n is in 'struct_time' object format
            time_0 = time_baseline
            time_n = time.gmtime(time_0 + self.seconds_per_day * time_factor * sign_factor)
            self.assertNotEqual( time_0, calendar.timegm(time_n) )
            num_days_different = self.te.difference_of_days(calendar.timegm(time_n), time_0)
            incremented_time = self.te.increment_day_by_n_days(time_0, num_days_different)
            self.assertEqual(    0, self.te.difference_of_days(incremented_time, calendar.timegm(time_n)) )
            self.assertNotEqual( incremented_time, calendar.timegm(time_n) )
            new_epoch_02 = self.te.set_date_timeofday_to_reference(incremented_time, calendar.timegm(time_n))
            self.assertEqual(    new_epoch_02, calendar.timegm(time_n) )


            # time_0 is in 'struct_time' object format
            # time_n is in 'struct_time' object format
            time_0 = time.gmtime(time_baseline)
            time_n = time.gmtime(calendar.timegm(time_0) + self.seconds_per_day * time_factor * sign_factor)
            self.assertNotEqual( calendar.timegm(time_0), calendar.timegm(time_n) )
            num_days_different = self.te.difference_of_days(calendar.timegm(time_n), calendar.timegm(time_0))
            incremented_time = self.te.increment_day_by_n_days(calendar.timegm(time_0), num_days_different)
            self.assertEqual(    0, self.te.difference_of_days(incremented_time, calendar.timegm(time_n)) )
            self.assertNotEqual( incremented_time, calendar.timegm(time_n) )
            new_epoch_02 = self.te.set_date_timeofday_to_reference(incremented_time, calendar.timegm(time_n))
            self.assertEqual(    new_epoch_02, calendar.timegm(time_n) )

      # Zero date differences
      for time_factor in [ 0.0 ]:
         for sign_factor in [ -1, 1 ]:


            # time_0 is in epoch seconds format
            # time_n is in epoch seconds format
            time_0 = time_baseline
            time_n = time_0 + self.seconds_per_day * time_factor * sign_factor
            self.assertEqual( time_0, time_n )
            num_days_different = self.te.difference_of_days(time_n, time_0)
            incremented_time = self.te.increment_day_by_n_days(time_0, num_days_different)
            self.assertEqual(    0, self.te.difference_of_days(incremented_time, time_n) )
            self.assertEqual( incremented_time, time_n )
            new_epoch_02 = self.te.set_date_timeofday_to_reference(incremented_time, time_n)
            self.assertEqual(    new_epoch_02, time_n )

      for time_factor in [ 1.0, -1.0]:
         for sign_factor in [ -1, 1 ]:

            if time_factor == sign_factor:
               # time_0 is in epoch seconds format
               # time_n is in epoch seconds format
               time_0 = time_baseline
               time_n = time_0 + self.seconds_per_day * time_factor * sign_factor
               self.assertNotEqual( time_0, time_n )
               num_days_different = self.te.difference_of_days(time_n, time_0)
               incremented_time = self.te.increment_day_by_n_days(time_0, num_days_different)
               self.assertEqual(    0, self.te.difference_of_days(incremented_time, time_n) )
               self.assertEqual( incremented_time, time_n )
               new_epoch_02 = self.te.set_date_timeofday_to_reference(incremented_time, time_n)
               self.assertEqual(    new_epoch_02, time_n )

         # Times differ by EXACTLY one day in both directions
         # time_0 is in epoch seconds format
         # time_n is in epoch seconds format
         time_0 = time_baseline
         time_n = time_0 + self.seconds_per_day * time_factor
         self.assertNotEqual( time_0, time_n )
         num_days_different = self.te.difference_of_days(time_n, time_0)
         incremented_time = self.te.increment_day_by_n_days(time_0, num_days_different)
         self.assertEqual(    0, self.te.difference_of_days(incremented_time, time_n) )
         self.assertEqual( incremented_time, time_n )
         new_epoch_02 = self.te.set_date_timeofday_to_reference(incremented_time, time_n)
         self.assertEqual(    new_epoch_02, time_n )


   def test_date_to_epoch(self):

      test_data_float = {
                     803029459.0  :  'Tue Jun 13 00:44:19 1995',
                     860827486.0  :  'Fri Apr 11 23:44:46 1997',
                     918625513.0  :  'Tue Feb  9 21:45:13 1999',
                     976423540.0  :  'Sat Dec  9 20:45:40 2000',
                    1034221566.0  :  'Wed Oct  9 20:46:06 2002',
                    1092019593.0  :  'Sun Aug  8 19:46:33 2004',
                    1265413674.0  :  'Fri Feb  5 15:47:54 2010',
                    1323211701.0  :  'Tue Dec  6 14:48:21 2011',
                    1438807754.0  :  'Wed Aug  5 13:49:14 2015'
                  }

      test_data_str = {
                       '1381009728.0'  :  'Sat Oct  5 14:48:48 2013'
                      }

      for epoch_time in test_data_float:
         struct_time_obj = time.gmtime(epoch_time)
         self.assertEqual(      epoch_time.__class__.__name__, 'float'       )
         self.assertEqual( struct_time_obj.__class__.__name__, 'struct_time' )

         date_from_epoch       = self.te.date_to_epoch(epoch_time)
         date_from_struct_time = self.te.date_to_epoch(struct_time_obj)

         self.assertEqual(       date_from_epoch.__class__.__name__, 'float' )
         self.assertEqual( date_from_struct_time.__class__.__name__, 'int' )

         self.assertEqual( epoch_time, date_from_epoch )
         self.assertEqual( epoch_time, date_from_struct_time )

      for epoch_time in test_data_str:
         struct_time_obj = time.gmtime(float(epoch_time))
         self.assertEqual(      epoch_time.__class__.__name__, 'str'         )
         self.assertEqual( struct_time_obj.__class__.__name__, 'struct_time' )

         date_from_epoch       = self.te.date_to_epoch(epoch_time)
         date_from_struct_time = self.te.date_to_epoch(struct_time_obj)

         self.assertEqual(       date_from_epoch.__class__.__name__, 'str'   )
         self.assertEqual( date_from_struct_time.__class__.__name__, 'int' )

         self.assertEqual( epoch_time,        date_from_epoch )
         self.assertEqual( float(epoch_time), date_from_struct_time )


   def test_date_to_struct_time(self):

      test_data_float = {
                     803029459.0  :  'Tue Jun 13 00:44:19 1995',
                     860827486.0  :  'Fri Apr 11 23:44:46 1997',
                     918625513.0  :  'Tue Feb  9 21:45:13 1999',
                     976423540.0  :  'Sat Dec  9 20:45:40 2000',
                    1034221566.0  :  'Wed Oct  9 20:46:06 2002',
                    1092019593.0  :  'Sun Aug  8 19:46:33 2004',
                    1265413674.0  :  'Fri Feb  5 15:47:54 2010',
                    1323211701.0  :  'Tue Dec  6 14:48:21 2011',
                    1438807754.0  :  'Wed Aug  5 13:49:14 2015'
                  }

      test_data_str = {
                    '1381009728.0'  :  'Sat Oct  5 14:48:48 2013'
                  }

      for epoch_time in test_data_float:
         struct_time_obj = time.gmtime(epoch_time)
         self.assertEqual(      epoch_time.__class__.__name__, 'float'       )
         self.assertEqual( struct_time_obj.__class__.__name__, 'struct_time' )

         date_from_epoch       = self.te.date_to_struct_time(epoch_time)
         date_from_struct_time = self.te.date_to_struct_time(struct_time_obj)

         self.assertEqual(       date_from_epoch.__class__.__name__, 'struct_time' )
         self.assertEqual( date_from_struct_time.__class__.__name__, 'struct_time' )

         self.assertEqual( time.gmtime(epoch_time), date_from_epoch )
         self.assertEqual( time.gmtime(epoch_time), date_from_struct_time )

      for epoch_time in test_data_str:
         struct_time_obj = time.gmtime(float(epoch_time))
         self.assertEqual(      epoch_time.__class__.__name__, 'str'         )
         self.assertEqual( struct_time_obj.__class__.__name__, 'struct_time' )

         date_from_epoch       = self.te.date_to_struct_time(epoch_time)
         date_from_struct_time = self.te.date_to_struct_time(struct_time_obj)

         self.assertEqual(       date_from_epoch.__class__.__name__, 'struct_time' )
         self.assertEqual( date_from_struct_time.__class__.__name__, 'struct_time' )

         self.assertEqual( time.gmtime(float(epoch_time)), date_from_epoch )
         self.assertEqual( time.gmtime(float(epoch_time)), date_from_struct_time )


   def test_date_to_datestring(self):

      test_data_float = {
                      803029459.0   :  'Tue Jun 13 07:44:19 1995',   # Date Stings are in UTC (GMT)
                      860827486.0   :  'Sat Apr 12 06:44:46 1997',   # Date Stings are in UTC (GMT)
                      918625513.0   :  'Wed Feb 10 05:45:13 1999',   # Date Stings are in UTC (GMT)
                      976423540.0   :  'Sun Dec 10 04:45:40 2000',   # Date Stings are in UTC (GMT)
                     1034221566.0   :  'Thu Oct 10 03:46:06 2002',   # Date Stings are in UTC (GMT)
                     1092019593.0   :  'Mon Aug  9 02:46:33 2004',   # Date Stings are in UTC (GMT)
                     1265413674.0   :  'Fri Feb  5 23:47:54 2010',   # Date Stings are in UTC (GMT)
                     1323211701.0   :  'Tue Dec  6 22:48:21 2011',   # Date Stings are in UTC (GMT)
                     1438807754.0   :  'Wed Aug  5 20:49:14 2015'    # Date Stings are in UTC (GMT)
                  }

      test_data_str = {
                       '1381009728.0'  :  'Sat Oct  5 21:48:48 2013'
                      }

      for epoch_time in sorted( test_data_float ):
         struct_time_obj = time.gmtime(epoch_time)
         self.assertEqual(      epoch_time.__class__.__name__, 'float'       )
         self.assertEqual( struct_time_obj.__class__.__name__, 'struct_time' )

         date_from_epoch       = self.te.date_to_datestring(epoch_time)
         date_from_struct_time = self.te.date_to_datestring(struct_time_obj)

         self.assertEqual(       date_from_epoch.__class__.__name__, 'str' )
         self.assertEqual( date_from_struct_time.__class__.__name__, 'str' )

         self.assertEqual( test_data_float[epoch_time], date_from_epoch )
         self.assertEqual( test_data_float[epoch_time], date_from_struct_time )

      for epoch_time in sorted( test_data_str ):
         struct_time_obj = time.gmtime(float(epoch_time))
         self.assertEqual(      epoch_time.__class__.__name__, 'str'         )
         self.assertEqual( struct_time_obj.__class__.__name__, 'struct_time' )

         date_from_epoch       = self.te.date_to_datestring(epoch_time)
         date_from_struct_time = self.te.date_to_datestring(struct_time_obj)

         self.assertEqual(       date_from_epoch.__class__.__name__, 'str' )
         self.assertEqual( date_from_struct_time.__class__.__name__, 'str' )

         self.assertEqual( test_data_str[epoch_time], date_from_epoch )
         self.assertEqual( test_data_str[epoch_time], date_from_struct_time )






#generate_backup_times



   def tearDown(self):
      pass



def suite():
   suite=unittest.TestLoader().loadTestsFromTestCase(Test_xxx)
   suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_yyy))
   return suite


suite=unittest.TestLoader().loadTestsFromTestCase(Test_xxx)
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_yyy))



unittest.TextTestRunner(verbosity=2).run(suite)
