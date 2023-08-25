"""
Display your system's hostname and IP address
"""

"""
A hostname is a name that is assigned to a computer or device on a network, and
it is used to identify and communicate with that device.

To view the current hostname, run the command below:
"""

hostname

"""
An IP address (Internet Protocol address) is a numerical label assigned to each
device connected to a computer network that uses the Internet Protocol for
communication.

You can use the -i option to view the IP address of the host:
"""
hostname -i

"""
Display network interface configuration
"""

"""
The ifconfig command is used to configure or display network interface parameters
for a network.

To display the configuration of all network interfaces of your system, enter:
"""
ifconfig

"""
To display the configuration of a particular device, such as the ethernet
adapter eth0, enter:
"""
ifconfig eth0

"""
eth0 is usually the primary network interface that connects your server to the
network.

You can see your server's IP address in line 2 after the word inet.
"""

"""
Test connectivity to a host
"""

"""
Use the ping command to check if www.google.com is reachable. The command keeps
pinging data packets to server at www.google.com and prints the response it gets
back. (Press Ctrl+c to stop pinging.)
"""
ping www.google.com

"""
If you want to ping only a limited number of times, use -c option.
"""
ping -c 5 www.google.com

"""
Transfer data from a server
"""

"""
You can use curl to access the file at the following URL and display the file's
contents on your screen:
"""
curl https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Bash%20Scripting/usdoi.txt

"""
To access the file at the given URL and also save it in your current working
directory, use the -O option:
"""
curl -O https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Bash%20Scripting/usdoi.txt

"""
You can also use curl to view the HTML code for any web page if you know its URL.
"""

"""
Download file(s) from a URL
"""

"""
The wget command is similar to curl, however its primary use is for file
downloading. One unique feature of wget is that it can recursively download
files at a URL.

To see wget in action, first remove usdoi.txt from your current directory:
"""
rm usdoi.txt

"""
then download it again using wget as follows:
"""
wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Bash%20Scripting/usdoi.txt


#########################à
###############################
#####################################
"""
Create and manage file archives
"""

"""
The tar command allows you to pack multiple files and directories into a single
archive file.

The following command creates an archive of the entire /bin directory and writes
the archive to a single file named bin.tar.

The options used are as follows:

Option	Description
-c	Create new archive file
-v	Verbosely list files processed
-f	Archive file name
"""
tar -cvf bin.tar /bin

"""
To see the list of files in the archive, use the -t option:
"""
tar -tvf bin.tar

"""
To untar the archive or extract files from the archive, use the -x option:
"""
tar -xvf bin.tar

"""
Package and compress archive files
"""

"""
The zip command allows you to compress files.

The following command creates a zip file named config.zip consisting of all the
files with extension .conf in the /etc directory.
"""
zip config.zip /etc/*.conf


"""
The -r option can be used to zip an entire directory.

The following command creates an archive of the /bin directory.
"""
zip -r bin.zip /bin


"""
Extract, list, or test compressed files in a ZIP archive
"""

"""
The unzip command allows you to extract files.

To list the files of the archive config.zip, enter the following:
"""
unzip -l config.zip


"""
The following command extracts all the files in the archive bin.zip.
"""
unzip -o bin.zip

"""
We added the -o option to force overwrite in case you run the command more than
once.

You should see a folder named bin created in your directory.
"""
