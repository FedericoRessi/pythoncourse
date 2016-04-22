# Making exercises

Students are supposed to work on their own computers using a copy of this project.
There are a lists of files (which name starts with the prefix _exercise__) that
students should complete in order to complete the pratical session.

## Download the project

From bash use git to clone exercises repository and enter in the new folder:
```
git clone https://github.com/FedericoRessi/pythoncourse.git
cd pythoncourse/
```

## Running Tox

All exercises are Python script (_exercise__*.py) to be modified according to behavior
documente in the same script.

For each script there is a test in charge to verify if modified code behave as specified.
Every test would be skipped until its target script is unchanged.

To execute all tests and verify that it works as expected you can run tox from the main
project folder:

```
tox
```

This is what you should expect when running it before touching the first exercise:

```
GLOB sdist-make: /Users/fressi/workspace/python-class-16.04/setup.py
py27 inst-nodeps: /Users/fressi/workspace/python-class-16.04/.tox/dist/python-course-1604-0.0.1.dev45.zip
py27 installed: coverage==4.0.3,funcsigs==1.0.0,mock==2.0.0,ordereddict==1.1,pbr==1.9.1,py==1.4.31,pytest==2.9.1,pytest-cov==2.2.1,python-course-1604==0.0.1.dev45,six==1.10.0
py27 runtests: PYTHONHASHSEED='2658208170'
py27 runtests: commands[0] | coverage erase
py27 runtests: commands[1] | rm -fR .coverage .coverage.*
py27 runtests: commands[2] | py.test --cov=python_course_1604 --cov-report term-missing --cov-report html --cov-report xml
============================= test session starts ==============================
platform darwin -- Python 2.7.10, pytest-2.9.1, py-1.4.31, pluggy-0.3.1
rootdir: /Users/fressi/workspace/python-class-16.04, inifile: tox.ini
plugins: cov-2.2.1
collected 20 items

python_course_1604/class_01/tests/test_01.py s
python_course_1604/class_01/tests/test_02.py sss
python_course_1604/class_01/tests/test_03.py ssss
python_course_1604/class_01/tests/test_04.py s
python_course_1604/class_01/tests/test_05.py ssss
python_course_1604/class_01/tests/test_06.py sssss
python_course_1604/tests/test_00.py ..
--------------- coverage: platform darwin, python 2.7.10-final-0 ---------------
Name                                                           Stmts   Miss Branch BrPart  Cover   Missing
----------------------------------------------------------------------------------------------------------
python_course_1604/__init__.py                                     0      0      0      0   100%   
python_course_1604/class_01/__init__.py                            0      0      0      0   100%   
python_course_1604/class_01/exercize_01_hello_world.py             0      0      0      0   100%   
python_course_1604/class_01/exercize_02_if_statement.py            1      0      2      1    67%   10->-10
python_course_1604/class_01/exercize_03_capture_exception.py       2      0      4      2    67%   11->-11, 16->-16
python_course_1604/class_01/exercize_04_stack_limit.py             3      1      2      1    60%   20, 23->-23
python_course_1604/class_01/exercize_05_while_loop.py              5      2      2      1    57%   15, 21, 24->-24
python_course_1604/class_01/exercize_06_while_break_else.py        5      2      2      1    57%   15, 21, 24->-24
----------------------------------------------------------------------------------------------------------
TOTAL                                                             16      5     12      6    61%   
Coverage HTML written to dir report/html/coverage
Coverage XML written to file report/coverage.xml

===================== 2 passed, 18 skipped in 0.22 seconds =====================
py34 inst-nodeps: /Users/fressi/workspace/python-class-16.04/.tox/dist/python-course-1604-0.0.1.dev45.zip
py34 installed: coverage==4.0.3,mock==2.0.0,pbr==1.9.1,py==1.4.31,pytest==2.9.1,pytest-cov==2.2.1,python-course-1604==0.0.1.dev45,six==1.10.0
py34 runtests: PYTHONHASHSEED='2658208170'
py34 runtests: commands[0] | coverage erase
py34 runtests: commands[1] | rm -fR .coverage .coverage.*
py34 runtests: commands[2] | py.test --cov=python_course_1604 --cov-report term-missing --cov-report html --cov-report xml
============================= test session starts ==============================
platform darwin -- Python 3.4.4, pytest-2.9.1, py-1.4.31, pluggy-0.3.1
rootdir: /Users/fressi/workspace/python-class-16.04, inifile: tox.ini
plugins: cov-2.2.1
collected 20 items

python_course_1604/class_01/tests/test_01.py s
python_course_1604/class_01/tests/test_02.py sss
python_course_1604/class_01/tests/test_03.py ssss
python_course_1604/class_01/tests/test_04.py s
python_course_1604/class_01/tests/test_05.py ssss
python_course_1604/class_01/tests/test_06.py sssss
python_course_1604/tests/test_00.py ..
--------------- coverage: platform darwin, python 3.4.4-final-0 ----------------
Name                                                           Stmts   Miss Branch BrPart  Cover   Missing
----------------------------------------------------------------------------------------------------------
python_course_1604/__init__.py                                     0      0      0      0   100%   
python_course_1604/class_01/__init__.py                            0      0      0      0   100%   
python_course_1604/class_01/exercize_01_hello_world.py             0      0      0      0   100%   
python_course_1604/class_01/exercize_02_if_statement.py            1      0      2      1    67%   10->-10
python_course_1604/class_01/exercize_03_capture_exception.py       2      0      4      2    67%   11->-11, 16->-16
python_course_1604/class_01/exercize_04_stack_limit.py             3      1      2      1    60%   20, 23->-23
python_course_1604/class_01/exercize_05_while_loop.py              5      2      2      1    57%   15, 21, 24->-24
python_course_1604/class_01/exercize_06_while_break_else.py        5      2      2      1    57%   15, 21, 24->-24
----------------------------------------------------------------------------------------------------------
TOTAL                                                             16      5     12      6    61%   
Coverage HTML written to dir report/html/coverage
Coverage XML written to file report/coverage.xml

===================== 2 passed, 18 skipped in 0.26 seconds =====================
flake8 inst-nodeps: /Users/fressi/workspace/python-class-16.04/.tox/dist/python-course-1604-0.0.1.dev45.zip
flake8 installed: flake8==2.5.4,mccabe==0.4.0,pep8==1.7.0,pyflakes==1.0.0,python-course-1604==0.0.1.dev45
flake8 runtests: PYTHONHASHSEED='2658208170'
flake8 runtests: commands[0] | flake8 --max-complexity=8 python_course_1604
pylint inst-nodeps: /Users/fressi/workspace/python-class-16.04/.tox/dist/python-course-1604-0.0.1.dev45.zip
pylint installed: astroid==1.4.5,colorama==0.3.7,lazy-object-proxy==1.2.2,pylint==1.5.5,python-course-1604==0.0.1.dev45,six==1.10.0,wrapt==1.10.8
pylint runtests: PYTHONHASHSEED='2658208170'
pylint runtests: commands[0] | pylint --reports=n --rcfile=pylint.rc python_course_1604
___________________________________ summary ____________________________________
  py27: commands succeeded
  py34: commands succeeded
  flake8: commands succeeded
  pylint: commands succeeded
  congratulations :)
```

Messages starting with py27 are referred to tests executed with Python 2.7 while messages starting with py34 to tests executed with Python 3.4.
All tests (and scripts) have to work in both Python 2.7 and Python 3.4 to pass the tests.
flake8 and pylint are instead two famous static analysis tools in charge of lookint at your code style and to spot syntax errors.
This could help you understanding what you are doing wrong.

### Executed scripts

Every exercise script that has been changed is tested by a test. For example test
```
python_course_1604/class_01/tests/test_01.py
```
tests exercize
```
python_course_1604/class_01/exercize_01_hello_world.py
```

You can see witch tests are executed at this lines:
```
python_course_1604/class_01/tests/test_01.py s
python_course_1604/class_01/tests/test_02.py sss
python_course_1604/class_01/tests/test_03.py ssss
python_course_1604/class_01/tests/test_04.py s
python_course_1604/class_01/tests/test_05.py ssss
python_course_1604/class_01/tests/test_06.py sssss
python_course_1604/tests/test_00.py ..
```
The _s_ on the side of test path means that test has been skipped.
The _._ means instead that the test has been executed.

### Code coverage

There is a section starting with something like that:
```
--------------- coverage: platform darwin, python 3.4.4-final-0 ----------------
Name                                                           Stmts   Miss Branch BrPart  Cover   Missing
----------------------------------------------------------------------------------------------------------
python_course_1604/__init__.py                                     0      0      0      0   100%   
python_course_1604/class_01/__init__.py                            0      0      0      0   100%   
python_course_1604/class_01/exercize_01_hello_world.py             0      0      0      0   100%   
python_course_1604/class_01/exercize_02_if_statement.py            1      0      2      1    67%   10->-10
python_course_1604/class_01/exercize_03_capture_exception.py       2      0      4      2    67%   11->-11, 16->-16
python_course_1604/class_01/exercize_04_stack_limit.py             3      1      2      1    60%   20, 23->-23
python_course_1604/class_01/exercize_05_while_loop.py              5      2      2      1    57%   15, 21, 24->-24
python_course_1604/class_01/exercize_06_while_break_else.py        5      2      2      1    57%   15, 21, 24->-24
----------------------------------------------------------------------------------------------------------
TOTAL                                                             16      5     12      6    61%   
Coverage HTML written to dir report/html/coverage
Coverage XML written to file report/coverage.xml
```

This gives you an overview about which lines of the scripts you are working have been actually executed by tests.
You can have a better view about executed lines by opening with your browser generated files the URL
produced executing following command:
```
echo file:///$(pwd)/report/html/coverage/index.html 
```
On my case it prints this URL:
```
file:////Users/fressi/workspace/python-class-16.04/report/html/coverage/index.html
```
# Never work on master branch.

Before making any change to the code make sure you are working on your own branch and not on master branch.
```
git checkout -b <your-branch-name> || git checkout <your-branch-name>
```

## Do the 1st exercise

Edit the first exercise:
```
python_course_1604/class_01/exercize_01_hello_world.py
```
as follow:
```Python
'''
Created on 6 Apr 2016

@author: Federico Ressi <federico.ressi@intel.com>
'''

# Write a line that prints 'Hello world!'
print 'Hello world!'
```
and run tox
```
tox
```
You should expect something like this:
```
GLOB sdist-make: /Users/fressi/workspace/python-class-16.04/setup.py
py27 inst-nodeps: /Users/fressi/workspace/python-class-16.04/.tox/dist/python-course-1604-0.0.1.dev45.zip
py27 installed: coverage==4.0.3,funcsigs==1.0.0,mock==2.0.0,ordereddict==1.1,pbr==1.9.1,py==1.4.31,pytest==2.9.1,pytest-cov==2.2.1,python-course-1604==0.0.1.dev45,six==1.10.0
py27 runtests: PYTHONHASHSEED='1278900245'
py27 runtests: commands[0] | coverage erase
py27 runtests: commands[1] | rm -fR .coverage .coverage.*
py27 runtests: commands[2] | py.test --cov=python_course_1604 --cov-report term-missing --cov-report html --cov-report xml
==================================================================== test session starts ====================================================================
platform darwin -- Python 2.7.10, pytest-2.9.1, py-1.4.31, pluggy-0.3.1
rootdir: /Users/fressi/workspace/python-class-16.04, inifile: tox.ini
plugins: cov-2.2.1
collected 20 items 

python_course_1604/class_01/tests/test_01.py .
python_course_1604/class_01/tests/test_02.py sss
python_course_1604/class_01/tests/test_03.py ssss
python_course_1604/class_01/tests/test_04.py s
python_course_1604/class_01/tests/test_05.py ssss
python_course_1604/class_01/tests/test_06.py sssss
python_course_1604/tests/test_00.py ..
----------------------------------------------------- coverage: platform darwin, python 2.7.10-final-0 ------------------------------------------------------
Name                                                           Stmts   Miss Branch BrPart  Cover   Missing
----------------------------------------------------------------------------------------------------------
python_course_1604/__init__.py                                     0      0      0      0   100%   
python_course_1604/class_01/__init__.py                            0      0      0      0   100%   
python_course_1604/class_01/exercize_01_hello_world.py             1      0      0      0   100%   
python_course_1604/class_01/exercize_02_if_statement.py            1      0      2      1    67%   10->-10
python_course_1604/class_01/exercize_03_capture_exception.py       2      0      4      2    67%   11->-11, 16->-16
python_course_1604/class_01/exercize_04_stack_limit.py             3      1      2      1    60%   20, 23->-23
python_course_1604/class_01/exercize_05_while_loop.py              5      2      2      1    57%   15, 21, 24->-24
python_course_1604/class_01/exercize_06_while_break_else.py        5      2      2      1    57%   15, 21, 24->-24
----------------------------------------------------------------------------------------------------------
TOTAL                                                             17      5     12      6    62%   
Coverage HTML written to dir report/html/coverage
Coverage XML written to file report/coverage.xml

=========================================================== 3 passed, 17 skipped in 0.31 seconds ============================================================
py34 inst-nodeps: /Users/fressi/workspace/python-class-16.04/.tox/dist/python-course-1604-0.0.1.dev45.zip
py34 installed: coverage==4.0.3,mock==2.0.0,pbr==1.9.1,py==1.4.31,pytest==2.9.1,pytest-cov==2.2.1,python-course-1604==0.0.1.dev45,six==1.10.0
py34 runtests: PYTHONHASHSEED='1278900245'
py34 runtests: commands[0] | coverage erase
py34 runtests: commands[1] | rm -fR .coverage .coverage.*
py34 runtests: commands[2] | py.test --cov=python_course_1604 --cov-report term-missing --cov-report html --cov-report xml
==================================================================== test session starts ====================================================================
platform darwin -- Python 3.4.4, pytest-2.9.1, py-1.4.31, pluggy-0.3.1
rootdir: /Users/fressi/workspace/python-class-16.04, inifile: tox.ini
plugins: cov-2.2.1
collected 19 items / 1 errors 

python_course_1604/class_01/tests/test_02.py sss
python_course_1604/class_01/tests/test_03.py ssss
python_course_1604/class_01/tests/test_04.py s
python_course_1604/class_01/tests/test_05.py ssss
python_course_1604/class_01/tests/test_06.py sssss
python_course_1604/tests/test_00.py ..
------------------------------------------------------ coverage: platform darwin, python 3.4.4-final-0 ------------------------------------------------------
Name                                                           Stmts   Miss Branch BrPart  Cover   Missing
----------------------------------------------------------------------------------------------------------
python_course_1604/__init__.py                                     0      0      0      0   100%   
python_course_1604/class_01/__init__.py                            0      0      0      0   100%   
python_course_1604/class_01/exercize_02_if_statement.py            1      0      2      1    67%   10->-10
python_course_1604/class_01/exercize_03_capture_exception.py       2      0      4      2    67%   11->-11, 16->-16
python_course_1604/class_01/exercize_04_stack_limit.py             3      1      2      1    60%   20, 23->-23
python_course_1604/class_01/exercize_05_while_loop.py              5      2      2      1    57%   15, 21, 24->-24
python_course_1604/class_01/exercize_06_while_break_else.py        5      2      2      1    57%   15, 21, 24->-24
----------------------------------------------------------------------------------------------------------
TOTAL                                                             16      5     12      6    61%   
Coverage HTML written to dir report/html/coverage
Coverage XML written to file report/coverage.xml

========================================================================== ERRORS ===========================================================================
_______________________________________________ ERROR collecting python_course_1604/class_01/tests/test_01.py _______________________________________________
.tox/py34/lib/python3.4/site-packages/_pytest/python.py:611: in _importtestmodule
    mod = self.fspath.pyimport(ensuresyspath=importmode)
.tox/py34/lib/python3.4/site-packages/py/_path/local.py:650: in pyimport
    __import__(modname)
<frozen importlib._bootstrap>:2237: in _find_and_load
    ???
<frozen importlib._bootstrap>:2226: in _find_and_load_unlocked
    ???
<frozen importlib._bootstrap>:1191: in _load_unlocked
    ???
<frozen importlib._bootstrap>:1161: in _load_backward_compatible
    ???
.tox/py34/lib/python3.4/site-packages/_pytest/assertion/rewrite.py:171: in load_module
    py.builtin.exec_(co, mod.__dict__)
python_course_1604/class_01/tests/test_01.py:10: in <module>
    import python_course_1604.class_01.exercize_01_hello_world as exercize
E     File "/Users/fressi/workspace/python-class-16.04/python_course_1604/class_01/exercize_01_hello_world.py", line 8
E       print 'Hello world!'
E                          ^
E   SyntaxError: Missing parentheses in call to 'print'
======================================================= 2 passed, 17 skipped, 1 error in 0.41 seconds =======================================================
ERROR: InvocationError: '/Users/fressi/workspace/python-class-16.04/.tox/py34/bin/py.test --cov=python_course_1604 --cov-report term-missing --cov-report html --cov-report xml'
flake8 inst-nodeps: /Users/fressi/workspace/python-class-16.04/.tox/dist/python-course-1604-0.0.1.dev45.zip
flake8 installed: flake8==2.5.4,mccabe==0.4.0,pep8==1.7.0,pyflakes==1.0.0,python-course-1604==0.0.1.dev45
flake8 runtests: PYTHONHASHSEED='1278900245'
flake8 runtests: commands[0] | flake8 --max-complexity=8 python_course_1604
pylint inst-nodeps: /Users/fressi/workspace/python-class-16.04/.tox/dist/python-course-1604-0.0.1.dev45.zip
pylint installed: astroid==1.4.5,colorama==0.3.7,lazy-object-proxy==1.2.2,pylint==1.5.5,python-course-1604==0.0.1.dev45,six==1.10.0,wrapt==1.10.8
pylint runtests: PYTHONHASHSEED='1278900245'
pylint runtests: commands[0] | pylint --reports=n --rcfile=pylint.rc python_course_1604
__________________________________________________________________________ summary __________________________________________________________________________
  py27: commands succeeded
ERROR:   py34: commands failed
  flake8: commands succeeded
  pylint: commands succeeded
```

As you can see from summary py27, flake8 and pylink jobs have been success, while py34 has failed.
This is because the sintax for print statement has been changed in Python 3 and now it requires
parameters to passes inside _(...)_ as any other function.
```
E   SyntaxError: Missing parentheses in call to 'print'
```

Edit it again as below and rerun tox
```
'''
Created on 6 Apr 2016

@author: Federico Ressi <federico.ressi@intel.com>
'''

# Write a line that prints 'Hello world!'
print('Hello world!')
```

Now you should expect a success. Congratulations you di the first exercise.

## Push your 1st change
To have your code reviewed by teacher(s) you have to commit it and push it on your own upstream branch.
Make sure edited file is goint to be committed.
```
git add python_course_1604/class_01/exercize_01_hello_world.py
git status
```
you should expect something like this
```
On branch <your-branch-name>
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	modified:   python_course_1604/class_01/exercize_01_hello_world.py
```
Now you are ready to commit and push
```
git commit
git push --set-upstream origin <your-branch-name>
```

Once your upstrean branch is created you can summit further changes by executing:
```
git add <modified-files>
git commit
git push
```

## Create a pull request
Now that you are publishing your working branch you can create a pull request for your changes

Go to [GitHub project page](https://github.com/FedericoRessi/pythoncourse) and create a
[new pull request](https://github.com/FedericoRessi/pythoncourse/pull/new/master).

Make sure your pull request is referred to your branch name.

**IMPORTANT: please remember to never click on the button that says _Merge pull request_** 
