filename = 'poem.txt'
words_to_find = ['twinkle', 'star']
found_words = {word: False for word in words_to_find}
try:
    with open(filename, 'r') as file:
        content = file.read()
        content_lower = content.lower()
        for word in words_to_find:
            if word in content_lower:
                found_words[word] = True
    for word, found in found_words.items():
        if found:
            print(f"The word '{word}' IS present in the file.")
        else:
            print(f"The word '{word}' IS NOT present in the file.")
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
