# Calculator Demo

This folder contains three calculator programs built in Python as part of the GenAI Copilot with Python web development training.

## Files

- `basic_calc.py`: A simple calculator with basic arithmetic operations (add, subtract, multiply, divide)
- `calc.py`: A scientific calculator with additional trigonometric and mathematical functions
- `scientific_calc.py`: Another version of the scientific calculator (similar to calc.py)

## Prerequisites

- Python 3.x installed on your system

## How to Run

1. Open a terminal and navigate to this folder:

   ```bash
   cd labs/calc-demo
   ```

2. Run any of the calculators:

   ```bash
   python basic_calc.py
   python calc.py
   python scientific_calc.py
   ```

3. Follow the on-screen prompts to select operations and enter numbers.

4. Type 'q' to quit the calculator.

## Features

### Basic Calculator (basic_calc.py)

- Addition
- Subtraction
- Multiplication
- Division (with zero division error handling)

### Scientific Calculator (calc.py / scientific_calc.py)

- All basic operations
- Trigonometric functions (sin, cos, tan) - input in degrees
- Logarithm (base 10)
- Square root
- Power function

## Error Handling

All calculators include input validation:

- Checks for numeric input
- Handles division by zero
- Handles invalid operations for logarithms and square roots

## Example Usage

```
Basic Calculator
Select operation:
1. Add
2. Subtract
3. Multiply
4. Divide

Enter choice (1-4) or 'q' to quit: 1
Enter first number: 5
Enter second number: 3
Result: 5.0 + 3.0 = 8.0
```

## Notes

- These are command-line interface (CLI) programs
- Designed for educational purposes to demonstrate Python functions and control flow
- Part of the training labs for learning Python with GitHub Copilot
