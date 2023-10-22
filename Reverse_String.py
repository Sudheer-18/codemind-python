def reverse_words(sentence):
    # Split the sentence into words
    words = sentence.split()
    
    # Reverse the list of words
    reversed_words = list(reversed(words))
    
    # Join the reversed words back into a sentence
    reversed_sentence = ' '.join(reversed_words)
    
    return reversed_sentence

# Input sentence
input_sentence = input()

# Call the function to reverse the words
result = reverse_words(input_sentence)

# Print the reversed sentence
print(result)
