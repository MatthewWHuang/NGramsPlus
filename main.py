import random


def load_tokens():
    with open("data.txt", "r") as file:
        data = file.read()
        return data.split(" ")
    
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
    newTokens = input("You: ").split(" ")
    if "[clear]" in newTokens:
        prompt = []
    prompt.extend(newTokens)
    print(" ".join(newTokens), end=" ")
    token = " "
    while token and not (token.endswith(".")):
        token = predict_next(prompt, TOKENS)
        if "\n" in token:
            print(token.split("\n")[0], "", end="")
            break
        print(token, "", end="")
        prompt.append(token)
    print()