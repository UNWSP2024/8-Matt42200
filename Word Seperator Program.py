def convert_sentence(sentence):
    result = sentence[0].upper() + sentence[1:].lower()


    final_result = ""
    for char in result:
        if char.isupper():
            final_result += " " + char.lower()  # Add space before the uppercase letter
        else:
            final_result += char  # Add the lowercase letters as they are
            
    return final_result


sentence = input("Enter the sentence with run-together words: ")


print(convert_sentence(sentence))