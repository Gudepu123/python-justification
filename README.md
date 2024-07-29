# Text Justification Script

## Description

This script takes a paragraph string and a paragraph width as input parameters and returns an array of left and right justified strings. No words are broken in the process.

## Assumptions

- The paragraph string is a single continuous string with words separated by spaces.
- The paragraph width is a positive integer.
- The output is printed line by line, where each line is a left and right justified string of the specified width.

## How to Run

1. Ensure you have Python 3 installed on your system.
2. Save the script to a file named `justify.py`.
3. Run the script from the command line with the required arguments.

```sh
python3 justify.py --paragraph-string "This is a sample text but a complicated problem to be solved, so we are adding more text to see that it actually works." --paragraph-width 20
