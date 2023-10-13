with open("books/frankenstein.txt") as file:
    text = file.read()

count = text.split()
print(len(count))


char_dict = {}
for word in count:
    word = word.lower()
    for char in word:
        if not char.isalpha():
            continue
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1


def chars_dict_to_sorted_list(chars_dict):
    sorted_list = []
    for char in chars_dict:
        sorted_list.append({"char": char, "count": chars_dict[char]})
    sorted_list.sort(reverse=True, key=lambda x: x["count"])
    return sorted_list

word_sort = chars_dict_to_sorted_list(char_dict)
for word in word_sort:
    print(f"The '{word['char']}' character was found {word['count']} times") 