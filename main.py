# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}
import string

def read_file_content(filename):
    with open(filename) as f:
     content = f.read()
     return content


print(read_file_content("./story.txt"))

def count_words():
    text = read_file_content("./story.txt")
    d = {}
    words = text.split()
    table = str.maketrans("", "", string.punctuation)
    stripped = [w.translate(table) for w in words]
    for word in stripped:
        if word in d:
            d[word] = d[word] + 1 
        else:
            d[word] = 1    
    return d

print(count_words())