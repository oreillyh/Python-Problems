def reverse(word):
    length = len(word)
    if (length <= 1):
        return word
    return word[length-1] + reverse(word[:length-1])

if __name__ == '__main__':
 print('{}'.format(reverse('hguH')))