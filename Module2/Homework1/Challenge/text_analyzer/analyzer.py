import textstat

def count_words(text):
    """Count words in text. Split on whitespace."""
    
    return len(text.split())


def count_lines(text):
    """Count lines in text. Split on \n."""
    
    return len(text.split('\n'))

def count_characters(text):
    """Count all characters including spaces."""
    
    return len(text)

def calculate_average_word_length(text):
    """Calculate average word length. Use the textstat library."""
    # Install: pip install textstat
    # Use: textstat.avg_word_length(text)
    
    # return textstat.avg_word_length(text)
    wordCnt = textstat.lexicon_count(text)
    charCnt = textstat.char_count(text)
    return float(charCnt) / float(wordCnt)

def analyze_text(text):
    """Return a dictionary with all analysis results:
    {
        'word_count': int,
        'line_count': int,
        'character_count': int,
        'avg_word_length': float
    }"""
    
    return {
        'word_count': count_words(text),
        'line_count': count_lines(text),
        'character_count': count_characters(text),
        'avg_word_length': calculate_average_word_length(text)
    }