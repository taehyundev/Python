word = input("문자열 입력: ")
word_dict = dict()
while(word!=""):
    cnt = int()
    for i  in range(len(word)):
        if word[0] == word[i]:
            cnt = cnt +1
    word_dict[word[0]] = cnt
    word = word.replace(word[0],'')
word_key = list(word_dict.keys())

for i in range(len(word_key)):
    print(word_key[i]+" : ",word_dict[word_key[i]]," 회   |"+'*' * word_dict[word_key[i]])
