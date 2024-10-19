def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        wordcount = len(words)
        bookwords = ""
        for i in range(wordcount):
            bookwords += " " + words[i].lower()
        
char = [
{"letter":"a", "count": 0},
{"letter":"b", "count": 0},
{"letter":"c", "count": 0},
{"letter":"d", "count": 0},
{"letter":"e", "count": 0},
{"letter":"f", "count": 0},
{"letter":"g", "count": 0},
{"letter":"h", "count": 0},
{"letter":"i", "count": 0},
{"letter":"j", "count": 0},
{"letter":"k", "count": 0},
{"letter":"l", "count": 0},
{"letter":"m", "count": 0},
{"letter":"n", "count": 0},
{"letter":"o", "count": 0},
{"letter":"p", "count": 0},
{"letter":"q", "count": 0},
{"letter":"r", "count": 0},
{"letter":"s", "count": 0},
{"letter":"t", "count": 0},
{"letter":"u", "count": 0},
{"letter":"v", "count": 0},
{"letter":"w", "count": 0},
{"letter":"x", "count": 0},
{"letter":"y", "count": 0},
{"letter":"z", "count": 0}
]

def sort_on(dict):
    return dict["count"]

def charnum():
    with open("books/frankenstein.txt") as l:
        file_contents = l.read()
    words = file_contents.split()
    wordcount = len(words)
    bookwords = ""
    for i in range(wordcount):
        bookwords += words[i].lower()
    return bookwords

def outputchardict(bookwordstr):
    for j in range(len(bookwordstr)):    
        for x in range(26):
            if bookwordstr[j] in char[x]["letter"]:
                char[x]["count"] += 1
    char.sort(reverse=True, key=sort_on)
    print (char)
    print("\n-- End of Report --")

main()
outputchardict(charnum())
#outputchardict()