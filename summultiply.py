# Ian McLoughlin, 2018-03-14
# https://github.com/ianmcloughlin/problems-python-fundamentals

def sumultiply(x, y):
  # Create a variable that will become the answer.
  total = 0
  # Loop over y, adding x to the total.
  for i in range(y):
    total = total + x
  return total

# Tests from question.
print(sumultiply(11, 13))
print(sumultiply(5, 123))