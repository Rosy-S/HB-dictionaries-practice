def process_text(filename):
    testfile = open(filename)
    final_dict = {}
    for line in testfile:
        data = line.split(" ")
        for word in data:
            word = word.rstrip()
            final_dict[word] = final_dict.get(word, 0) + 1
    
    for key, value in sorted(final_dict.items()):
        print key, value


process_text("twain.txt")


