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








files=(
       1034221566
       1092019593
       1149817620
       1207615647
       1265413674
      )



epoch_now=`date +%s`
echo $epoch_now



dir_base='/home/david/local_backup'
let "seconds_per_day=60*60*24"
let "days_between_full_backups=14*${seconds_per_day}"
let "first_epoch=1378973400-2*${days_between_full_backups}"




echo
let "current_full_epoch=first_epoch"
#for i in "${files[@]}"
for jjj in 1 2 3 4 5
do

   if (("$current_full_epoch" < "$epoch_now"))
   then
      echo
      if [ $overwrite_existing_backups = "YES" ];
      then
         rm -rf  ${dir_base}/${current_full_epoch}
         echo "Dir deleted and to be recreated:   ${dir_base}/${current_full_epoch}"
      fi

      # Full backup
      echo
      echo  "FULL backup    ${current_full_epoch}"
      mkdir -p  ${dir_base}/${current_full_epoch}/${current_full_epoch}
      touch     ${dir_base}/${current_full_epoch}/${current_full_epoch}/${current_full_epoch}.tar.gz.gpg
      touch     ${dir_base}/${current_full_epoch}/${current_full_epoch}.yaml
      sleep 1

      let "all_increments_offset=0"
      for ccc in 3 10
      do
         let "offset=$ccc*${seconds_per_day}"
         let "epoch=${current_full_epoch}+$offset"
         if (("$epoch" < "$epoch_now"))
         then
            echo  "   incremental backup  count / epoch    ${ccc} / ${epoch}"

            # Incremental backup
            mkdir -p  ${dir_base}/${current_full_epoch}/${epoch}
            touch     ${dir_base}/${current_full_epoch}/${epoch}/${epoch}.tar.gz.gpg
         else
            echo "incremental backup epoch is past current epoch:   backup / current    $epoch   $epoch_now"
         fi
         let "all_increments_offset=${all_increments_offset}+${offset}"
         sleep 1

      done
#      let "current_full_epoch=${current_full_epoch}+${all_increments_offset}+${days_between_full_backups}"
      let "current_full_epoch=${current_full_epoch}+${days_between_full_backups}"
      echo

   else
      echo "FULL backup epoch is past current epoch:   backup / current    $current_full_epoch   $epoch_now"
   fi





done
echo
