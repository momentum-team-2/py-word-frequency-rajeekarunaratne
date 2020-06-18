STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    
file = open('one-today.txt', "r")

def normalize_text(text):
    # lowercases and unpunctuates text
    line_to_keep = ""
    for line in text:
        line = line.lower()
        all_letters = "abcdefghijklmnopqrstuvwxyzéí’ "
        for char in line:
            if char in all_letters:
                line_to_keep += char
            else:
                line_to_keep += " "   
    
    return (line_to_keep)


def remove_stopwords(text):
    # takes out stop words but sadly some other words as well :(
    line_to_keep = ""
    for word in text.split():
        if word not in STOP_WORDS:        
            line_to_keep += word
            line_to_keep += " "
    return (line_to_keep) 

normalized = normalize_text(file)
removed = remove_stopwords(normalized)
print(removed)




if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
