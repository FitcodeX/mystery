import re

def list_odd_length_words(any_string):
    words = any_string.split(" ")
    words_no_specials = []
    for word in words:
        plain_word = re.sub("[.!?]", "", word)
        words_no_specials.append(plain_word)
 
    word_dictionary = {}

    for word in words_no_specials:
        if len(word) in word_dictionary: 
            word_dictionary[len(word)] = word_dictionary[len(word)] + [word]
        else:
            word_dictionary[len(word)]=[word]
    odd_length_words = {}

    for word in word_dictionary:
        for odd_word in word_dictionary[word]:
            if len(odd_word) % 2 == 1:
                odd_length_words[word] = word_dictionary[word]
        else:
            continue
    return odd_length_words




# Tests
assert(list_odd_length_words("This is a sentence. And yet another one!") == {1: ['a'], 3: ['And', 'yet', 'one'], 7: ['another']})
assert(list_odd_length_words("Miscollated alphabetic superimposition") == {11: ['Miscollated'], 15: ['superimposition']})
print(list_odd_length_words("a a a a bb bb bb ccc ccc") == {1: ['a', 'a', 'a', 'a'], 3: ['ccc', 'ccc']})