# EmployeeAccrualsProject
A python script designed to process a csv file containing employee accruals information

This Python script takes a csv file containing rows of employee balances and returns a csv file with one row for each employee containing all of their balances as columns.

Input file example:

BALANCE    VALUE    EMPLOYEE_ID ...
COMP       12        1
SICK       6         1
VACATION   10        1
.
.
.


Output file example:

EMPLOYEE_ID      COMP      SICK      VACATION  ... 
1                 12        6          10
.
.
.
