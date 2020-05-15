results = [25,0,1,0,0,1,1]
processed = 0
passed =0
while results:
    processed+= 1
    result = results.pop()
    if not result:
        break
    passed+=1
else:
    print('Processed:', processed, 'passed:', passed)
          
