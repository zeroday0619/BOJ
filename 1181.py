import sys

first_input = sys.stdin.readline()

def text_length(text: str) -> dict:
    _text = text.replace(" ", "").replace("\n", "")
    length = len(_text)
    return {"text": _text, "length": length}
    

def __input(i):
    del i
    return text_length(sys.stdin.readline())
    

num = [__input(i) for i in range(int(first_input))]
print(num)