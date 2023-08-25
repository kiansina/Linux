"""
The .sh is a convention used to identify a text file as being a shell script.
"""


"""
Viewing file content with the cat command
"""
cat entrypoint.sh

"""
Although the cat command may not be the best way to view the contents of a file,
especially larger files, it is quite useful for shell scripting applications.
For example, it is often used to concatenate, or append one file onto another.
"""

"""
Viewing file content with the more command
"""
more entrypoint.sh

"""
you will see the top portion of the file first.

Tip: The first line of this particular file, #!/bin/bash, is called a shebang.
Basically, this shebang line makes the file a bash script by invoking the bash
shell. You will learn more about shebang lines later in this course.

When using the more command, you can see only as many lines as will fit on your
terminal window at once.

To see the next portion of the file, just press your spacebar. You can keep
paging this way, tapping the spacebar until you reach the end of the file. Once
you reach the last page, you will exit back to the command prompt.

Another way to exit is simply to type q, which quits and returns to the command
prompt.
"""


"""
Scrolling through file content with the less command
"""
less entrypoint.sh

"""
What if you want to move up and down through the file, not just downward? In
this case, you can use the less command:
"""

"""
Just like more, the less command displays the first page of the file. What's
useful about less is that you can use it to move around the file, page by page,
using the Page Up and Page Down keys.

You can also scroll up and down through the file line-by-line, using the Up Arrow
and Down Arrow keys, ↑ and ↓.

Unlike more, less does not automatically exit when you reach the end of a file,
allowing you the option to continue scrolling around. You can quit at any time by
typing q.
"""

####### Loading new file to exercise
cd /home/project
wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Bash%20Scripting/usdoi.txt
"""
The wget command downloads a text file called usdoi.txt from the provided URL.
You'll see this command again later in the context of networking commands. You
can check to see if you successfully downloaded the usdoi.txt by using the ls
command.
"""

"""
Display the first N lines of a file
"""

"""
head

By default, head will print the first 10 lines of a file. To use it with
usdoi.txt, enter the following:
"""
head usdoi.txt

"""
You can also specify the number of lines to be printed. Print only the first 3
lines of text from the file usdoi.txt by entering:
"""
head -3 usdoi.txt


"""
Display the last N lines of a file
"""

"""
tail

By default, tail will print the last 10 lines of the file usdoi.txt:
"""
tail usdoi.txt


"""
Just like with head, you can specify the number of lines to be printed. Print
the last 2 lines of the file usdoi.txt by entering the following:
"""
tail -2 usdoi.txt

"""
Count lines, words, or characters from a text file
"""

"""
wc

If you want to find the number of lines, words, and characters in a file like
usdoi.txt, enter the following command:
"""

wc usdoi.txt

"""
he output contains the number of lines, followed by the number of words, followed
by the number of characters in the file.

To get just the count of lines in usdoi.txt, use the -l option:
"""
wc -l usdoi.txt

"""
Similarly, for the count of words in usdoi.txt, use the -w option:
"""
wc -w usdoi.txt

"""
To print the number of characters in usdoi.txt, use the -c option:
"""
wc -c usdoi.txt

"""
Sort and display lines of file alphanumerically
"""
sort usdoi.txt

#To view those lines sorted in reverse order, enter:
sort -r usdoi.txt

"""
Drop consecutive duplicated lines and display result
"""
uniq zoo.txt
"""
The uniq line will drop any lines in the file that are identical and consecutive.
This is similar to what is known as "dropping duplicates". As you can see from
this example, however, there can still be duplicated lines left over if these
lines are not repeated right after the other.
"""

"""
Extract lines matching a specified criterion
"""

"""
The grep command allows you to specify a pattern and search for lines within a
file that match that pattern.

For example, the following command prints all lines in the file usdoi.txt which
contain the word people:
"""
grep people usdoi.txt

"""
Some frequently used options for grep include:

Option	Description
-n	Along with the matching lines, also print the line numbers
-c	Get the count of matching lines
-i	Ignore the case of the text while matching
-v	Print all lines which do not contain the pattern
-w	Match only if the pattern matches whole words
"""

"""
You can use these options to print all the lines from the /etc/passwd file which
do not contain the pattern login:
"""
grep -v login /etc/passwd


"""
Extract fields from lines of text
"""

"""
The cut command allows you to view only specific fields from each line of text
in a file.

For example, you can use cut with the -c option to view only the first two
characters of each line:
"""
cut -c -2 zoo.txt
#Or to view each line starting from the second character:
cut -c 2- zoo.txt

"""
The cut command can also be used to extract a field from a delimited file.
"""

"""
Now you can extract just the phone numbers for each person listed in the file
using the -d (delimiter) and f (field) options as follows:
"""
cut -d "," -f2 names_and_numbers.csv

"""
-d "," tells the command that the delimiter is a comma, and -f2 tells it to
extract the second field.
"""

"""
Merge text files line-by-line, aligned as columns
"""

"""
Use the paste command to merge lines of multiple files together.

Download the following file:
"""
wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-LX0117EN-SkillsNetwork/labs/module%201/zoo_ages.txt

"""
Then use the paste command to view the two files merged together, line-by-line,
as columns delimited by a Tab character:
"""
paste zoo.txt zoo_ages.txt


"""
Try changing the delimiter. Instead of the default Tab delimiter, you can
specify a comma , as follows:
"""

paste -d "," zoo.txt zoo_ages.txt

"""
Display the number of lines in the /etc/passwd file.
"""
wc -l /etc/passwd


"""
Display the lines that contain the string "not installed" in
/var/log/bootstrap.log.
"""
grep "not installed" /var/log/bootstrap.log



"""
The text file at
https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Bash%20Scripting/top-sites.txt
contains a list of popular websites. Find all the websites on the list that have
the word "org" in them.
"""
wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Bash%20Scripting/top-sites.txt
grep org top-sites.txt

"""
Alternative Solution
"""
curl -o top-sites.txt https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Bash%20Scripting/top-sites.txt
grep org top-sites.txt


"""
Print the first seven lines of top-sites.txt.
"""
head -n 7 top-sites.txt

"""
Print the last seven lines of top-sites.txt.
"""
tail -n 7 top-sites.txt

"""
Print the first three characters of each line from top-sites.txt
"""
cut -c -3 top-sites.txt

"""
Extract and view only the names, without their phone numbers, from the file
names_and_numbers.csv.
"""
cd /home/project
cut -d "," -f 1 names_and_numbers.csv
