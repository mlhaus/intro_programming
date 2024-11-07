import re
from collections import OrderedDict

def get_clean_word(word):
    '''
    Input: a word
    Output: the word with no non-alphabetic characters
    '''
    # Source: https://stackoverflow.com/a/22521156/6629315
    regex = re.compile('[^a-zA-Z]')
    return regex.sub("", word).lower()


words = [] # a list is an unordered group of items. Each item has an index (0, 1, 2, etc.)
with open("spider.txt", "r") as file:
    while(line := file.readline()) != "":
        words += line.strip().split() # strip will remove new line character \n, split will convert the line into a list of words
    # print(words)

word_count = {} # a dictionary is a group of unordered entries. Each entry is a key:value pair. There are no indexes.
# Example: {"spider":3, "out":2, "rain":2}
for word in words:
    clean_word = get_clean_word(word)
    # print(clean_word)
    if(clean_word not in word_count):
        word_count[clean_word] = 1 # count the word for the first time. The word becomes the key
    else:
        word_count[clean_word] += 1 # add 1 to a word that we have counted before

# print(word_count)
sorted_word_count = sorted(word_count.items(), key=lambda kv: kv[1], reverse=True) # returns a list of tuples
# print(OrderedDict(sorted(word_count.items(), key=lambda kv: kv[1], reverse=True))) # returning an OrderedDict object
for i in range(10):
    print(f"The word '{sorted_word_count[i][0]}' appears {sorted_word_count[i][1]} times.")


# if __name__ == "__main__":
#     print(get_clean_word("@bCd$!gH.,j"))