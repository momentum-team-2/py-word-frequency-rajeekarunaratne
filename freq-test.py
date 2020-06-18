# import string

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

file = open('one-today.txt', "r")

def normalize_text(text):
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


# def remove_stopwords(text):
#     line_to_keep = ""
#     for word in text.split():
#         if word not in STOP_WORDS:        
#             line_to_keep += word
#             line_to_keep += " "
#     return (line_to_keep) 

normalized = normalize_text(file)
print(normalized)
# removed = remove_stopwords(normalized)
# print(removed)


