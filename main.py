import random

def tokenize(text):
    return text.replace(". ", " . ").replace(".\n", " .\n").split(" ")

def join(tokens):
    return " ".join(tokens).replace(" .", ".")

def load_tokens():
    with open("data.txt", "r") as file:
        data = file.read()
        return tokenize(data)
    
def predict_next(past, tokens):
    past = list(map(lambda x: x.lower(), past))
    depth = 0
    occurences = {}
    for token in tokens:
        if depth == len(past):
            depth = 0
            occurences[token] = occurences.get(token, 0) + 1
        if token.lower() == past[depth]:
            depth += 1
        else:
            depth = 0
            if depth > 0:
                occurences[token] = occurences.get(token, 0) + (depth/len(past))
    if not occurences:
        if len(past) == 1:
            return ""
        else:
            return predict_next(past[1:], tokens)
    return random.choices(list(occurences.keys()), occurences.values())[0]

TOKENS = load_tokens()

prompt = []
while True:
    newTokens = tokenize(input("You: "))
    if "[clear]" in newTokens:
        prompt = []
    prompt.extend(newTokens)
    token = " "
    response = newTokens
    while token and not (token.endswith(".")):
        token = predict_next(prompt, TOKENS)
        if "\n" in token:
            print(token.split("\n")[0], "", end="")
            break
        response.append(token)
        prompt.append(token)
    print(join(response))