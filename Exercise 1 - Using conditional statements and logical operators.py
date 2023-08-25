"""
Exercise 1 - Using conditional statements and logical operators
"""

"""
In this exercise, you will create a simple Bash script containing a conditional
statement to handle the following tasks:

Prompt the user for a Yes or No response to a question
Print a response based on the user's answer
"""

echo '#!/bin/bash' > conditional_script.sh
chmod u+x conditional_script.sh


"""
1.2. Query the user and store their response
"""

"""
Now get your script to:

Ask the user a binary "yes or no" question of your choosing
Store the user's answer in a variable.
"""

#Your Bash script should now look something like this:


#!/bin/bash
echo 'Are you enjoying this course so far?'
echo -n "Enter \"y\" for yes, \"n\" for no."
read response

"""
1.3. Use a conditional block to select a response for the user
"""

"""
Finally, use a conditional block to print a message to the user based on their
response to your query.
"""

#Now your Bash script should be similar to the following:

#!/bin/bash
echo 'Are you enjoying this course so far?'
echo -n "Enter \"y\" for yes, \"n\" for no"
read response
if [ "$response" == "y" ]
then
    echo "I'm pleased to hear you are enjoying the course!"
    echo "Your feedback regarding what you have been enjoying would be most welcome!"
elif [ "$response" = "n" ]
then
   echo "I'm sorry to hear you are not enjoying the course."
   echo "Your feedback regarding what we can do to improve the learning experience"
   echo "for this course would be greatly appreciated!"
else
   echo "Your response must be either 'y' or 'n'."
   echo "Please re-run the script to try again."
fi
