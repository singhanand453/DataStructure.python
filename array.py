import array
arr=array.array('i',[1,2,3])
#for i in range(0,3):
    #print(arr[i],end=" ")

#arr.append(4);
#for i in range(0,4):
    #print(arr[i],end=" ")

#arr.insert(2,6)
#print("\r")
#for i in range(0,5):
    #print(arr[i],end=" ")

#print(arr.pop(2))
#for i in range(0,4):
    #print(arr[i],end=" ")

#print(arr.remove(1))
#for i in range(0,3):
    #print(arr[i],end=" ")

print(arr.index(2))
arr.reverse()
for i in range(0,3):
    print(arr[i],end=" ")

