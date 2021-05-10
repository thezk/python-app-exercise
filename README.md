# Python App Exercise

## Exercise
- Use the ApiService to fetch TODOs from an API and save them into the _storage_ folder
    - TODOs can be accessed from this URL: https://jsonplaceholder.typicode.com/todos/
    - Each TODO should be saved on a single file in CSV format
    - The filename must contain the TODO "id" prefixed with the current date.
        - Example: 2021_04_28_123.csv


## Extra points
- Use _requests_ library from [PyPI](https://pypi.org/project/requests/)

## Notes for the reviewers

I made a modular project and refactored a bit the structure (not much) to encapsulate the concept of 
an independent service that runs in the "App" class.

I didn't use classes for everything. I prefer using the classes when it really makes sense and I always try to 
keep my code as functional as it can be to avoid status bugs.

Also, I didn't comment every single class or function because I prefer to make self explanatory code. My comments are 
mostly to explain parts of the code that aren't clear or to explain why I did something in the way it's in the code.

In order to run this small project you just have to install the requirements.txt dependencies (only requests)
and then run the main.py with python (I used 3.9.4).
The requirements.txt file is frozen in order to avoid possible compatibility problems (which would be very rare but
better safe than sorry).