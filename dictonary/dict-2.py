d  = {111:"Raj",112:"kiran",113:"king"}
print(d)
print(d[111],d[112]) # Reading individual values from the dict by providing key

print(d.get(113)) # get is a function which can get the values by providing a key

#Displayin the key and values paiars using keys
for i in d.keys():
    print(f'{i}--->{d[i]}')
#Displayin the key and values pairs by using items
for i,j in d.items():
    print(f'{i}-->{j}')
    
