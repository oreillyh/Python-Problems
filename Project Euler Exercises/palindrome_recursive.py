def palindrome(word):
    length = len(word)
 #print("length was %d" % length)
    if (length <= 1):
        return True
 #print( "comparing %s with %s result is %r" % (word[0], word[length-1], (word[0] == word[length-1])))
    return (word[0] == word[length-1]) and palindrome(word[1:length-1])

if __name__ == '__main__':
    print('{}'.format(palindrome('madam')))