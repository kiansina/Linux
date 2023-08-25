"""
Create a new script file
"""

"""
.sh file is a script file
"""

"""
You will also add comments to the script, which are lines starting with #.
Comments are not executed by the shell.
"""

touch greet.sh

nano greet.sh

"""
paste following in .sh file
"""
##################################################from here
# This script accepts the user\'s name and prints
# a message greeting the user

# Print the prompt message on screen
echo -n "Enter your name :"

# Wait for user to enter a name, and save the entered name into the variable \'name\'
read name

# Print the welcome message followed by the name
echo "Welcome $name"

# The following message should print on a single line. Hence the usage of \'-n\'
echo -n "Congratulations! You just created and ran your first shell script "
echo "using Bash on IBM Skills Network"
##################################################Until here



"""
Run the commands below in the newly opened terminal.

Let's check the permissions for this new file by entering the following:
"""
ls -l greet.sh

"""
If the file exists and has read permissions, run the following command to
execute it:
"""
bash greet.sh










"""
Find the path to the interpreter
"""

"""
The which command helps you find out the path of the command bash.
"""
which bash

#In this case, it returns the path /bin/bash.

"""
Edit the script greet.sh and add the shebang line to the script
"""

"""
Open the file and add the following line at the beginning of the script:
"""
#! /bin/bash

"""
Check the permissions of the script
"""

"""
One more step needs to be completed to make greet.sh completely executable by name.

To add the execute permission for the user on greet.sh, enter the following:
"""
chmod +x greet.sh  #it is bad
chmod u+x greet.sh #it is good

"""
Execute the script.
"""
./greet.sh
