with open('LIWC_words.txt', 'r') as document:
    answer = {}
    for line in document:
        line = line.split()
        #print(line)
        if not line:  # empty line?
            continue
        print(line[0], line[1:])
        answer[line[0]] = line[1:]
        #break
print(answer)
