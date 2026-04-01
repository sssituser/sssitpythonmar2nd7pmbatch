d = {10:"krian",20:"raj",30:"pavan"}

print(d)
## how to add key and value pairs to dictionary
#1 way

d[11]="sai"
d[12] = "prabhas"

d.setdefault(100,"king")
d.setdefault(150,"queen")
d.update({33:"abb"})
d.__setitem__(103,"abc")

print(d)