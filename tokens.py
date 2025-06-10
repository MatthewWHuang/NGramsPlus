replacements = []
joins = []
punctuation = [".", ",", "!", "?", ":", ";", "'", "\""]
for char in punctuation:
    replacements.append((char + " ", " " + char + " ")) 
    replacements.append((char + "\n", " " + char + "\n")) 
    joins.append((" " + char, char))

def tokenize(text):
    for replacement in replacements:
        text = text.replace(*replacement)
    return text.split(" ")

def join(tokens):
    joined = " ".join(tokens)
    for replacement in joins:
        joined = joined.replace(*replacement)
    return joined