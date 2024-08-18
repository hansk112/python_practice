

def reverse_string(a_word):
    
    # slicing 
    # sequence[start:stop:step]
    reverse_word = a_word[::-1]
    # a_word.reverse_string()

    return reverse_word

name ="hans"

reverse_name = reverse_string(name)
print(reverse_name)