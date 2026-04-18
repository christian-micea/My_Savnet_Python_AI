import os

def read_text_file(file_path):
    """Read a text file and return its contents as a string.
    Returns None if file cannot be read."""

    result = ""

    with open(file_path, 'r') as file:
        result = file.read()

    if not result:
        return None
    
    return result
    

def get_all_text_files(directory):
    """Return a list of all .txt files in the given directory.
    Use os.walk() to find files recursively."""

    # from what I uderstand, it is unnecessary to use a recursive structure for os.walk()
    # because it already traverses all subdirectories starting from the root in a for() loop

    text_files = []
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.txt'):
                text_files.append(os.path.join(root, file))
    
    return text_files
    

def is_valid_text_file(file_path):
    """Return True if file exists and has .txt extension."""

    if not file_path.endswith('.txt'):
        return False
    
    if not os.path.isfile(file_path):
        return False
    
    return True