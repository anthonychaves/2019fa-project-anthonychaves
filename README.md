# Toward Advanced Python for Data Science
## A CSCI-E-29 Project
#### by Anthony Chaves

This project is an effort to ease the learning curve for those new to using Python for data science.  The aim is to provide an overview of the current Python ecosystem and the tools currently in favor with Python-friendly data scientists.  The goal of this project is to help you be a good Python developer.  We will examine several tools that are part of this practice, including:
* The Python command line environment
* The PyCharm IDE
* Creating and destroying Python virtual environments
* Python module and package management
* Good practices using git as part of your development workflow
* Testing with PyTest
* Interactive debugging using the PyCharm debugger

* Python Runtime Environment
  * Python Virtual machine overview
  * python installations for developers - which python, python --version
  * system python, user python (set environment variable in bashrc), virtual environment python, focus on pipenv, include pip, conda, command line and pycharm integration with pipenv
  * pipenv.lock file, why we check this in, how to modify it
  * all pipenv commands, especially pipenv --rm, and why
  * how to use each type of python installation (which binary executable is called?)
  * python program execution - as main, as module

* Starting from fresh install:
  * Commands to know

```bash
anthony@vision:~/projects/csci-e-29$ which python
/usr/bin/python
anthony@vision:~/projects/csci-e-29$ /usr/bin/python --version
Python 2.7.17rc1
```
  Wrong!

```bash
anthony@vision:~/projects/csci-e-29$ which python3
/usr/bin/python3
anthony@vision:~/projects/csci-e-29$ /usr/bin/python3 --version
Python 3.7.5
```
  Right!

* python3
* which python
* python3 --version
* python3 --help
* Modify .bashrc for convenience: alias python=python3, exit terminal or restart bash
* alias python=python3
* export PATH=$HOME/.local/bin:$PATH  
* sudo apt list python-pip
* sudo apt list python3-pip
* sudo apt install python3-pip

```bash
anthony@vision:~/projects/csci-e-29$ sudo apt list python-pip
Listing... Done
python-pip/eoan,eoan,now 18.1-5 all [installed]
anthony@vision:~/projects/csci-e-29$ sudo apt list python3-pip
Listing... Done
python3-pip/eoan,eoan,now 18.1-5 all [installed]
```

* pip (wrong command, not installed)
* pip3
* python -m pip install --help
* python -m pip install --user pipenv
* ls -lh ~/.local/bin/* (directory where python/pipenv and all other commands are installed)
* ls -lh ~/.local/lib/python3.6/site-packages/ (directory where virtual environments are created and libraries/modules are installed)

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

* pip (this command no longer works!  pipenv broke it.)
* how do we safely remove pipenv/pip?
* sudo apt remove python3-pip
* rm -rf ~/.local/lib/python3.6/*
* sudo apt install python3-pip
* python3 -m pip install --user pipenv

https://pypi.org/project/pytest/

* mkdir csci-e-29
* cd csci-e-29
* ls -lh ~/.local/bin (pipenv installed commands, into our PATH)
* ls -lh ~/.local/lib/python3.6/site-packages/ (pipenv installed some packages)
* ls -lh ~/.local/share/virtualenvs/ (pipenv created a virtualenv for our project, this is where its packages live)

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

anthony@vision:~/projects/csci-e-29$ ls -lh ~/.local/share/virtualenvs/csci-e-29-bCKsFG7f/*
/home/anthony/.local/share/virtualenvs/csci-e-29-bCKsFG7f/bin:
total 5.0M
-rw-r--r-- 1 anthony anthony 2.3K Dec 15 20:53 activate
-rw-r--r-- 1 anthony anthony 1.5K Dec 15 20:53 activate.csh
-rw-r--r-- 1 anthony anthony 3.1K Dec 15 20:53 activate.fish
-rw-r--r-- 1 anthony anthony 1.8K Dec 15 20:53 activate.ps1
-rw-r--r-- 1 anthony anthony 1.5K Dec 15 20:53 activate_this.py
-rw-r--r-- 1 anthony anthony 1.2K Dec 15 20:53 activate.xsh
-rwxr-xr-x 1 anthony anthony  270 Dec 15 20:54 coverage
-rwxr-xr-x 1 anthony anthony  270 Dec 15 20:54 coverage3
-rwxr-xr-x 1 anthony anthony  270 Dec 15 20:54 coverage-3.7
-rwxr-xr-x 1 anthony anthony  288 Dec 15 20:53 easy_install
-rwxr-xr-x 1 anthony anthony  288 Dec 15 20:53 easy_install-3.7
-rwxr-xr-x 1 anthony anthony  275 Dec 15 20:53 pip
-rwxr-xr-x 1 anthony anthony  275 Dec 15 20:53 pip3
-rwxr-xr-x 1 anthony anthony  275 Dec 15 20:53 pip3.7
-rwxr-xr-x 1 anthony anthony  260 Dec 15 20:54 py.test
-rwxr-xr-x 1 anthony anthony  260 Dec 15 20:54 pytest
lrwxrwxrwx 1 anthony anthony    9 Dec 15 20:53 python -> python3.7
lrwxrwxrwx 1 anthony anthony    9 Dec 15 20:53 python3 -> python3.7
-rwxr-xr-x 1 anthony anthony 4.9M Dec 15 20:53 python3.7
-rwxr-xr-x 1 anthony anthony 2.4K Dec 15 20:53 python-config
-rwxr-xr-x 1 anthony anthony  266 Dec 15 20:53 wheel

/home/anthony/.local/share/virtualenvs/csci-e-29-bCKsFG7f/include:
total 0
lrwxrwxrwx 1 anthony anthony 23 Dec 15 20:53 python3.7m -> /usr/include/python3.7m

/home/anthony/.local/share/virtualenvs/csci-e-29-bCKsFG7f/lib:
total 4.0K
drwxr-xr-x 4 anthony anthony 4.0K Dec 15 20:53 python3.7

/home/anthony/.local/share/virtualenvs/csci-e-29-bCKsFG7f/src:
total 0

```
* Creating Pipfile: pipenv install
* Look at the output: Pipfile, Pipfile.lock.  What are these and why?
* pipfile --rm
* ls -lh ~/.local/share/virtualenvs/ (verify the virtualenv directory was removed)
* pipenv install
* ls -lh ~/.local/share/virtualenvs/ (verify the virtualenv directory exists)
* pipenv install --dev pytest pytest-cov

* classes: PositiveDefinite example
* Python package/module
* how to define package/module
* how to include __main__ and run as module
* cd src
* python -m sandbox
* if __name__ == "__main__" evaluates to TRUE, so the block runs (include link to this in official python documentation)
* test directory and structure
* pytest command line
* pytest how to call right module path
* pycharm ctrl+k
* pycharm reformat file
* export PYTHONPATH=./src
* PYTHONPATH=./src in PyCharm terminal settings
* run pytest on the command line after settings

* Python: writing a descriptor
* Python: testing a descriptor
* Python: Debugging a descriptor

* git
* commands (init, add file, add directory, commit, commit message, branch, merge)
* branching workflows
* remote origin push fetch
* the --allow-unrelated-histories method is kind of an antipattern.

* debugging
* execution (main) vs. testing
* breakpoints
* using debugger in pycharm
* inspecting variables
* watching expressions
* emphasis on code that is simple to run and test, not a lot of boilerplate, unlike luigi/django

* testing
* pytest
* testing frameworks (UnitTest - which framework?)

* Putting it all together: development mantra
* console/debugger
* write test: how do i call this?
* docstring, just write input types, semantic meaning, output type
* run test, watch it fail
* implement method, run test, watch it fail
* implement success, run test, watch it fail, because we haven't put the correct expected results in yet.
* copy actual to expected, if that's correct
* tests prove that it actually "works for me"
* commit test, code, and documentation to git
* move on to the next step

[![Toward Advanced Python for Data Science](http://img.youtube.com/vi/1mRQA6JAohk/0.jpg)](http://www.youtube.com/watch?v=1mRQA6JAohk "Toward Advanced Python for Data Science")

================================================================

* pipenv
  * what problems does it solve?
  * what problems does it introduce?
  * pipenv usage: command line and pipfile
  * resolving errors
  * browsing pypi
  * Create/destroy/update pipenvs, how and why
  * pipenv with pycharm
  * pipenv install vs. pipenv update vs. pipenv install --dev vs. pipenv install -e .
  * how to explore packages and code installed in pipenv
  * how to find python executable used by pipenv
  * how to use pipenv from pycharm for pipenv shell, also from command line



* dataframe: what is it?
