def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    characters = {}

    for char in text:
        char = char.lower()  # Normalize to lowercase for consistent counting
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    
    return characters

def sort_on_count(item):
    return item["count"]

def sort_dictionary(dict):
    list_of_chars = []

    for char, count in dict.items():
        list_of_chars.append({"char": char, "count": count})

    list_of_chars.sort(reverse=True, key=sort_on_count)
    return list_of_chars
