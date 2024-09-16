import sys

def string_sort(words):
    words = list(set(words))
    words.sort(key=lambda x: (len(x), x))
    return words


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    words = [sys.stdin.readline().strip() for _ in range(n)]
    sorted_words = string_sort(words)
    for word in sorted_words:
        print(word)