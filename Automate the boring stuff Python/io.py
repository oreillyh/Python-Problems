import io

with open('log.txt', 'w') as writeFile:
    toLog = input("What do you want to write to the log?")
    writeFile.write(toLog)
    