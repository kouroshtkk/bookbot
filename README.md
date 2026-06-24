# BookBot

BookBot is a Python-based command-line tool designed to analyze the contents of books (plain text files). It processes the text to compute statistics, including the total word count and a sorted breakdown of character frequencies, helping you understand the composition of any literary work.

This is my first project as part of the [Boot.dev](https://www.boot.dev) backend developer curriculum!

## Features

- **Word Counter:** Instantly calculates the total number of words in any text file.
- **Character Frequency Analysis:** Counts how often each alphabetical character appears in the text.
- **Case-Insensitive Counting:** Converts all text to lowercase before analysis to ensure accurate counting (e.g., 'A' and 'a' are grouped together).
- **Formatted Reports:** Prints a clean, structured report to the console showing:
  - The path of the analyzed book.
  - The total number of words.
  - A list of alphabetical characters sorted from most frequent to least frequent.

## Getting Started

### Prerequisites

To run this project, you need to have Python 3 installed on your system.

### Running BookBot

1. Clone or download the repository to your local machine.
2. Navigate to the project directory:
   ```bash
   cd bookbot
   ```
3. Run the script by providing the path to a text file (e.g., one of the books in the `books/` directory):
   ```bash
   python3 main.py books/frankenstein.txt
   ```

## Example Output

When running BookBot on Mary Shelley's *Frankenstein*, the report looks like this:

```text
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 75767 total words
--------- Character Count -------
e: 44538
t: 29493
a: 25894
o: 24494
i: 23927
n: 23643
s: 20360
r: 20079
h: 19176
d: 16318
l: 12306
m: 10206
u: 10111
c: 9011
f: 8451
y: 7756
w: 7450
p: 5952
g: 5795
b: 4868
v: 3737
k: 1661
x: 691
j: 497
q: 325
z: 235
============= END ===============
```

## Project Structure

- [main.py](file:///home/kouroshtkk/bootdev/bookbot/main.py): The main entry point of the program. Handles CLI arguments and triggers the analysis report.
- [stats.py](file:///home/kouroshtkk/bootdev/bookbot/stats.py): Contains helper functions for reading files, counting words, generating the character dictionary, and sorting the frequency list.
- [books/](file:///home/kouroshtkk/bootdev/bookbot/books/): A directory containing sample text files for testing the analyzer.
