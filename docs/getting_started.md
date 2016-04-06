# Getting Started

This pratical version of the course is going to be online. Therefore you need
a personal computer with installed a Web browser and an Internet connection
active.

To access to this course you also have to install GIT, Bash, Python and
some python packages. Please follow following steps in the given order.

## Step 1: create a personal account on BitBucket

The course is hosted on [BitBucket](http://www.bitbucket.org) Web site.
You need to register personal account in order to access to it. You can create
one [here](https://bitbucket.org/account/signup/).
Once you have created your own accout please ask to project organizer to
send you an invitation to join the online course.

You can write to:
- Federico Ressi <federico.ressi_[at]_intel.com> (please replace _[at]_ with @)

## Step 2: install GIT and Bash

GIT and Bash are required to downlowand your copy of the course, to run
tests and to publish your homework to this Web site.

### Linux

All Linux distributions comes with Bash. GIT instead could be installed using
distribution specific package manager. For example in Ubuntu you can type
following:

```
sudo apt-get install git
```

Please refer to your distro documentation for more details about this.

### OSX

On OSX bash is installed by default as Linux. You can download an up-to-date
git from its official [Web site](https://git-scm.com/downloads).

### Windows and other OSs

On Window platform you can have both GIT and Bash installed by installing GIT
SCM from its official [Web site](https://git-scm.com/downloads).

## Step 3: install Python

This course requires both Python 2.7 and Python 3.4 to be installed to give a
taste of differences this two flavors can give.

To check if the right python version is properly installed you can type
following:

```
python2.7 --version
python3.4 --version
```

### Linux

All Linux distributions comes with Bash. GIT instead could be installed using
distribution specific package manager. For example in Ubuntu 14.04 you can type
following:

```
sudo apt-get install python2.7 python2.7-dev python3.4 python3.4-dev
```

### OSX, Windows and other operative systems

On other OSs you can download Python from its official
[Web site](https://www.python.org/downloads/).

## Step 4: install PIP

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

## Step 5: install Tox

Tox is used to execute tests to evaluate you exercise are properly written.
To install and keep up to date Tox and PIP you have to execute following:

```
pip install -U --user tox
```

Finally check that tox is working:

```
tox --version
```
