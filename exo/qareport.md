# Habitable Exo-Planets Quality Report

- **Created at:** 2017-05-09 15:06:50.251022
- **Corral Version:** 0.2.7


## 1. Summary

- **Tests Success:** `Yes`
- **Tests Ran:** `2`
- **Processors:** `3`
- **Coverage:** `81.94%`
- **Maintainability & Style Errors:** `0`

<!-- -->

- **QA Index:** `27.31%`
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
Ran 2 tests in 0.740s

OK

```
---

### 2.2 Coverage
```
Name              Stmts   Miss  Cover
-------------------------------------
exo/__init__.py       1      0   100%
exo/alerts.py        37     16    57%
exo/commands.py       1      0   100%
exo/load.py          20     10    50%
exo/models.py        23      0   100%
exo/pipeline.py       4      0   100%
exo/settings.py      17      0   100%
exo/steps.py         19      0   100%
exo/tests.py         22      0   100%
-------------------------------------
TOTAL               144     26    82%

```
---

### 2.3 MAINTAINABILITY & STYLE
```

```

