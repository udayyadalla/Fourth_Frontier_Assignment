# Fourth_Frontier_Assignment

Steps to run this code:
===============
To Run the file : python name of the file .py (eg: python MyOperations.py)

Explanation:
========

There are on total 4 files, MyOpearions.py, Map.py, Variables.py, elementactions.py

In that MyOperations.py(Main File) , I have imported the config and Map files

In the MyOperations.py(Main File)

i. Created the class name as "MyOperations". 
ii. In the initialization part, I have used automationpractice to control the chrome browser.
iii. added the new mail ID and created an account
iv. once account is created, entered all the mandatory fields and registered to portal
v. Finally verifying the account is created with the valid username or not and returning the text present on it
vi. Created the shutdown(Definition) to close the open browser

Map.py:
=====
In this Map.py file, I have added all the xpath' s so that if some xpath is changed no need to modify the MyOperations.py file.

Variable.py:
========
In this Variable.py, I am reading all the input parameters  like email, username, password, et.al.... form this variables.py. 

In the MyOperations.py(Main File) , I have created the object to that class and I have called all the definitions to preform the scenario in the main file
