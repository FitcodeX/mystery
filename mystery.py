import re

def list_odd_length_words(any_string):
    string_split = any_string.split(" ")
    string_no_specials = []
    for element in string_split:
        letter_char = re.sub("[.!?]", "", element)
        string_no_specials.append(letter_char)
    print(any_string, string_split, string_no_specials)
    z = {}

    for stuff in string_no_specials:
        if len(stuff) in z: 
            z[len(stuff)] = z[len(stuff)] + [stuff]
        else:
            z[len(stuff)]=[stuff]
    string_split = {}

    for string_no_specials in z:
        for element in z[y]:
            if len(element) % 2 == 1:
                a[y] = z[y]
        else:
            continue
    return a




# Tests
#assert(my_func("This is a sentence. And yet another one!") == {1: ['a'], 3: ['And', 'yet', 'one'], 7: ['another']})
#assert(my_func("Miscollated alphabetic superimposition") == {11: ['Miscollated'], 15: ['superimposition']})
#print(my_func("a a a a bb bb bb ccc ccc") == {1: ['a', 'a', 'a', 'a'], 3: ['ccc', 'ccc']})