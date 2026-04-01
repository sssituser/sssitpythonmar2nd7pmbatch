d = {1:"raj",2:"ravi",3:"kiran",4:"charan",5:"mohan",6:"ratan"}

evens = {key: value for key, value in d.items() if key % 2 == 0}

print(evens)