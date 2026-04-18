# Python Package & Module Organization Challenge

## Challenge Title: Text File Statistics Analyzer

## Overview
Create a simple text file analysis tool organized as a proper Python package. This challenge will teach you to structure code into modules and use external libraries.

## Required Package Structure
Create EXACTLY this structure:
```
text_analyzer/
├── __init__.py
├── analyzer.py          # Main analysis functions
├── file_ops.py          # File operations
├── reporter.py          # Report generation
└── main.py              # Command-line interface
```

## Step-by-Step Instructions

### Step 1: Create the Package Structure
1. Create the `text_analyzer` directory
2. Create all 4 Python files listed above
3. Each `__init__.py` should be empty

### Step 2: Implement `file_ops.py`
Create these EXACT functions:

```python
def read_text_file(file_path):
    """Read a text file and return its contents as a string.
    Returns None if file cannot be read."""
    # Your code here

def get_all_text_files(directory):
    """Return a list of all .txt files in the given directory.
    Use os.walk() to find files recursively."""
    # Your code here

def is_valid_text_file(file_path):
    """Return True if file exists and has .txt extension."""
    # Your code here
```

### Step 3: Implement `analyzer.py`
Create these EXACT functions:

```python
def count_words(text):
    """Count words in text. Split on whitespace."""
    # Your code here

def count_lines(text):
    """Count lines in text. Split on \n."""
    # Your code here

def count_characters(text):
    """Count all characters including spaces."""
    # Your code here

def calculate_average_word_length(text):
    """Calculate average word length. Use the textstat library."""
    # Install: pip install textstat
    # Use: textstat.avg_word_length(text)
    # Your code here

def analyze_text(text):
    """Return a dictionary with all analysis results:
    {
        'word_count': int,
        'line_count': int,
        'character_count': int,
        'avg_word_length': float
    }"""
    # Your code here
```

### Step 4: Implement `reporter.py`
Create these EXACT functions:

```python
def format_report(analysis_data, filename):
    """Return a formatted string report."""
    return f"""
Analysis Report for: {filename}
===============================
Word Count: {analysis_data['word_count']}
Line Count: {analysis_data['line_count']}
Character Count: {analysis_data['character_count']}
Average Word Length: {analysis_data['avg_word_length']:.2f}
"""

def save_report_to_file(report_text, output_path):
    """Save the report text to a file."""
    # Your code here
```

### Step 5: Implement `main.py`
Create EXACTLY this command-line interface:

```python
import argparse
from .file_ops import read_text_file, get_all_text_files
from .analyzer import analyze_text
from .reporter import format_report, save_report_to_file

def main():
    parser = argparse.ArgumentParser(description='Analyze text files')
    parser.add_argument('path', help='Path to file or directory')
    parser.add_argument('--output', '-o', help='Output file for report')
    
    args = parser.parse_args()
    
    if os.path.isfile(args.path):
        # Analyze single file
        text = read_text_file(args.path)
        if text:
            analysis = analyze_text(text)
            report = format_report(analysis, args.path)
            if args.output:
                save_report_to_file(report, args.output)
            else:
                print(report)
    elif os.path.isdir(args.path):
        # Analyze all .txt files in directory
        files = get_all_text_files(args.path)
        for file_path in files:
            text = read_text_file(file_path)
            if text:
                analysis = analyze_text(text)
                report = format_report(analysis, file_path)
                print(report)
    else:
        print(f"Error: {args.path} is not a valid file or directory")

if __name__ == '__main__':
    main()
```

### Step 6: Update `__init__.py`
Add these EXACT imports to make your package easy to use:

```python
from .analyzer import analyze_text, count_words, count_lines
from .file_ops import read_text_file, get_all_text_files
from .reporter import format_report, save_report_to_file
```

## Required External Library
You MUST install and use:
```bash
pip install textstat
```

Use it in the `calculate_average_word_length` function.

## Testing Your Solution

### Test 1: Single File Analysis
```bash
cd /home/work/WORK/Coding\ Projects/Savnet/Python_AI/MyWork/Module2/Homework1
python -m text_analyzer.main sample.txt
```

### Test 2: Save Report to File
```bash
python -m text_analyzer.main sample.txt --output report.txt
```

### Test 3: Directory Analysis
```bash
python -m text_analyzer.main /path/to/directory/with/txt/files
```

## Sample Test Data
Create a test file named `sample.txt` with this content:
```
Hello world!
This is a test file.
It has multiple lines.
And some words to count.
```

Expected output for this file:
- Word Count: 12
- Line Count: 4
- Character Count: 69 (including spaces and newlines)
- Average Word Length: ~4.0 (using textstat)

## What You'll Learn
1. **Package Structure**: How to organize code into modules
2. **Imports**: How to import between modules in the same package
3. **External Libraries**: How to use PyPI libraries (textstat)
4. **Command Line**: How to create CLI interfaces with argparse
5. **File Operations**: How to safely read files and handle directories

## Success Criteria
- All functions work as specified
- Package can be run with `python -m text_analyzer.main`
- Uses textstat library for average word length
- Handles both files and directories
- Reports are formatted correctly
- No crashes on invalid inputs

## Hints
- Use `try/except` for file operations
- Use `os.path.exists()` and `os.path.isfile()` to check paths
- Import `os` in `main.py` for path operations
- Test each module individually before integrating

Good luck! 🚀
