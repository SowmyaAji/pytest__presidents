# pytest__presidents
A pytest module to test getting and verifying the list of US Presidents upto Biden using the requests library and the DuckDuckGo instant answers api

## Overview:
Created as lab for CSC256 at Wake Tech Community College.

### Instructions / Requirements:

 * Write a PyTest module that queries the DuckDuckGo api for “presidents of the united states,” and tests that each president is listed in the response.
  * We’ll only look for the last name of a president.  That means that we won’t distinguish between John Adams and his son, John Quincy Adams, or George Bush the senior  and ‘W.’
  
### How to use this repo:
 * Pre-req:  built with Python 3.10
 
 - clone this repo and cd into it
 - open a venv and install the requirements.txt with ``$ pip install -r requirements.txt``
 - run ``pytest``
 
 ### Watch out for:
 
 - The list of presidents against which the code checks the data stops with Biden, as he is the last President as of 11/05/2022 and is hard coded. This should be added to, if testing in the future. 
 
