Pricing and print invoice
==============================
This project will work for Python 3.7 or higher.

Project Structure
-----------------
This project has one modules:
* `com.solution` contains print invoice functions.

Test modules are placed under the `tests` directory.

Running Tests
-------------
pytest has many command line options with a powerful discovery mechanism:
* `python -m pytest` to discover and run all tests from the current directory
* `python -m pytest -v` to explicitly print the result of each test as it is run
* `python -m pytest tests/{A}.py` to run only A test
* `python -m pytest --junitxml=results.xml` to generate a JUnit-style XML test report
* `python -m pytest -h`  for command line help

It is also possible to run pytest directly with the "pytest" or "py.test" command,
instead of using the longer "python -m pytest" module form. However, the shorter
command does *not* append the current directory path to *PYTHONPATH*.

[Configuration settings](http://doc.pytest.org/en/latest/customize.html)
may also be added to "pytest.ini".

Running main function
-------------
python main.py --product='Pants' --product='Shoes' --product='Jacket'  --product='T-shirt' --product='Blouse'