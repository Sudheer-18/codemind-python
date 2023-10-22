def reverse_words_in_sentence(sentence):
    # Split the sentence into words using space as a delimiter
    words = sentence.split()
    
    # Reverse each word and store them in a list
    reversed_words = [word[::-1] for word in words]
    
    # Join the reversed words to form the sentence
    reversed_sentence = " ".join(reversed_words)
    
    return reversed_sentence

# Example usage:
original_sentence =input()
reversed_sentence = reverse_words_in_sentence(original_sentence)
print( reversed_sentence)
