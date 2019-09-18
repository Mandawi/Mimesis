def div_sen_key(sen_list,search_queries):
    div_sen=[] # list of divided sentences to put on images
    for sen in sen_list:
        print("Sentence being observed:",sen)
        word_start=0 # index of the word to start with
        word_counter=0 # count words
        for word in list(sen.split(" ")):
            print("Word being observed:",word)
            word_counter+=len(word)+1
            if word in search_queries:
                print("Start index:"+str(word_start)+"\nEnd index:"+str(word_counter))
                print("Word:"+sen[word_start:word_counter])
                div_sen.append(sen[word_start:word_counter])
                word_start=word_counter
    return div_sen

print(div_sen_key(["I like apples a lot, they are very tasty","They make me very hungry"],["apples","they","tasty","hungry"]))