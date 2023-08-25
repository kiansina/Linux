"""
The /bin directory happens to be where Linux commmands such as ls and pwd are stored. For
example, you can see that ls is present by entering the following:
"""

ls /bin/ls

"""
To list all files starting with b in the /bin directory, try entering the following:
"""
ls /bin/b*

"""
To list all files ending in r in the /bin directory, enter the following:
"""
ls /bin/*r


"""
To print a longer list of files with additional information, such as the
last-modified date, enter the following:
"""
ls  -l

"""
Here are some common options that you can try with the ls command:

Option	Description
-a	list all files, including hidden files
-d	list directories only, do not include files
-h	with -l and -s, print sizes like 1K, 234M, 2G
-l	include attributes like permissions, owner, size, and last-modified date
-S	sort by file size, largest first
-t	sort by last-modified date, newest first
-r	reverse the sort order
"""

"""
To get a long list of all files in /etc, including any hidden files, enter the following:
"""
#Here we combined the options -l and -a by using the shorter notation, -la.
ls -la /etc

"""
Create a directory
"""
mkdir scripts


"""
Create an empty file
"""
touch myfile.txt

"""
If the file already exists, the touch command updates the access timestamp, or
last-modified date of the file. To see this, enter:
"""
date -r myfile.txt

"""
Search for and locate files
"""
"""
The find command is used to search for files in a directory. You can search for
files based on different attributes, such as the file's name, type, owner, size,
or timestamp.

The find command conducts a search of the entire directory tree starting from
the given directory name.

For example, the following command finds all .txt files in the /etc directory
and all of its subdirectories:
"""

find /etc -name \'*.txt\'


"""
Remove files
"""
"""
The rm command is used to delete files, ideally with the -i option, which
creates a prompt to ask for confirmation before every deletion.

To remove the file myfile.txt, enter the following command and press y to
confirm deletion, or n to deny deletion:
"""

rm -i myfile.txt

"""
Tip: When you are only removing one file with the rm command, the -i option is
redundant. But if you want to remove multiple files, for example by using a
wildcard to find all filenames matching a pattern, it's best practice to confirm
or deny each deletion by including the -i option.

Be careful when deleting files or directories! There is normally no way to
restore a deleted file once it is deleted, as there is no trash folder. This is
why you should always back up, or archive, your important files. You will learn
more about archiving files soon.
"""


"""
Move and rename a file
"""
"""
You should always use caution when moving a file. If the target file already
exists, it will be overwritten, or replaced, by the source file.

Conveniently, however, when the source and target directories are the same, you
can use mv to rename a file.

To illustrate this, use mv to rename users.txt to user-info.txt by entering the
following command:
"""
mv users.txt user-info.txt

"""
Because the source and target directories are the same (your present working
directory), the mv command will rename the file.
"""

"""
Now, you can move user-info.txt to the /tmp directory as follows:
"""
mv user-info.txt /tmp

"""
Copy files
"""

cp /tmp/user-info.txt user-info.txt


"""
At times, you may want to copy the contents of an existing file into a new one.

The following command copies the content of /etc/passwd to a file named users.txt
within the current directory:
"""
cp /etc/passwd users.txt


"""
View file access permissions
"""

#Run the following code to download the required files for this exercise:
cd /home/project
wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-LX0117EN-SkillsNetwork/labs/module%201/usdoi.txt


"""
Each file and each directory in your Linux system has permissions set for three
permission categories: the 'user', the 'group', and 'all users' (or 'other').

The following permissions are set for each file and directory:

Permission	Symbol
read	r
write	w
execute	x
To see the permissions currently set for a file, run the ls command with the -l
option.

For example, to see the permissions for the file named usdoi.txt in your current
directory, enter the following:
"""

ls -l usdoi.txt

"""
A sample output looks like the following:

-rw-r--r-- 1 theia theia 8121 May 31 16:45 usdoi.txt

The permissions set here are rw-r--r--. The - preceeding these permissions
indicates that usdoi.txt is a file. If it were a directory, you would see a d
instead of the -.

The first three entries correspond to the current user, the next three correspond
to the group, and the last three are for all others. You can see the user has read
and write permissions, while the user group only has read permission, and all other
users have only read permission. No users have execute permission, as indicated
by the - instead of an x in the third position for each user category.
"""

"""
Change file access permissions
"""

"""
chmod

The chmod or change mode command lets you change the permissions set for a file.

Specify which permissions to change with a combination of the following characters:

Option	Description
r, w, x	Permissions: read, write, and execute
u,g, o 	User categories: user, group, and all others
+, -	Operations: grant and revoke
The following command revokes read permissions for all users (user, group, and
other) on the file usdoi.txt:
"""
chmod -r usdoi.txt

#To grant read access to all users on usdoi.txt, enter:
chmod +r usdoi.txt

#Now to remove the read permission only for 'other' category, enter the following:
chmod o-r usdoi.txt

"""
View default directory access permissions
"""

"""
Recall the following table, which illustrates the meanings of each permission
for directories with examples of allowable operations for a given directory.

Directory Permission	Permissible action(s)
r	list directory contents using ls command
w	add/remove files or directories from directory
x	enter directory using cd command
For this exercise, first move to your project directory and create a new
directory called test:
"""

cd /home/project
mkdir test
ls -l

"""
You, "theia", as the owner of test, have read, write, and execute permissions
set by default. But all others only have read and execute permissions set and
cannot write to your test directory. This means users outside your group can't
add or remove files from test. They can, however, explore your directory to see
what files and directories exist there.
"""

"""
Note: You might be wondering what that s permission is in the execute slot for
your group. The s stands for "special permission". It means that any new files
created within the directory will have their group ownership set to be the same
as the directory owner. We won't go into this level of detail in this course,
but you can learn more about advanced Linux permissions here: Linux permissions:
SUID, SGID, and sticky bit.
"""

"""
Remove user execute permissions on your test directory
"""
cd test
mkdir test2
cd ../

chmod u-x test
cd test
"""
You get an error message!

bash: cd: test: Permission denied

As you just removed execute permissions for yourself on your test directory,
you can no longer make it your present working directory. However, you can still
"read" it with the ls command:
"""
ls -l

"""
Even though you have "write" permissions set, you can't actually create a new
directory within test, because removing execute permissions overrides write
permissions. For example, entering,
"""
mkdir test/test3

"""
throws an error:

mkdir: cannot create directory ‘test/test’: Permission denied

This time, try restoring execute permissions on test and denying write
permissions. Then verify your changes:
"""

chmod u+x test
chmod u-w test
ls -l

"""
Now you can go into test, but you still can't write to it! Entering
"""
cd test
mkdir test_again
"""
throws the error:

mkdir: cannot create directory ‘test_again’: Permission denied
"""
