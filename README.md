# Toward Advanced Python for Data Science
## A CSCI-E-29 Project
#### by Anthony Chaves

This project is an effort to ease the learning curve for those new to using Python for data science.  The aim is to provide an overview of the current Python ecosystem and the tools currently in favor with Python-friendly data scientists.  The goal of this project is to help you be a good Python developer.  The bulk of the content is delivered as section material with a 96 minute live development session.  Regarding software development practices for data science, the aim is to get on the right track and stay there.  It is not about how to debug specific errors.  The first part of this project is about the different Python distributions a data scientist may encounter on their system.  The second part is a live development exercise, showing examples of developer tools in practice.  New data scientists are encouraged to follow along.  While the sample code may not be the most interesting topic, it explores a Python language feature (Descriptors) in-depth.  The point is not the sample code itself, the point is to understand the process and best practices used to explore, develop, and test our software as data scientists.  We will examine several tools that are part of this practice, including:
  * The Python command line environment
  * Creating and destroying Python virtual environments
  * Python module and package management
  * The PyCharm IDE
  * Good practices using git as part of your development workflow
  * Testing with PyTest on the command line and in the PyCharm IDE
  * Interactive debugging using the PyCharm debugger

---

## Python distributions
This section of the project describes the typical Python development scenario on a Linux distribution, specifically Ubuntu Linux.  The concepts described here are as abstract as possible, while the command line instructions are specific to Ubuntu Linux 18.04 and newer.  Data scientists using different Linux distributions, or Mac OS, or Windows have different command line procedures and installation process.  Once we have a usable Python, the live development video starts with the PyCharm IDE, where users on any platform can benefit.  The concepts of System Python, User Python and Virtual Environment Python remain the same from system to system.  

### which python
The ability to understand the nuances and complexities of modern data science starts with knowing your execution environment.  Python's history includes status as the defacto scripting language for application servers, system package managers, and software glue between disparate programs.  As such, it has become an important part of several long-standing projects.  These projects, system package managers like apt, for example, require consistency and longevity of support.  These special-purposed Pythons use specific versions of Python the language, and require specific versions of the Python interpreter.  The apt package manager requires Python 2.7.  Python 2.7 is installed on any system using the apt package manager, and is made available on the command line.  This deep integration with the system package manager leads us to call this Python the "system Python".  We can investigate what that Python is, and where it lives.  It is vital that we do not use, nor disturb, the system Python, as our development requirements are incompatable with having an immutable Python environment like the apt package manager requires.

From the command line, we can learn about the system Python.  
```bash
anthony@vision:~/projects/csci-e-29$ which python
/usr/bin/python


anthony@vision:~/projects/csci-e-29$ /usr/bin/python --version
Python 2.7.17rc1
```
Python 2.7 is _ancient_ for our purposes, but it is just fine for apt.  We are going to use Python 3.6 or 3.7 for our development.  We need to use the package manager to install Python 3.6 or Python 3.7.  This is what we call the User Python.  User Python forms the basis for creating Python virtual environments.  It is important to install a modern Python for development.  We will also leave this User Python untouched beyond the initial install.  One of the drawbacks of using the system or user Python is that they are subject to modification by the operating system, package manager, other users on the system, or our own poor decision-making.  Debugging and fixing these Pythons is time consuming and difficult.  Our preference for Python virtual environments alleviates these problems by making Python environments inexpensive to create and destroy.

Find out what Python 3 interpreters are available using apt.
```bash
anthony@vision:~/projects/csci-e-29$ sudo apt list python3
Listing... Done
python3/eoan,now 3.7.5-1 amd64 [installed]
python3/eoan 3.7.5-1 i386
```
If the Python for your system is not listed as [installed], install it using apt.
```bash
anthony@vision:~/projects/csci-e-29$ sudo apt install python3
Reading package lists... Done
Building dependency tree       
Reading state information... Done
python3 is already the newest version (3.7.5-1).
0 upgraded, 0 newly installed, 0 to remove and 1 not upgraded.
```
When prompted, inspect the additional packages that will be installed by apt, then choose 'y' to install them.  

```bash
anthony@vision:~/projects/csci-e-29$ which python3
/usr/bin/python3


anthony@vision:~/projects/csci-e-29$ /usr/bin/python3 --version
Python 3.7.5
```
There are now two different Python interpreters installed on our system.  This is where problems start to arise.  In the case where we use either the system or user Python for development, we start to install Python packages and third party libraries that can be incompatable with one another, and with the Python language itself, depending on versions of language and package.  We can avoid a little confusion by aliasing our python command for our (user) use in the bash shell.
```bash
anthony@vision:~/projects/csci-e-29$ nano ~/.bashrc
```
At the bottom of this file, include the following line:
```bash
alias python=python3
```
Restart bash to activate the change.  What happens when we come back to python?

```bash
anthony@vision:~/projects/csci-e-29$ which python
/usr/bin/python


anthony@vision:~/projects/csci-e-29$ /usr/bin/python --version
Python 2.7.17rc1


anthony@vision:~/projects/csci-e-29$ python --version
Python 3.7.5
```
The which command still shows the full path to system Python, version 2.7.  However, running the python command in bash executes our alias, which uses the python3 binary.  This is ok and completely expected.  Our alias does not change how apt interacts with the system Python.  Even better, we have put an obstacle in our own way in regard to unintentionally changing system Python.  At our user command line, python executes Python 3.7, not Python 2.7.  Python 2.7 is not usable unless we specify the full system path to the binary. This is a good thing, as only apt should use the system Python.

### pipenv

Our development should use Python virtual environments.  A Python virtual environment creates copies of and symlinks to the appropriate files and binaries.  It also gets its own PYTHONHOME directory, under the hidden ~/.local directory.  There are several Python tools that can create a Python virtual environment.  We will focus on pipenv, and we will install pip in order to bootstrap pipenv itself.  Our Python virtual environments used for development will use pipenv.  The advantage that virtual environments have over system and user Python is isolation.  Python virtual environments allow for different libraries and dependencies to be installed in different virtual environments, even if they are created with the same user Python.  That each virtual environment has its own base directory, each containing a bin, lib and share directory, so that any libraries installed in one virtual environment are not available in other virtual environments.  This includes the system and user Python environments.  The pipenv tool, when creating a virtual environment, creates aliases to the python binary, and modifies the PYTHONHOME, PYTHONPATH and other environment variables so that only the libraries installed under the current virtual environment are available to the Python executable.  

Find the pip tool for your system.
#### pipenv bootstrap
```bash
anthony@vision:~/projects/csci-e-29$ sudo apt list python-pip
Listing... Done
python-pip/eoan,eoan,now 18.1-5 all


anthony@vision:~/projects/csci-e-29$ sudo apt list python3-pip
Listing... Done
python3-pip/eoan,eoan,now 18.1-5 all [installed]


anthony@vision:~/projects/csci-e-29$ sudo apt install python3-pip
Reading package lists... Done
Building dependency tree       
Reading state information... Done
python3-pip is already the newest version (18.1-5).
0 upgraded, 0 newly installed, 0 to remove and 1 not upgraded.
```
Note that we want to install python3-pip, _not_ python-pip.  Remember, we always use Python 3.6 or Python 3.7 for data science software development.  Our tools need to be targeted at the correct Python.

```bash
anthony@vision:~/projects/csci-e-29$ sudo apt install python3-pip
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following NEW packages will be installed:
  python3-pip
0 upgraded, 1 newly installed, 0 to remove and 1 not upgraded.
Need to get 135 kB of archives.
After this operation, 707 kB of additional disk space will be used.
Get:1 http://us.archive.ubuntu.com/ubuntu eoan/universe amd64 python3-pip all 18.1-5 [135 kB]
Fetched 135 kB in 0s (1,728 kB/s)    
Selecting previously unselected package python3-pip.
(Reading database ... 358151 files and directories currently installed.)
Preparing to unpack .../python3-pip_18.1-5_all.deb ...
Unpacking python3-pip (18.1-5) ...
Setting up python3-pip (18.1-5) ...
Processing triggers for man-db (2.8.7-3) ...


anthony@vision:~/projects/csci-e-29$ python -m pip install --user pipenv
Collecting pipenv
  Using cached https://files.pythonhosted.org/packages/13/b4/3ffa55f77161cff9a5220f162670f7c5eb00df52e00939e203f601b0f579/pipenv-2018.11.26-py3-none-any.whl
Requirement already satisfied: pip>=9.0.1 in /usr/lib/python3/dist-packages (from pipenv) (18.1)
Requirement already satisfied: certifi in /usr/lib/python3/dist-packages (from pipenv) (2018.8.24)
Collecting virtualenv (from pipenv)
  Downloading https://files.pythonhosted.org/packages/05/f1/2e07e8ca50e047b9cc9ad56cf4291f4e041fa73207d000a095fe478abf84/virtualenv-16.7.9-py2.py3-none-any.whl (3.4MB)
    100% |████████████████████████████████| 3.4MB 489kB/s
Requirement already satisfied: setuptools>=36.2.1 in /usr/lib/python3/dist-packages (from pipenv) (41.1.0)
Collecting virtualenv-clone>=0.2.5 (from pipenv)
  Using cached https://files.pythonhosted.org/packages/ba/f8/50c2b7dbc99e05fce5e5b9d9a31f37c988c99acd4e8dedd720b7b8d4011d/virtualenv_clone-0.5.3-py2.py3-none-any.whl
Installing collected packages: virtualenv, virtualenv-clone, pipenv
Successfully installed pipenv-2018.11.26 virtualenv-16.7.9 virtualenv-clone-0.5.3
```

Installing the pipenv tool fleshes out the ~/.local/ directory.  It creates or modifies the bin, lib and share directories, and creates the virtualenvs directory.  It's important to know the contents of each of these directories.  Any Python package dependencies installed by pipenv, including those listed in your Pipfile, will be installed to these subdirectories.  When you eventually run in to problems, it's likely the problem originates in one of these subdirectories or their children.  An error message that provides an absolute or relative file path would list a file under the ~/.local directory.

```bash
anthony@vision:~/projects/csci-e-29$ ls -lh ~/.local/lib/python3.7/site-packages/
total 140K
-rw-r--r-- 1 anthony anthony  11K Dec 16 17:44 clonevirtualenv.py
drwxr-xr-x 6 anthony anthony 4.0K Dec 16 17:44 pipenv
drwxr-xr-x 2 anthony anthony 4.0K Dec 16 17:44 pipenv-2018.11.26.dist-info
drwxr-xr-x 2 anthony anthony 4.0K Dec 16 17:44 __pycache__
drwxr-xr-x 2 anthony anthony 4.0K Dec 16 17:44 virtualenv-16.7.9.dist-info
drwxr-xr-x 2 anthony anthony 4.0K Dec 16 17:44 virtualenv_clone-0.5.3.dist-info
-rw-r--r-- 1 anthony anthony 104K Dec 16 17:44 virtualenv.py
drwxr-xr-x 3 anthony anthony 4.0K Dec 16 17:44 virtualenv_support
```
The ~/.local/lib/python3.7/site-packages/ directory contains files required by pipenv.

```bash
anthony@vision:~/projects/csci-e-29$ ls -lh ~/.local/bin
total 84K
-rwxr-xr-x 1 anthony anthony 223 Oct 20 21:42 chardetect
-rwxr-xr-x 1 anthony anthony 222 Oct 20 21:42 cookiecutter
-rwxr-xr-x 1 anthony anthony 218 Oct 20 22:26 coverage
-rwxr-xr-x 1 anthony anthony 217 Oct 20 22:21 coverage2
-rwxr-xr-x 1 anthony anthony 217 Oct 20 22:21 coverage-2.7
-rwxr-xr-x 1 anthony anthony 218 Oct 20 22:26 coverage3
-rwxr-xr-x 1 anthony anthony 218 Oct 20 22:26 coverage-3.7
-rwxr-xr-x 1 anthony anthony 212 Oct 26 16:34 dotenv
-rwxr-xr-x 1 anthony anthony 232 Nov  3 13:52 easy_install
-rwxr-xr-x 1 anthony anthony 232 Nov  3 13:52 easy_install-2.7
-rwxr-xr-x 1 anthony anthony 216 Oct 20 21:42 flake8
-rwxr-xr-x 1 anthony anthony 217 Oct 20 21:42 futurize
-rwxr-xr-x 1 anthony anthony 219 Oct 20 21:42 pasteurize
-rwxr-xr-x 1 anthony anthony 206 Nov  3 17:50 pipenv
-rwxr-xr-x 1 anthony anthony 217 Nov  3 17:50 pipenv-resolver
-rwxr-xr-x 1 anthony anthony 214 Oct 20 21:42 pycodestyle
-rwxr-xr-x 1 anthony anthony 213 Oct 20 21:42 pyflakes
-rwxr-xr-x 1 anthony anthony 208 Oct 20 22:26 py.test
-rwxr-xr-x 1 anthony anthony 208 Oct 20 22:26 pytest
-rwxr-xr-x 1 anthony anthony 212 Nov  3 13:54 virtualenv
-rwxr-xr-x 1 anthony anthony 217 Nov  3 17:50 virtualenv-clone


anthony@vision:~/projects/csci-e-29$ ls -lh ~/.local/lib/
total 12K
drwx------ 3 anthony anthony 4.0K Oct 20 21:42 python2.7
drwx------ 3 anthony anthony 4.0K Sep  8 15:04 python2.7.old
drwxr-xr-x 3 anthony anthony 4.0K Oct 20 21:28 python3.7


anthony@vision:~/projects/csci-e-29$ ls -lh ~/.local/share/virtualenvs/
total 88K
drwxr-xr-x 6 anthony anthony 4.0K Oct 20 12:23 2019fa-ccp0-anthonychaves-3Lda1HQB
drwxr-xr-x 6 anthony anthony 4.0K Oct 20 15:23 2019fa-ccp1-anthonychaves-OQxe2B0W
drwxr-xr-x 6 anthony anthony 4.0K Oct 20 14:14 2019fa-cookiecutter-csci-pset-anthonychave-Ryq8Yfcg
drwxr-xr-x 6 anthony anthony 4.0K Oct 20 12:09 2019fa-cookiecutterp0-anthonychaves-7ZzfDe-8
drwxr-xr-x 6 anthony anthony 4.0K Oct 20 11:59 2019fa-cookiecutterproject0-anthonychaves-jYbzRlCb
drwxr-xr-x 6 anthony anthony 4.0K Nov 16 11:08 2019fa-csci-utils-anthonychaves-MKbmVYPf
drwxr-xr-x 6 anthony anthony 4.0K Oct 20 21:33 2019fa-flake8-compat-anthonychaves-LtK6nKSb
drwxr-xr-x 6 anthony anthony 4.0K Sep  8 15:10 2019fa-pset-0-anthonychaves-wNrsb2XL
drwxr-xr-x 6 anthony anthony 4.0K Sep 23 13:41 2019fa-pset-1-anthonychaves-nTCdyFNF
drwxr-xr-x 6 anthony anthony 4.0K Nov 14 16:19 2019fa-pset-3-anthonychaves-2Jy_UqM0
drwxr-xr-x 7 anthony anthony 4.0K Oct 26 15:42 2019fa-pset-3-anthonychaves-50S3xAQj
drwxr-xr-x 6 anthony anthony 4.0K Nov  4 12:37 2019fa-pset-4-anthonychaves-a-T58xMy
drwxr-xr-x 6 anthony anthony 4.0K Nov  3 20:00 2019fa-pset-4-anthonychaves-gz6WrjrT
drwxr-xr-x 6 anthony anthony 4.0K Nov 17 23:10 2019fa-pset-5-anthonychaves-_fekrB1J
drwxr-xr-x 6 anthony anthony 4.0K Dec  5 11:48 2019fa-pset-6-anthonychaves-HQLZBWOA
drwxr-xr-x 6 anthony anthony 4.0K Oct 20 13:51 2019fa-testing-anthonychaves-SOW-3Ew7
drwxr-xr-x 6 anthony anthony 4.0K Oct 20 21:32 2019fa-test-project-anthonychaves-kP90_7xr
drwxr-xr-x 6 anthony anthony 4.0K Oct 20 21:37 2019fa-test-project-anthonychaves-VyJ7rrxE
drwxr-xr-x 5 anthony anthony 4.0K Nov 19 13:51 ArgParseSandbox-o5k85Js1
drwxr-xr-x 5 anthony anthony 4.0K Oct 20 10:40 cookiecutter-template0-TVqRxLqX
drwxr-xr-x 6 anthony anthony 4.0K Oct 20 15:05 cookiecutter_test-x5qB-lqM
drwxr-xr-x 6 anthony anthony 4.0K Nov 10 13:00 Sandbox-JU9NO2b2
```

The virtualenvs directory is the location on disk where our virtual environments reside.  Digging further, we can show that our dependencies are installed in the site-packages subdirectory.  This fact is important when debugging third party libraries, or any dependency installed by pipenv.  Our goal is to use pipenv exclusively for installing Python packages, keeping our development footprint as small as possible, reducing the area through which bugs can enter our environment.

The lib/python3.7 directory is interesting.  This directory contains symlinks to files in the python3.7 user directory.  This is not surprising.  Python virtual environments are lightweight.  The user Python is the basis for our virtual environments.  Different user Python versions may be available on a system, and virtual environments can use a version specified at virtual environment creation-time.  Any changes, for example destroying and recreating the virtual environment using a different version of Python, are reflected here.

Let's create a virtual environment from the Pipfile in this project repository.  From the project directory, execute the following command in your bash shell.
```bash
anthony@vision:~/projects/csci-e-29$ pipenv install --dev
Creating a virtualenv for this project…
Pipfile: /home/anthony/projects/csci-e-29/Pipfile
Using /usr/bin/python3.7 (3.7.5) to create virtualenv…
⠇ Creating virtual environment...Already using interpreter /usr/bin/python3.7
Using base prefix '/usr'
New python executable in /home/anthony/.local/share/virtualenvs/csci-e-29-bCKsFG7f/bin/python3.7
Also creating executable in /home/anthony/.local/share/virtualenvs/csci-e-29-bCKsFG7f/bin/python
Installing setuptools, pip, wheel...
done.
Running virtualenv with interpreter /usr/bin/python3.7

✔ Successfully created virtual environment!
Virtualenv location: /home/anthony/.local/share/virtualenvs/csci-e-29-bCKsFG7f
Pipfile.lock (e017f0) out of date, updating to (5ce92a)…
Locking [dev-packages] dependencies…
✔ Success!
Locking [packages] dependencies…
Updated Pipfile.lock (e017f0)!
Installing dependencies from Pipfile.lock (e017f0)…
  🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 13/13 — 00:00:01
To activate this project\'s virtualenv, run pipenv shell.
Alternatively, run a command inside the virtualenv with pipenv run.
```

This creates a Python virtual environment that we can inspect based on what we know from above.  There are a few things of note.  First, pipenv created a virtual environment with the directory name plus a hash appended to it as the top level virtual environment directory.  Second, note how the pytest and pytest-cov packages appear in the ~/.local/share/virtualenvs/csci-e-29-bCKsFG7f/lib/python3.7/site-packages
directory.  As projects get larger, there will be more packages installed to this directory.  Keep this in mind when you encounter package installation problems in the future.

```bash
anthony@vision:~/projects/csci-e-29$ ls -lh ~/.local/share/virtualenvs/csci-e-29-bCKsFG7f/lib/python3.7/*
lrwxrwxrwx  1 anthony anthony   25 Dec 15 20:53 /home/anthony/.local/share/virtualenvs/csci-e-29-bCKsFG7f/lib/python3.7/abc.py -> /usr/lib/python3.7/abc.py
lrwxrwxrwx  1 anthony anthony   28 Dec 15 20:53 /home/anthony/.local/share/virtualenvs/csci-e-29-bCKsFG7f/lib/python3.7/base64.py -> /usr/lib/python3.7/base64.py
lrwxrwxrwx  1 anthony anthony   28 Dec 15 20:53 /home/anthony/.local/share/virtualenvs/csci-e-29-bCKsFG7f/lib/python3.7/bisect.py -> /usr/lib/python3.7/bisect.py
lrwxrwxrwx  1 anthony anthony   33 Dec 15 20:53 /home/anthony/.local/share/virtualenvs/csci-e-29-bCKsFG7f/lib/python3.7/_bootlocale.py -> /usr/lib/python3.7/_bootlocale.py
lrwxrwxrwx  1 anthony anthony   28 Dec 15 20:53 /home/anthony/.local/share/virtualenvs/csci-e-29-bCKsFG7f/lib/python3.7/codecs.py -> /usr/lib/python3.7/codecs.py
lrwxrwxrwx  1 anthony anthony   30 Dec 15 20:53 /home/anthony/.local/share/virtualenvs/csci-e-29-bCKsFG7f/lib/python3.7/collections -> /usr/lib/python3.7/collections
lrwxrwxrwx  1 anthony anthony   38 Dec 15 20:53 /home/anthony/.local/share/virtualenvs/csci-e-29-bCKsFG7f/lib/python3.7/_collections_abc.py -> /usr/lib/python3.7/_collections_abc.py
lrwxrwxrwx  1 anthony anthony   47 Dec 15 20:53 /home/anthony/.local/share/virtualenvs/csci-e-29-bCKsFG7f/lib/python3.7/config-3.7m-x86_64-linux-gnu -> /usr/lib/python3.7/config-3.7m-x86_64-linux-gnu
lrwxrwxrwx  1 anthony anthony   26 Dec 15 20:53 /home/anthony/.local/share/virtualenvs/csci-e-29-bCKsFG7f/lib/python3.7/copy.py -> /usr/lib/python3.7/copy.py
lrwxrwxrwx  1 anthony anthony   29 Dec 15 20:53 /home/anthony/.local/share/virtualenvs/csci-e-29-bCKsFG7f/lib/python3.7/copyreg.py -> /usr/lib/python3.7/copyreg.py
lrwxrwxrwx  1 anthony anthony   35 Dec 15 20:53 /home/anthony/.local/share/virtualenvs/csci-e-29-bCKsFG7f/lib/python3.7/_dummy_thread.py -> /usr/lib/python3.7/_dummy_thread.py
lrwxrwxrwx  1 anthony anthony   28 Dec 15 20:53 /home/anthony/.local/share/virtualenvs/csci-e-29-bCKsFG7f/lib/python3.7/encodings -> /usr/lib/python3.7/encodings
lrwxrwxrwx  1 anthony anthony   26 Dec 15 20:53 /home/anthony/.local/share/virtualenvs/csci-e-29-bCKsFG7f/lib/python3.7/enum.py -> /usr/lib/python3.7/enum.py
lrwxrwxrwx  1 anthony anthony   29 Dec 15 20:53 /home/anthony/.local/share/virtualenvs/csci-e-29-bCKsFG7f/lib/python3.7/fnmatch.py -> /usr/lib/python3.7/fnmatch.py
lrwxrwxrwx  1 anthony anthony   31 Dec 15 20:53 /home/anthony/.local/share/virtualenvs/csci-e-29-bCKsFG7f/lib/python3.7/functools.py -> /usr/lib/python3.7/functools.py
lrwxrwxrwx  1 anthony anthony   32 Dec 15 20:53 /home/anthony/.local/share/virtualenvs/csci-e-29-bCKsFG7f/lib/python3.7/__future__.py -> /usr/lib/python3.7/__future__.py
lrwxrwxrwx  1 anthony anthony   33 Dec 15 20:53 /home/anthony/.local/share/virtualenvs/csci-e-29-bCKsFG7f/lib/python3.7/genericpath.py -> /usr/lib/python3.7/genericpath.py
lrwxrwxrwx  1 anthony anthony   29 Dec 15 20:53 /home/anthony/.local/share/virtualenvs/csci-e-29-bCKsFG7f/lib/python3.7/hashlib.py -> /usr/lib/python3.7/hashlib.py
lrwxrwxrwx  1 anthony anthony   27 Dec 15 20:53 /home/anthony/.local/share/virtualenvs/csci-e-29-bCKsFG7f/lib/python3.7/heapq.py -> /usr/lib/python3.7/heapq.py
lrwxrwxrwx  1 anthony anthony   26 Dec 15 20:53 /home/anthony/.local/share/virtualenvs/csci-e-29-bCKsFG7f/lib/python3.7/hmac.py -> /usr/lib/python3.7/hmac.py
lrwxrwxrwx  1 anthony anthony   28 Dec 15 20:53 /home/anthony/.local/share/virtualenvs/csci-e-29-bCKsFG7f/lib/python3.7/importlib -> /usr/lib/python3.7/importlib
lrwxrwxrwx  1 anthony anthony   25 Dec 15 20:53 /home/anthony/.local/share/virtualenvs/csci-e-29-bCKsFG7f/lib/python3.7/imp.py -> /usr/lib/python3.7/imp.py
lrwxrwxrwx  1 anthony anthony   24 Dec 15 20:53 /home/anthony/.local/share/virtualenvs/csci-e-29-bCKsFG7f/lib/python3.7/io.py -> /usr/lib/python3.7/io.py
lrwxrwxrwx  1 anthony anthony   29 Dec 15 20:53 /home/anthony/.local/share/virtualenvs/csci-e-29-bCKsFG7f/lib/python3.7/keyword.py -> /usr/lib/python3.7/keyword.py
lrwxrwxrwx  1 anthony anthony   30 Dec 15 20:53 /home/anthony/.local/share/virtualenvs/csci-e-29-bCKsFG7f/lib/python3.7/lib-dynload -> /usr/lib/python3.7/lib-dynload
lrwxrwxrwx  1 anthony anthony   30 Dec 15 20:53 /home/anthony/.local/share/virtualenvs/csci-e-29-bCKsFG7f/lib/python3.7/LICENSE.txt -> /usr/lib/python3.7/LICENSE.txt
lrwxrwxrwx  1 anthony anthony   31 Dec 15 20:53 /home/anthony/.local/share/virtualenvs/csci-e-29-bCKsFG7f/lib/python3.7/linecache.py -> /usr/lib/python3.7/linecache.py
lrwxrwxrwx  1 anthony anthony   28 Dec 15 20:53 /home/anthony/.local/share/virtualenvs/csci-e-29-bCKsFG7f/lib/python3.7/locale.py -> /usr/lib/python3.7/locale.py
-rw-r--r--  1 anthony anthony    0 Dec 15 20:53 /home/anthony/.local/share/virtualenvs/csci-e-29-bCKsFG7f/lib/python3.7/no-global-site-packages.txt
lrwxrwxrwx  1 anthony anthony   28 Dec 15 20:53 /home/anthony/.local/share/virtualenvs/csci-e-29-bCKsFG7f/lib/python3.7/ntpath.py -> /usr/lib/python3.7/ntpath.py
lrwxrwxrwx  1 anthony anthony   30 Dec 15 20:53 /home/anthony/.local/share/virtualenvs/csci-e-29-bCKsFG7f/lib/python3.7/operator.py -> /usr/lib/python3.7/operator.py
-rw-r--r--  1 anthony anthony    4 Dec 15 20:53 /home/anthony/.local/share/virtualenvs/csci-e-29-bCKsFG7f/lib/python3.7/orig-prefix.txt
lrwxrwxrwx  1 anthony anthony   24 Dec 15 20:53 /home/anthony/.local/share/virtualenvs/csci-e-29-bCKsFG7f/lib/python3.7/os.py -> /usr/lib/python3.7/os.py
lrwxrwxrwx  1 anthony anthony   31 Dec 15 20:53 /home/anthony/.local/share/virtualenvs/csci-e-29-bCKsFG7f/lib/python3.7/posixpath.py -> /usr/lib/python3.7/posixpath.py
lrwxrwxrwx  1 anthony anthony   28 Dec 15 20:53 /home/anthony/.local/share/virtualenvs/csci-e-29-bCKsFG7f/lib/python3.7/random.py -> /usr/lib/python3.7/random.py
lrwxrwxrwx  1 anthony anthony   29 Dec 15 20:53 /home/anthony/.local/share/virtualenvs/csci-e-29-bCKsFG7f/lib/python3.7/reprlib.py -> /usr/lib/python3.7/reprlib.py
lrwxrwxrwx  1 anthony anthony   24 Dec 15 20:53 /home/anthony/.local/share/virtualenvs/csci-e-29-bCKsFG7f/lib/python3.7/re.py -> /usr/lib/python3.7/re.py
lrwxrwxrwx  1 anthony anthony   33 Dec 15 20:53 /home/anthony/.local/share/virtualenvs/csci-e-29-bCKsFG7f/lib/python3.7/rlcompleter.py -> /usr/lib/python3.7/rlcompleter.py
lrwxrwxrwx  1 anthony anthony   28 Dec 15 20:53 /home/anthony/.local/share/virtualenvs/csci-e-29-bCKsFG7f/lib/python3.7/shutil.py -> /usr/lib/python3.7/shutil.py
-rw-r--r--  1 anthony anthony  29K Dec 15 20:53 /home/anthony/.local/share/virtualenvs/csci-e-29-bCKsFG7f/lib/python3.7/site.py
lrwxrwxrwx  1 anthony anthony   33 Dec 15 20:53 /home/anthony/.local/share/virtualenvs/csci-e-29-bCKsFG7f/lib/python3.7/sre_compile.py -> /usr/lib/python3.7/sre_compile.py
lrwxrwxrwx  1 anthony anthony   35 Dec 15 20:53 /home/anthony/.local/share/virtualenvs/csci-e-29-bCKsFG7f/lib/python3.7/sre_constants.py -> /usr/lib/python3.7/sre_constants.py
lrwxrwxrwx  1 anthony anthony   31 Dec 15 20:53 /home/anthony/.local/share/virtualenvs/csci-e-29-bCKsFG7f/lib/python3.7/sre_parse.py -> /usr/lib/python3.7/sre_parse.py
lrwxrwxrwx  1 anthony anthony   26 Dec 15 20:53 /home/anthony/.local/share/virtualenvs/csci-e-29-bCKsFG7f/lib/python3.7/stat.py -> /usr/lib/python3.7/stat.py
lrwxrwxrwx  1 anthony anthony   28 Dec 15 20:53 /home/anthony/.local/share/virtualenvs/csci-e-29-bCKsFG7f/lib/python3.7/struct.py -> /usr/lib/python3.7/struct.py
lrwxrwxrwx  1 anthony anthony   29 Dec 15 20:53 /home/anthony/.local/share/virtualenvs/csci-e-29-bCKsFG7f/lib/python3.7/tarfile.py -> /usr/lib/python3.7/tarfile.py
lrwxrwxrwx  1 anthony anthony   30 Dec 15 20:53 /home/anthony/.local/share/virtualenvs/csci-e-29-bCKsFG7f/lib/python3.7/tempfile.py -> /usr/lib/python3.7/tempfile.py
lrwxrwxrwx  1 anthony anthony   30 Dec 15 20:53 /home/anthony/.local/share/virtualenvs/csci-e-29-bCKsFG7f/lib/python3.7/tokenize.py -> /usr/lib/python3.7/tokenize.py
lrwxrwxrwx  1 anthony anthony   27 Dec 15 20:53 /home/anthony/.local/share/virtualenvs/csci-e-29-bCKsFG7f/lib/python3.7/token.py -> /usr/lib/python3.7/token.py
lrwxrwxrwx  1 anthony anthony   27 Dec 15 20:53 /home/anthony/.local/share/virtualenvs/csci-e-29-bCKsFG7f/lib/python3.7/types.py -> /usr/lib/python3.7/types.py
lrwxrwxrwx  1 anthony anthony   30 Dec 15 20:53 /home/anthony/.local/share/virtualenvs/csci-e-29-bCKsFG7f/lib/python3.7/warnings.py -> /usr/lib/python3.7/warnings.py
lrwxrwxrwx  1 anthony anthony   29 Dec 15 20:53 /home/anthony/.local/share/virtualenvs/csci-e-29-bCKsFG7f/lib/python3.7/weakref.py -> /usr/lib/python3.7/weakref.py
lrwxrwxrwx  1 anthony anthony   33 Dec 15 20:53 /home/anthony/.local/share/virtualenvs/csci-e-29-bCKsFG7f/lib/python3.7/_weakrefset.py -> /usr/lib/python3.7/_weakrefset.py

/home/anthony/.local/share/virtualenvs/csci-e-29-bCKsFG7f/lib/python3.7/distutils:
total 12K
-rw-r--r-- 1 anthony anthony  228 Dec 15 20:53 distutils.cfg
-rw-r--r-- 1 anthony anthony 4.3K Dec 15 20:53 __init__.py

/home/anthony/.local/share/virtualenvs/csci-e-29-bCKsFG7f/lib/python3.7/site-packages:
total 440K
drwxr-xr-x 3 anthony anthony 4.0K Dec 15 20:54 attr
drwxr-xr-x 2 anthony anthony 4.0K Dec 15 20:54 attrs-19.3.0.dist-info
drwxr-xr-x 5 anthony anthony 4.0K Dec 15 20:54 coverage
drwxr-xr-x 2 anthony anthony 4.0K Dec 15 20:54 coverage-5.0.dist-info
-rw-r--r-- 1 anthony anthony  126 Dec 15 20:53 easy_install.py
drwxr-xr-x 5 anthony anthony 4.0K Dec 15 20:54 importlib_metadata
drwxr-xr-x 2 anthony anthony 4.0K Dec 15 20:54 importlib_metadata-1.3.0.dist-info
drwxr-xr-x 3 anthony anthony 4.0K Dec 15 20:54 more_itertools
drwxr-xr-x 2 anthony anthony 4.0K Dec 15 20:54 more_itertools-8.0.2.dist-info
drwxr-xr-x 3 anthony anthony 4.0K Dec 15 20:54 packaging
drwxr-xr-x 2 anthony anthony 4.0K Dec 15 20:54 packaging-19.2.dist-info
drwxr-xr-x 5 anthony anthony 4.0K Dec 15 20:53 pip
drwxr-xr-x 2 anthony anthony 4.0K Dec 15 20:53 pip-19.3.1.dist-info
drwxr-xr-x 5 anthony anthony 4.0K Dec 15 20:53 pkg_resources
drwxr-xr-x 3 anthony anthony 4.0K Dec 15 20:54 pluggy
drwxr-xr-x 2 anthony anthony 4.0K Dec 15 20:54 pluggy-0.13.1.dist-info
drwxr-xr-x 9 anthony anthony 4.0K Dec 15 20:54 py
drwxr-xr-x 2 anthony anthony 4.0K Dec 15 20:54 py-1.8.0.dist-info
drwxr-xr-x 2 anthony anthony 4.0K Dec 15 20:54 __pycache__
drwxr-xr-x 2 anthony anthony 4.0K Dec 15 20:54 pyparsing-2.4.5.dist-info
-rw-r--r-- 1 anthony anthony 258K Dec 15 20:54 pyparsing.py
drwxr-xr-x 8 anthony anthony 4.0K Dec 15 20:54 _pytest
drwxr-xr-x 3 anthony anthony 4.0K Dec 15 20:54 pytest
drwxr-xr-x 2 anthony anthony 4.0K Dec 15 20:54 pytest-5.3.2.dist-info
drwxr-xr-x 3 anthony anthony 4.0K Dec 15 20:54 pytest_cov
drwxr-xr-x 2 anthony anthony 4.0K Dec 15 20:54 pytest_cov-2.8.1.dist-info
-rw-r--r-- 1 anthony anthony  376 Dec 15 20:54 pytest-cov.pth
drwxr-xr-x 6 anthony anthony 4.0K Dec 15 20:53 setuptools
drwxr-xr-x 2 anthony anthony 4.0K Dec 15 20:53 setuptools-42.0.2.dist-info
drwxr-xr-x 2 anthony anthony 4.0K Dec 15 20:54 six-1.13.0.dist-info
-rw-r--r-- 1 anthony anthony  33K Dec 15 20:54 six.py
drwxr-xr-x 4 anthony anthony 4.0K Dec 15 20:54 wcwidth
drwxr-xr-x 2 anthony anthony 4.0K Dec 15 20:54 wcwidth-0.1.7.dist-info
drwxr-xr-x 4 anthony anthony 4.0K Dec 15 20:53 wheel
drwxr-xr-x 2 anthony anthony 4.0K Dec 15 20:53 wheel-0.33.6.dist-info
drwxr-xr-x 2 anthony anthony 4.0K Dec 15 20:54 zipp-0.6.0.dist-info
-rw-r--r-- 1 anthony anthony 4.9K Dec 15 20:54 zipp.py
```

We are nearly finished learning about the Python virutal environments created by pipenv. A shortcoming of this process is that binaries installed by pipenv are not on our PATH yet. We need to make one more change to ~/.bashrc to prepend the Python command path to our existing PATH environment variable.

At the bottom of ~/.bashrc, add the following line.
```bash
export PATH=$HOME/.local/bin:$PATH  
```

### Removing and recreating a virtual environment
In the event that our virtual environment becomes corrupted, whether due to our own error or a failing of a tool or package, we may need to completely remove that virtual environment and start over.  Thankfully, Python virtual environments made with pipenv are cheap to create, and cheap to delete.  The pipenv command supports doing this with a command line flag.  Don't hesitate to remove and recreate a virtual environment if you encounter an unsolvable environment error.  

```bash
anthony@vision:~/projects/csci-e-29$ pipenv --rm
Removing virtualenv (/home/anthony/.local/share/virtualenvs/csci-e-29-bCKsFG7f)…
```

The pipenv tool has a number of additional options and commands.
```bash
anthony@vision:~/projects/csci-e-29$ pipenv --help
Usage: pipenv [OPTIONS] COMMAND [ARGS]...

Options:
  --where             Output project home information.
  --venv              Output virtualenv information.
  --py                Output Python interpreter information.
  --envs              Output Environment Variable options.
  --rm                Remove the virtualenv.
  --bare              Minimal output.
  --completion        Output completion (to be eval''d).
  --man               Display manpage.
  --support           Output diagnostic information \for use in GitHub issues.
  --site-packages     Enable site-packages for the virtualenv.  [env var:
                      PIPENV_SITE_PACKAGES]
  --python TEXT       Specify which version of Python virtualenv should use.
  --three / --two     Use Python 3/2 when creating virtualenv.
  --clear             Clears caches (pipenv, pip, and pip-tools).  [env var:
                      PIPENV_CLEAR]
  -v, --verbose       Verbose mode.
  --pypi-mirror TEXT  Specify a PyPI mirror.
  --version           Show the version and exit.
  -h, --help          Show this message and exit.


Usage Examples:
   Create a new project using Python 3.7, specifically:
   $ pipenv --python 3.7

   Remove project virtualenv (inferred from current directory):
   $ pipenv --rm

   Install all dependencies for a project (including dev):
   $ pipenv install --dev

   Create a lockfile containing pre-releases:
   $ pipenv lock --pre

   Show a graph of your installed dependencies:
   $ pipenv graph

   Check your installed dependencies for security vulnerabilities:
   $ pipenv check

   Install a local setup.py into your virtual environment/Pipfile:
   $ pipenv install -e .

   Use a lower-level pip command:
   $ pipenv run pip freeze

Commands:
  check      Checks for security vulnerabilities and against PEP 508 markers
             provided in Pipfile.
  clean      Uninstalls all packages not specified in Pipfile.lock.
  graph      Displays currently-installed dependency graph information.
  install    Installs provided packages and adds them to Pipfile, or (if no
             packages are given), installs all packages from Pipfile.
  lock       Generates Pipfile.lock.
  open       View a given module in your editor.
  run        Spawns a command installed into the virtualenv.
  shell      Spawns a shell within the virtualenv.
  sync       Installs all packages specified in Pipfile.lock.
  uninstall  Un-installs a provided package and removes it from Pipfile.
  update     Runs lock, then sync.
```

### Removing/reinstalling pipenv itself
Rarely (ok, not so rarely), pipenv itself may be so broken that it needs to be reinstalled.  One caveat is that the act of installing pipenv itself _breaks_ the pip tool, which is required to install pipenv.  It is possible to remove pipenv, and still have a broken pip tool, making it nearly impossible to reinstall pipenv itself, and destroying the gains of Python virtual environments.  It is possible to safely and repeatably remove and reinstall pipenv with the following commands.
```bash
sudo apt remove python3-pip
rm -rf ~/.local/lib/python3.6/*
sudo apt install python3-pip
python -m pip install --user pipenv
```

## Live Development Tutorial

[![Toward Advanced Python for Data Science](http://img.youtube.com/vi/1mRQA6JAohk/0.jpg)](https://youtu.be/1mRQA6JAohk "Toward Advanced Python for Data Science")
