def count_words(text):
    words = text.split()
    return len(words)

def count_character(text):
    words = text.lower()
    counts = {}

    for char in words:      
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

def sorted_list(counts):
    char_list = []

    for char, count in counts.items():
        char_dict = {"char": char, "num": count}
        char_list.append(char_dict)

    def sort_on(dict):
        return dict["num"]

    char_list.sort(reverse=True, key=sort_on)

    return char_list