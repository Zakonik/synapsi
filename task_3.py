from math import ceil
def justify(words, max_width):
    biggest = max(words.split(), key=len)
    if max_width < len(biggest):
        print("Can't do. Width shorter then longest word")
        return ""
    words = words.split()
    final_str = []
    list_of_words = []
    tmp = []
    length = 0
    for word in words:
        if length+len(word) <= max_width:
            length = length+len(word)+1
            tmp.append(word)
        else:
            list_of_words.append(tmp)
            tmp = [word]
            length = len(word)+1
    list_of_words.append(tmp)

    for words in list_of_words:
        space_nr = max_width - sum(len(s) for s in words)
        space_places = len(words)-1
        nr = ceil(space_nr/space_places) if space_places != 0 else space_nr
        tmp_word=""
        for word in words:
            tmp_word = tmp_word+word+"".ljust(nr if space_nr>=nr else space_nr)
            space_nr = space_nr - nr
        final_str.append(tmp_word)
    final_str[-1]=" ".join(final_str[-1].split())


    return final_str

def print_formated(str,width):
    print(*('"{}"'.format(line) for line in justify(str,width)), sep="\n",end="\n\n")

if __name__ == '__main__':
    print_formated("Hey the watss up", 7)
    print_formated("hey up", 7)
    print_formated("Hey there mate, it’s nice to finally meet you!", 16)
    print_formated("Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit...", 10)
    print_formated("Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit...", 20)
