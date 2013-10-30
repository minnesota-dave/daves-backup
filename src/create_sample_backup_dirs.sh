#!/bin/bash


overwrite_existing_backups="NO"

if [[ -n "$1" ]]
then
   if [ $1 = "overwrite" ];
   then
#      echo "yesssss"
      overwrite_existing_backups="YES"
#   else
#      echo " NOOOOOOOOOOO"
   fi
fi



#echo
#if [ $overwrite_existing_backups = "YES" ];
#then
#   echo "yesssss"
#else
#   echo "HECK NOT"
#fi
#echo





#mkdir -p  1380002347/1380002347_full/1380002347_backup
#touch     1380002347/1380002347_full/1380002347_backup/1380002347.tar.gz.gpg
#touch     1380002347/1380002347_full/1380002347_backup_report.txt


#mkdir -p  1380002347/1380009997_incremental/1380009997_backup
#touch     1380002347/1380009997_incremental/1380009997_backup/1380009997.tar.gz.gpg
#touch     1380002347/1380009997_incremental/1380009997_backup_report.txt



files=(
       1034221566
       1092019593
       1149817620
       1207615647
       1265413674
      )

dir_base='/home/david/local_backup'
let "first_epoch=1034221566"
let "seconds_per_day=60*60*24"
let "days_between_full_backups=7*${seconds_per_day}"

echo
let "current_full_epoch=first_epoch"
#for i in "${files[@]}"
for jjj in 1 2 3
do

   echo
   if [ $overwrite_existing_backups = "YES" ];
   then
      rm -rf  ${dir_base}/${current_full_epoch}
      echo "Dir deleted and to be recreated:   ${dir_base}/${current_full_epoch}"
   fi

   # Full backup
   echo
   echo  "FULL backup    ${current_full_epoch}"
   mkdir -p  ${dir_base}/${current_full_epoch}/${current_full_epoch}_full/${current_full_epoch}_backup
   touch     ${dir_base}/${current_full_epoch}/${current_full_epoch}_full/${current_full_epoch}_backup/${current_full_epoch}.tar.gz.gpg
   touch     ${dir_base}/${current_full_epoch}/${current_full_epoch}_full/${current_full_epoch}_backup_report.txt

   let "all_increments_offset=0"
   for ccc in 1 2 3
   do
      let "offset=$ccc*${seconds_per_day}"
      let "epoch=${current_full_epoch}+$offset"
      echo  "   incremental backup  count / epoch    ${ccc} / ${epoch}"

      # Incremental backup
      mkdir -p  ${dir_base}/${current_full_epoch}/${epoch}_incremental/${epoch}_backup
      touch     ${dir_base}/${current_full_epoch}/${epoch}_incremental/${epoch}_backup/${epoch}.tar.gz.gpg
      touch     ${dir_base}/${current_full_epoch}/${epoch}_incremental/${epoch}_backup_report.txt
      let "all_increments_offset=${all_increments_offset}+${offset}"
      sleep 1

   done
   let "current_full_epoch=${current_full_epoch}+${all_increments_offset}+${days_between_full_backups}"
   sleep 1
   echo
done
echo
