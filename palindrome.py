# Ian McLoughlin, 2018-03-14
# https://github.com/ianmcloughlin/problems-python-fundamentals

def ispalindrome(s):
  # Create a variable that will become the answer.
  ans = True
  # Loop over the length of the string
  for i in range(len(s)):
    if s[i] != s[len(s) - i - 1]:
      ans = False
  return ans

# Tests from question.
print(ispalindrome("navan"))
print(ispalindrome("navanman"))