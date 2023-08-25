pwd
ls
cd
cd .. | . | ~ | /
# Using tabs to auto complete

sudo apt update

"""
Upgrading nano
nano is a simple command line editor that enables you to use the terminal window as a text
editor.

nano is already installed on your system. Go ahead and upgrade to the latest supported
version of nano by entering:
"""


sudo apt upgrade nano


"""
1.3. Installing Vim
Another popular text-editing program is Vim. Vim is a highly configurable text editor built
for efficiency. It takes some practice to get good at using Vim, but the time investment is
very worthwhile.

Because Vim isn't preinstalled on your Linux system, you'll need to install it yourself. If
you haven't already done so in this session, ensure you run the command sudo apt update.
Then to install Vim, enter the following command:
"""
sudo apt install vim


"""
 Creating and editing files with nano
"""

nano hello_world.txt


cat hello_world.txt

"""
Creating and editing files with Vim
"""
vim
:help
:q

vim hello_world_2.txt
i #use to insert

#use escape button to exit insert mode and return to command mode

:w #this saves your work (write)
:q

"""
We can use "echo" also in txt. then when we run "bash done.txt" This command invokes the
Bash shell to interpret the text contained in done.txt as a command. In particular, Bash
runs the echo command along with the quoted text as the input to echo, while echo simply
prints the input text to the terminal window.
"""
#add the following in the text file:
echo "I am done with the lab!"

#Then save and quit vim

bash done.txt





man ls


"""
Fetch and display up-to-date information about all upgradable packages:
"""
sudo apt update



"""
Upgrade to the latest supported version of nano: Instead of nano you can put whatever app
that you see in response of above command
"""
sudo apt upgrade nano


sudo apt install vim



printenv SHELL
# If the default is not bash you can make it bash by following code:
bash


#for all linux default commands there is a manual: for example:
man id

#You can get a listing of all the commands on your system that have a manual page by
#entering:
man -k .



""""
Similar to man pages, TLDR Pages is a free and open-source collaborative documentation
effort. The goal is to create documentation that is more accessible than the traditional
man pages, which tend to be quite verbose.
"""

npm install -g tldr

tldr ls #ls is just an example. it will give also some manual for ls
