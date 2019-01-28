def character_counter(sentence):
    # Reomove spaces and recover the characters in the sentence
    character_list = [character for character in sentence if not character.isspace()]
    # character_list.remove('')
    chararcter_dictionary = {}
    for character in character_list:
        if character not in chararcter_dictionary:
            chararcter_dictionary[character] = 1
        else:
            chararcter_dictionary[character] += 1
    return chararcter_dictionary


sentence = input('Enter a sentence:')
character_final_count = character_counter(sentence)
print(character_final_count)