# Arithmetic Arranger

This Python script provides a function to arrange arithmetic problems vertically, handling errors and optionally displaying answers. It is designed to format and display arithmetic problems in a visually appealing and easy-to-read manner, similar to how students arrange problems in primary school.

**Features:**
- Accepts a list of arithmetic problems as input.
- Validates input problems and handles errors:
  - Limits the number of problems to five.
  - Accepts only addition (+) and subtraction (-) operators.
  - Ensures operands contain digits only and have a maximum of four digits.
- Arranges problems vertically, aligning operands and operator properly.
- Displays answers below each problem optionally.
- Returns a string containing the formatted arrangement of problems.

**Usage:**
1. Import the `arithmetic_arranger` function from the `arithmetic_arranger.py` script.
2. Call the function with a list of arithmetic problems as the first argument.
3. Optionally, set the second argument to `True` to display answers.
4. The function returns a string containing the formatted arrangement of problems.

**Example:**
```python
from arithmetic_arranger import arithmetic_arranger

problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
print(arithmetic_arranger(problems))

problems = ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]
print(arithmetic_arranger(problems, True))
```

**Dependencies:**
- This script does not have any external dependencies and can be run using Python 3.

**License:**
This project is licensed under the MIT License. See the LICENSE file for more details.

**Acknowledgments:**
- This project is inspired by the "Arithmetic Formatter" challenge on freeCodeCamp.
