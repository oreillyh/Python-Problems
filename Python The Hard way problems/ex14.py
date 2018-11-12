#exercise 14 'Python the hard way'

from sys import argv
script, user_name = argv
prompt = '>'

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes - input(prompt)

print("What kind of computer do you have")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure whwre that is.
And you ahve a {computer} computer. Nice
""")
