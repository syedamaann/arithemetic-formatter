def arithmetic_arranger(problems, show_answers=False):
  # Check if the number of problems is valid
  if len(problems) > 5:
    return "Error: Too many problems."

  arranged_problems = ""
  for problem in problems:
    # Split the problem into operands and operator
    operand1, operator, operand2 = problem.split()

    # Check if the operator is valid
    if operator not in ['+', '-']:
      return "Error: Operator must be '+' or '-'."

    # Check if operands contain digits only and have a maximum of four digits
    if not operand1.isdigit() or not operand2.isdigit():
      return "Error: Numbers must only contain digits."
    if len(operand1) > 4 or len(operand2) > 4:
      return "Error: Numbers cannot be more than four digits."

    # Convert operands to integers
    operand1 = int(operand1)
    operand2 = int(operand2)

    # Calculate the answer
    if operator == '+':
      answer = operand1 + operand2
    else:
      answer = operand1 - operand2

    # Determine the maximum width of the operands
    max_width = max(len(str(operand1)), len(
        str(operand2))) + 2  # +2 for the operator and space

    # Arrange the operands and operator vertically
    arranged_problem = f"{operand1:>{max_width}}\n{operator} {operand2:>{max_width - 2}}\n{'-' * max_width}"

    # Include the answer if show_answers is True
    if show_answers:
      arranged_problem += f"\n{answer:>{max_width}}"

    arranged_problems += arranged_problem + "    "  # Add four spaces between problems

  # Remove extra space from the end and return the result
  return arranged_problems.rstrip()


# Example usage:
problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
print(arithmetic_arranger(problems))

problems = ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]
print(arithmetic_arranger(problems, True))
