loop = True
while(loop):
    print("infinity loop")
    for i in range(1,100000000000):
        newList = []
        
        # This loop creates a large nested list consumin

        
        
        
        x = 0
        x = x ** i
        print(i)
        newList.append(i)
        
        for j in range(len(newList)):
            print("Memory")
            newNewList = []
            newNewList.append(j)
            for z in range(len(newNewList)):
                print(z)
                innerList = []
                innerList.append(z)
                for a in innerList:
                    print("Inner memory")
                    zed = x ** j
                  
