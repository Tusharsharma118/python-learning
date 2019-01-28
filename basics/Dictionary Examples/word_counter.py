def word_counter(sentence):
    word_count_list = {}
    for word in sentence.split(' '):
       word_count_list[word] = word_count_list.get(word, 0) + 1

    return word_count_list

sentence = 'In the time when the operation of the machines becomes so odius, that you cant take part you cant even passively take part'
word_dict = word_counter(sentence)
print(word_dict)

