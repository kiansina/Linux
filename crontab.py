"""
The five time-and-date fields cannot contain spaces and their allowed values
are as follows:

Field	Allowed values
minute	0-59
hour	0-23, 0 = midnight
day	1-31
month	1-12
weekday	0-6, 0 = Sunday
"""

"""
The -l option of the crontab command prints the current crontab.
"""

crontab -l

"""
3.1. Add a job to crontab
"""
crontab -e

"""
This will create a new crontab file for you (if you don't have one already).
Now you are ready to add a new cron job.
"""

"""
Add the below line at the end of the crontab file:
"""
0 21 * * * echo "Welcome to cron" >> /tmp/echo.txt


"""
The above job specifies that the echo command should run when the minute is 0
and the hour is 21. It effectively means the job runs at 9.00 p.m every day.

The output of the command should be sent to a file /tmp/echo.txt.
"""

#Check if the job is added to the crontab by running the following command.
crontab -l

"""
3.2. Schedule a shell script
"""


"""
Let us create a simple shell script that prints the current time and the current
disk usage statistics.
"""

touch diskusage.sh
nano diskusage.sh

#add following:

#! /bin/bash
# print the current date time
date
# print the disk free statistics
df -h


"""
Verify that the script is working:
"""
chmod u+x diskusage.sh
./diskusage.sh


"""
Let us schedule this script to be run everyday at midnight 12:00 (when the hour
is 0 on the 24 hour clock).
We want the output of this script to be appended to /home/project/diskusage.log.
"""

crontab -e
#Add the following line to the end of the file:
0 0 * * * /home/project/diskusage.sh >>/home/project/diskusage.log

#Check if the job is added to the crontab by running the following command:
crontab -l




"""
Exercise 4 - Remove the current crontab
"""


"""
The -r option causes the current crontab to be removed.

Caution: This removes all your cron jobs. Be extra cautious when you use this
command on a production server.
"""
crontab -r

#Verify if your crontab is removed:
crontab -l


"""
1. Create a cron job that runs the task date >> /tmp/everymin.txt every minute.
"""
crontab -e
#add following
* * * * * date >>/home/project/everymin.txt 2>>/home/project/err.log
