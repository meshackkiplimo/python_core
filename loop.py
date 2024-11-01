# for loop
s = 'mesh'
for i in s:
    print(i)
    
    
# for loop in range
for i in range(0,10,2):
    print(i)
    
#enumerate loop
f1 = ['melon','apple','mango']
for i in enumerate(f1):
    print(i)

#nested loop
for i in range(1,4):
     for j in range (1,4):
         print(i,j)

    
    
#loops n one line
numbers  = [x for x in range(11)]
print (numbers)

#zip
fruits = ['apple','banana','cherry']
colors = ['red','yellow','pink']
for fruits,colors in zip(fruits,colors):
    print(fruits, "is " , colors )
    
    
#continue  loop


for letter in "messi":
    if letter == "s" or letter == "i":

        continue
    print("curent letter:",letter)
    
    #break
for i in  'kim':
        if i == "k":
            break
print(i)
    

    