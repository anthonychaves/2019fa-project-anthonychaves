# Toward Advanced Python for Data Science
## A CSCI-E-29 Project
#### by Anthony Chaves

This project is an effort to ease the learning curve for those new to using Python for data science.  The aim is to provide an overview of the current Python ecosystem and the tools currently in favor with Python-friendly data scientists.  

* Python Runtime Environment
  * Python Virtual machine overview
  * python installations for developers - which python, python --version
  * system python, user python (set environment variable in bashrc), virtual environment python, focus on pipenv, include pip, conda, command line and pycharm integration with pipenv
  * pipenv.lock file, why we check this in, how to modify it
  * all pipenv commands, especially pipenv --rm, and why
  * how to use each type of python installation (which binary executable is called?)

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
