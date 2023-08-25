"""
Exercise 1 - Initialize your weather report log file
"""
touch rx_poc.log

header=$(echo -e "year\tmonth\tday\tobs_tmp\tfc_temp")
echo $header>rx_poc.log

#instead of above 2 lines, one can use following line:
#echo -e "year\tmonth\tday\thour\tobs_tmp\tfc_temp">rx_poc.log


"""
Exercise 2 - Download the raw weather data
"""
touch rx_poc.sh
chmod u+x rx_poc.sh
ls -l rx_poc.sh

echo '#!/bin/bash'>>rx_poc.sh


"""
2.2 Edit rx_poc.sh to download today's weather report from wttr.in
"""

"""
2.2.1 Create the filename for today's wttr.in weather report
"""

nano rx_poc.sh
#add
fn="raw_date_$(date +"%Y-%m-%d")"
touch $fn

"""
2.2.2 Download the wttr.in weather report for Casablanca and save it with the
filename you created
"""

#way 1
city=Casablanca
curl wttr.in/$city --output $fn

#way2
curl wttr.in/Casablanca>>$fn

"""
Exercise 3 - Extract and load the required data
"""
grep °C $fn > temperatures.txt

obs_tmp=$(cat -A temperatures.txt | head -1 | cut -d "^" -f5 | cut -d "m" -f2)
echo "observed temperature = $obs_tmp"

fc_temp=$(cat -A temperatures.txt | head -3 | tail -1 | cut -d "^" -f16 | cut -d "m" -f2)

"""
3.2. Store the current hour, day, month, and year in corresponding shell variables
"""
hour=$(TZ='Morocco/Casablanca' date -u +%H)
day=$(TZ='Morocco/Casablanca' date -u +%d)
month=$(TZ='Morocco/Casablanca' date +%m)
year=$(TZ='Morocco/Casablanca' date +%Y)

"""
3.3. Merge the fields into a tab-delimited record, corresponding to a single row in Table 1
"""
record=$(echo -e "$year\t$month\t$day\t$obs_tmp\t$fc_temp")
echo $record>>rx_poc.log

"""
Exercise 4 - Schedule your Bash script rx_poc.sh to run every day at noon local time
"""

"""
4.1. Determine what time of day to run your script
"""
date

date -u #UTC
TZ='Morocco/Casablanca' date -u

"""
4.2 Create a cron job that runs your script
"""
crontab -e
#add
0 8 * * * /home/project/rx_poc.sh

"""
Exercise 5 - Create a script to report historical forecasting accuracy
"""
echo -e "year\tmonth\tday\tobs_tmp\tfc_temp\taccuracy\taccuracy_range" > historical_fc_accuracy.tsv

yesterday_fc=$(tail -2 rx_poc.log | cut -d " " -f5 | tail -1)
today_temp=$(tail -1 rx_poc.log | cut -d " " -f4)
accuracy=$(($yesterday_fc-$today_temp))


if [ -1 -le $accuracy ] && [ $accuracy -le 1 ]
then
   accuracy_range=excellent
elif [ -2 -le $accuracy ] && [ $accuracy -le 2 ]
then
    accuracy_range=good
elif [ -3 -le $accuracy ] && [ $accuracy -le 3 ]
then
    accuracy_range=fair
else
    accuracy_range=poor
fi
echo "Forecast accuracy is $accuracy"

row=$(tail -1 rx_poc.log)
year=$( echo $row | cut -d " " -f1)
month=$( echo $row | cut -d " " -f2)
day=$( echo $row | cut -d " " -f3)
echo -e "$year\t$month\t$day\t$today_temp\t$yesterday_fc\t$accuracy\t$accuracy_range" >> historical_fc_accuracy.tsv



"""
6.3. Display the minimum and maximum absolute forecasting errors for the week
"""
#!/bin/bash
echo $(tail -7 synthetic_historical_fc_accuracy.tsv  | cut -f6) > scratch.txt
week_fc=($(echo $(cat scratch.txt)))
# validate result:
for i in {0..6}; do
    echo ${week_fc[$i]}
done
for i in {0..6}; do
  if [[ ${week_fc[$i]} < 0 ]]
  then
    week_fc[$i]=$(((-1)*week_fc[$i]))
  fi
  # validate result:
  echo ${week_fc[$i]}
done
minimum=${week_fc[1]}
maximum=${week_fc[1]}
for item in ${week_fc[@]}; do
   if [[ $minimum > $item ]]
   then
     minimum=$item
   fi
   if [[ $maximum < $item ]]
   then
     maximum=$item
   fi
done
echo "minimum ebsolute error = $minimum"
echo "maximum absolute error = $maximum"
