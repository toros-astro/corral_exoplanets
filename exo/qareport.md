# Habitable Exo-Planets Quality Report

- **Created at:** 2017-05-09 14:57:43.291979
- **Corral Version:** 0.2.7


## 1. Summary

- **Tests Success:** `Yes`
- **Tests Ran:** `2`
- **Processors:** `3`
- **Coverage:** `81.63%`
- **Maintainability & Style Errors:** `19`

<!-- -->

- **QA Index:** `25.01%`
- **QA Qualification:** `F`


### 1.1 About The Corral Quality Assurance Index (QAI)

```
QAI = 2 * (TP * (PT/PNC) * COV) / (1 + exp(MSE/tau))

    Where:
        TP: If all tests passes is 1, 0 otherwise.
        PT: Processors and commands tested.
        PCN: The number number of processors (Loader, Steps and Alerts)
             and commands.
        COV: The code coverage (between 0 and 1).
        MSE: The Maintainability and Style Errors.
        tau: Tolerance of style errors per file

    
```

**Current Value of Tau:**: `13.00` per file


### 1.2 About The Qualification

The Corral qualification is a quantitave scale based on QAI


- QAI >= 0.00% -- `F`
- QAI >= 60.00% -- `D-`
- QAI >= 63.00% -- `D`
- QAI >= 67.00% -- `D+`
- QAI >= 70.00% -- `C-`
- QAI >= 73.00% -- `C`
- QAI >= 77.00% -- `C+`
- QAI >= 80.00% -- `B-`
- QAI >= 83.00% -- `B`
- QAI >= 87.00% -- `B+`
- QAI >= 90.00% -- `A-`
- QAI >= 93.00% -- `A`
- QAI >= 95.00% -- `A+`



## 2. Full Output

### 2.1 Tests
```
runTest (exo.tests.HabitableZoneTest) ... ok
runTest (exo.tests.HabitableZoneNoRstarNoTeffTest) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.772s

OK

```
---

### 2.2 Coverage
```
Name              Stmts   Miss  Cover
-------------------------------------
exo/__init__.py       1      0   100%
exo/alerts.py        37     16    57%
exo/commands.py       2      0   100%
exo/load.py          21     11    48%
exo/models.py        23      0   100%
exo/pipeline.py       4      0   100%
exo/settings.py      17      0   100%
exo/steps.py         20      0   100%
exo/tests.py         22      0   100%
-------------------------------------
TOTAL               147     27    82%

```
---

### 2.3 MAINTAINABILITY & STYLE
```
Found pep8-style errors.
Please check the Python code style reference: https://www.python.org/dev/peps/pep-0008/

Errors found: 
exo/alerts.py:67:32: E712 comparison to True should be 'if cond is True:' or 'if cond:'
exo/commands.py:20:0: F401 'corral.cli' imported but unused
exo/load.py:43:7: E111 indentation is not a multiple of four
exo/load.py:44:11: E111 indentation is not a multiple of four
exo/load.py:45:7: E111 indentation is not a multiple of four
exo/load.py:46:11: E111 indentation is not a multiple of four
exo/load.py:52:22: E203 whitespace before ':'
exo/load.py:53:22: E203 whitespace before ':'
exo/load.py:54:22: E203 whitespace before ':'
exo/load.py:55:22: E203 whitespace before ':'
exo/load.py:56:22: E203 whitespace before ':'
exo/load.py:59:22: E203 whitespace before ':'
exo/load.py:60:22: E203 whitespace before ':'
exo/models.py:59:0: E303 too many blank lines (3)
exo/settings.py:41:8: E126 continuation line over-indented for hanging indent
exo/steps.py:20:0: F401 'random' imported but unused
exo/steps.py:51:30: E711 comparison to None should be 'if cond is not None:'
exo/steps.py:55:13: E221 multiple spaces before operator
exo/tests.py:22:0: F401 '.load' imported but unused
exo/tests.py:22:0: F401 '.alerts' imported but unused
```

