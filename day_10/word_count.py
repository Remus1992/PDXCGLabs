# book = open ("faust.txt", "r")
# print (book.name)
# book.close()

# with open ("faust.txt", "r") as book:
# print (book.name)

# with open ("faust.txt", "r") as book:
#     book_contents = book.read()
#     print(book_contents)

# with open ("faust.txt", "r") as book:
#     for line in book:
#         print(line, end="")


# with open ("faust.txt", "r") as book:
#
#     size_to_read = 10
#
#     book_contents = book.read(size_to_read)
#
#     while len(book_contents) > 0:
#         print (book_contents, end='*')
#         book_contents = book.read(size_to_read)


# searchfile = open("faust.txt", "r")
# for line in searchfile:
#     if "Hurrah" in line: print (line)
# searchfile.close()

# f = open("faust.txt", "r")
# searchlines = f.readlines()
# f.close()
# for i, line in enumerate(searchlines):
#     if "Hurrah!" in line:
#         for l in searchlines[i:i+3]: print (l),
#         print

# file=open("faust.txt","r+")
#
# from collections import Counter
# wordcount = Counter(file.read().split())
# for item in wordcount.items(): print("{}\t{}".format(*item))
# file.close();

# file=open("faust.txt","r+")
# wordcount={}
# for word in file.read().split():
#     if word not in wordcount:
#         wordcount[word] = 1
#     else:
#         wordcount[word] += 1
# print (word,wordcount)
# file.close();

wordcount = {}

with open('faust.txt') as file:  # with can auto close the file
    for word in file.read().split():
        word = word.lower()
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1

wordcount = sorted(wordcount.items(), key=lambda x: x[1], reverse=True)

for k, v in wordcount[:5]:
    print(k, v)
###


# from collections import Counter
# with open('faust.txt') as file:  # with can auto close the file
#     wordcount = Counter(file.read().split())
#
# for k, v in wordcount.most_common(5):
#     print(k, v)

### Mikey's 
# from collections import Counter
# ctr = Counter()
# token_ctr = 0
# with open('faust.txt', 'r') as f:
#     for line in f:
#        line_words = line.strip().split()
#        for word in line_words:
#            if len(word) > 4:
#                token_ctr += 1
#                ctr[word] += 1
#
# def mostcommon():
#     print("The most common words are ", ctr.most_common(10))
#     print("There are ",token_ctr, " words in 'Faust' by Goethe.")
#     print("There are ",len(ctr), " unique words therein.")
# print(mostcommon())
