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
  * Commands to know:
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
    * pip (wrong command, not installed)
    * pip3
    * python -m pip install --help
    * python -m pip install --user pipenv
    * ls -lh ~/.local/bin/* (directory where python/pipenv and all other commands are installed)
    * ls -lh ~/.local/lib/python3.6/site-packages/ (directory where virtual environments are created and libraries/modules are installed)
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
    * Creating Pipfile: pipenv install
    * Look at the output: Pipfile, Pipfile.lock.  What are these and why?
    * pipfile --rm
    * ls -lh ~/.local/share/virtualenvs/ (verify the virtualenv directory was removed)
    * pipenv install
    * ls -lh ~/.local/share/virtualenvs/ (verify the virtualenv directory exists)
    * pipenv install --dev pytest pytest-cov

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

* dataframe: what is it?

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
