firstBracket = []
thirdBracket = []
curlBracket = []
angleBracket = []
counter = []
braces = {'(':')','{':'}','[':']','<':'>'}
oppBraces = {')':'(',']':'[','>':'<','}':'{'}

testString = "{this [is (a] python) <test 3>}"
flag = 0

for i in testString:
    if i == "(":
        idxOne = testString.index(i)
    elif i==")":
        idxTwo=testString.index(i)
for j in testString[idxOne:idxTwo+1]:
    firstBracket.append(j)
for i in firstBracket:
    c = braces.get(i)
    if c:
        counter.append(c)
    d = oppBraces.get(i)
    if d:
        counter.append(d)
if len(counter)%2!=0:
    flag = 1

for i in testString:
    if i == "[":
        idxOne = testString.index(i)
    elif i=="]":
        idxTwo=testString.index(i)
for j in testString[idxOne:idxTwo+1]:
    thirdBracket.append(j)
for i in thirdBracket:
    c = braces.get(i)
    if c:
        counter.append(c)
    d = oppBraces.get(i)
    if d:
        counter.append(d)
if len(counter)%2!=0:
    flag = 1

for i in testString:
    if i == "{":
        idxOne = testString.index(i)
    elif i=="}":
        idxTwo=testString.index(i)
for j in testString[idxOne:idxTwo+1]:
    curlBracket.append(j)
for i in curlBracket:
    c = braces.get(i)
    if c:
        counter.append(c)
    d = oppBraces.get(i)
    if d:
        counter.append(d)
if len(counter)%2!=0:
    flag = 1

for i in testString:
    if i == "<":
        idxOne = testString.index(i)
    elif i==">":
        idxTwo=testString.index(i)
for j in testString[idxOne:idxTwo+1]:
    angleBracket.append(j)
for i in angleBracket:
    c = braces.get(i)
    if c:
        counter.append(c)
    d = oppBraces.get(i)
    if d:
        counter.append(d)
if len(counter)%2!=0:
    flag = 1

if flag == 1:
    print "False"
else:
    print "True"