def number_to_text(n):
    keypad = {"1": [],
              "2": ["a", "b", "c"],
              "3": ["d", "e", "f"],
              "4": ["g", "h", "i"],
              "5": ["j", "k", "l"],
              "6": ["m", "n", "o"],
              "7": ["p", "q", "r", "s"],
              "8": ["t", "u", "v"],
              "9": ["w", "x", "y", "z"],
              "*": [],
              "0": ["+"],
              "#": []}
    if type(n) != str:
        n = str(n)
    words = []
    for c in n:
        if not words:
            for x in keypad.get(c, []):
                words.append(x)
        else:
            tmp = words
            words = []
            if not keypad.get(c, []):
                words = tmp
            else:
                for w in tmp:
                    part = []
                    for x in keypad.get(c, []):
                        part.append(w + x)
                    words = words + part
    return words


if __name__ == '__main__':
    print(number_to_text("123"))
    print(number_to_text("321"))
    print(number_to_text("*#01"))
    print(number_to_text("*#01234567890#*"))
    print(number_to_text("46"))
