# Getting Started

This pratical version of the course is going to be online. Therefore you need
a personal computer with installed a Web browser and an Internet connection
active.

To access to this course you also have to install Git, Bash, Python and
some python packages. Please follow following steps in the given order.

## Step 1: create a personal account on GitHub

This course is hosted on [GitHub](https://github.com) Web site.
You need to register personal account in order to access to it. You can create
one [here](https://github.com/join?source=header-home).
The course is release under open source licence. To download it, do your
exercises and publish it back on the site you shouldn't require special
permissions.

**Once you have an account send an e-mail to Federico Ressi to allow you to submit
your works for review**:

```
Federico Ressi <federico.ressi at intel.com>
```

please replace _at_ with _@_.

**In the text of the e-mail you should specify the
user name you are going to use on GitHub.**

## Step 2: install Git and Bash

Git and Bash are required to downlowand your copy of the course, to run
tests and to publish your homework to this course web site.

### Linux

All Linux distributions comes with Bash. Git instead could be installed using
distribution specific package manager. For example in Ubuntu you can type
following:

```
sudo apt-get install git
```

Please refer to your distro documentation for more details about this.

### OSX

On OSX bash is installed by default as Linux. You can download an up-to-date
Git version from its official [Web site](https://git-scm.com/downloads).

### Windows and other OSs

On Window platform you can have both Git and Bash installed by running Git
SCM installer from its official [Web site](https://git-scm.com/downloads).

## Step 3: configure Git

Once installed, to configure Git you should follow one of following guides:
- [First-Time Git Setup](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup) - by Git SCM
- [Set Up Git](https://help.github.com/articles/set-up-git/) - by GitHub


## Step 4: install Python

This course requires both Python 2.7 and Python 3.4 to be installed to give a
taste of differences between this two major releases.

To check if the right python version is properly installed you can type
following:

```
python2.7 --version
python3.4 --version
```

### Linux

All Linux distributions comes with Bash. Git instead could be installed using
distribution specific package manager.

For example in **Ubuntu 14.04** you can install required packages by typing:

```
sudo apt-get install python2.7 python2.7-dev python3.4 python3.4-dev
```

In some **other Linux** distribution there could be any package for Python 3.4.
In such case you should be able to compile it following
[this documentation](https://docs.python.org/3.4/using/unix.html).
Please note that a C compiler and some other development tool could be required.

### OSX, Windows and other operative systems

On other OSs you can download Python from its official
[Web site](https://www.python.org/downloads/).

## Step 5: install PIP

PIP is required to install Python software packages published by good big
open source Python comunity. Some useful instructions how to install it can be
found [here](https://pip.pypa.io/en/stable/installing/)

### Linux

Almost all Linux distributions provides some package for PIP. It is instead
preferible to use the last public version. To get installation script you
can use WGET:

```
wget https://bootstrap.pypa.io/get-pip.py
```

### All OSs including Linux

[Download get-pip.py](https://bootstrap.pypa.io/get-pip.py) script and execute
it using python 2.7 and python 3.4.

```
python2.7 get-pip.py --user
python2.7 -m pip install -U --user pip
python3.4 get-pip.py --user
python3.4 -m pip install -U --user pip
```

Finally check that pip is working:

```
python2.7 -m pip --version
python3.4 -m pip --version
```

## Step 6: setup proxy environment variables

Before installing python packages if you are beside corporation proxy (anb I gues you are ;-))
you should make sure following environment variables are defined.
```
export http_proxy=http://<yur-proxy-address>
export HTTPS_PROXY=http://<yur-proxy-address>
export https_proxy=http://<yur-proxy-address>
export no_proxy=127.0.0.1,localhost
export HTTP_PROXY=http://<yur-proxy-address>
```
Above lines has to be defined on your system. If you don't know your proxy
address you can ask to your collegues, or the network administrator or
contact the author of this document for help.

As I reccomend you to use bash
(like the one included with the Git SCM installer for Windows), you can define
them by editing your ```.bashrc``` file found on your home folder
(create it if it doesn't exist).

To know where you home folder is please type following from bash:
```
echo $HOME
```

To have environment variable changes applied you should restart bash or
import .bashrc by typing:
```
source ~/.bashrc
```

To verify environment variables are properly defined you can type following:
```
env | grep proxy
```

## Step 7: install Tox

Tox is used to execute tests to evaluate you exercise are properly written.
To install and keep up to date Tox and PIP you have to execute following:
```
pip install -U --user tox
```
Finally check that tox is working:
```
tox --version
```

## Step 8: clone course repository

From your terminal enter in the folder of your where you want to work and clone
this course repository and enter inside it.

```
git clone https://<your-github-username>@github.com/FedericoRessi/pythoncourse.git
cd pythoncourse
```

Please replace _```<your-github-username>```_ with your GitHub username.

Before you start doing any change you have to create your own branch:
```
git checkout -b <your-branch-name>
git push --set-upstream origin <your-branch-name>
```
replacing _```<your-branch-name>```_ with for example your Intel user ID.

**Above push operation will fail if you didn't received permission for committing
change to this repository as specified at Step 1.**

A valid branch name could be for example your GiHub user name. Branch names sould not
contain spaces or any white character.

## Step 9: create a pull request

Make your first change by editing your student details on file STUDENT.md
Then commit it:

```
git commit "Fill student details."
git push
```

Enters on GitHub [course page](https://github.com/FedericoRessi/pythoncourse)
and create a [new pull request](https://github.com/FedericoRessi/pythoncourse/pull/new/master).

On the left side in the drop down box you have to chose your working branch.
On the right side in the drop down box you have to leave it as "master" branch.

## Step 9: complete exercizes

You can now start working on exercises found on folder
[python_course_1604](../python_course_1604/class_01).
To validate your work you can type from the main folder of the project:

```
tox
```

Test execution will have success only when you would have completed all exercises.
Exercises you didn't touched will be skipped.

To submit your exercises for review you have to commit your changes
an then and pussh them to origin repository in your new branch.

```
git commit
git push
```

## Step 10: keep your repo up to date

It happens that something is updated on this project to solve problems or add more exercises.
You should try to keep your branch up to date your branch with baster branch you can merge
or rebase.

### Merge with master branch

```
git fetch --all
git merge origin/master 
```

### Rebase master branch

```
git fetch --all
git rebase origin/master 
```

If you chose to rebase be prepared to have to force pushing future changes
using _-f_ flag:

```git push -f```

**[GitHub support for rebasing](https://help.github.com/articles/about-git-rebase/)
could be weird if you have an open pull request for such branch because it alters
the history of your branch.**
