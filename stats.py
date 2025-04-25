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