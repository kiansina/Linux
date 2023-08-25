"""
Display the name of the current user
"""
whoami

#You can get a list of currently logged in users using the command:
who

"""
Get basic information about the operating system
"""
#By default the command prints the kernel name. The u in uname refers to "unix-like 0S".
uname

#Using the -a option prints all the system information.
uname -a

"""
Obtain the user and group identity information
"""
id


"""
Get available disk space
"""
df

# human readable format
df -h

"""
 View currently running processes
"""
#However, the output only contains the processes that are owned by you.
ps

#By using the -e option, you can display all of the processes running on the system. The includes processes owned by other users.
ps -e

"""
Get information on the running processes and system resources
"""
top
#The output keeps refreshing until you press q or Ctrl + c.

#If you want to exit automatically after a specified number of repetitions, use the -n option as follows:
top -n 10

"""
You can press the following keys with Shift while top is running to sort the table:

Key	Sorts by
m	Memory Usage
p	CPU Usage
n	Process ID (PID)
t	Running Time
For example, you can find out which process is consuming the most memory by entering Shift + m.
"""


"""
Display Messages
"""
echo "Welcome to the linux lab"

"""
Special Character	Effect
\n	Start a new line
\t	Insert a tab
"""

#Use the -e option of the echo command when working with special characters. For example:
echo -e "This will be printed \nin two lines"

"""
Display date and time
"""
date
#For example, the following command displays the current date in mm/dd/yy format:
date "+%D"

"""
Specifier	Explanation
%d	Displays the day of the month (01 to 31)
%h	Displays the abbreviated month name (Jan to Dec)
%m	Displays the month of year (01 to 12)
%Y	Displays the four-digit year
%T	Displays the time in 24 hour format as HH:MM:SS
%H	Displays the hour
"""



"""
View the Reference Manual For a Command
"""
man ls

#You will sometimes encounter a command that does not have a man page avaible on your
#system. To see all available man pages with a brief description of each command, enter:
man -k .
