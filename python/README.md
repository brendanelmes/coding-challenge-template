# Python template

This template makes use of [pytest](https://docs.pytest.org/) to run tests with parameterized inputs in order to compare the speed of different solutions.

## Local setup

Ensure that you are in directory `python/`

### Create virtual environment

```bash
python3 -m venv venv
```

### Activate virtual environment

```bash
source venv/bin/activate
```

### Install requirements

```bash
pip install -r requirements.txt
```

### Run the comparison
```
python3 -m pytest
```

>If you are using VSCode, ensure that you have the `python/` directory open as the workspace, otherwise imported modules may not be found

## Providing test inputs and expected outputs

In the `tests/test_solutions.py` file, specify these with names in the `params` dictionary:

```python
params = {
    'title_of_test_case': (input_array,expected_output),
    'short_array': ([1,2,3],3),
    'worst_case': ([1]*1000000,1000000)
}
```

The timings of each test case will be displayed in the log output.

You may need to adjust the input and output formatting of this dictionary.
This will require alteration of the method.

## Trying multiple solutions

In the `solutions/` directory, specify files with naming convention:

```
solution1.py
solution2.py
solution3.py
...
```

containing methods with matching names:

```python
def solution3(input_array):
    
    # Add your code here
    
    return output_value
```

which can be imported into the `test_solutions.py` file and added to the array `solutions`

```python
from solutions.solution1 import solution1
from solutions.solution2 import solution2

solutions = [solution1,solution2]
```

Each solution in this array will be added to the solutions which get run for each test case.

Sample output:

```yaml                  
tests/test_solutions.py::test_multiple_solutions[empty_array] 
--------------------------------------------------- live log call ------------------------------------
INFO     test_solutions:test_solutions.py:22 Solution1: 0.0000009537
INFO     test_solutions:test_solutions.py:22 Solution2: 0.0000009537
PASSED                                                                        [ 33%]
tests/test_solutions.py::test_multiple_solutions[short_array] 
----------------------------------------------------live log call ------------------------------------
INFO     test_solutions:test_solutions.py:22 Solution1: 0.0000009537
INFO     test_solutions:test_solutions.py:22 Solution2: 0.0000009537
PASSED                                                                        [ 66%]
tests/test_solutions.py::test_multiple_solutions[worst_case] 
---------------------------------------------------- live log call -----------------------------------
INFO     test_solutions:test_solutions.py:22 Solution1: 0.0000009537
INFO     test_solutions:test_solutions.py:22 Solution2: 0.0151939392
PASSED                                                                        [100%]

==================================================== 3 passed in 0.06s ===============================
```