listy = [1,2,3,4,5]
listy.append(listy[0:])
listy = listy[len(listy)-1:]
print(listy)