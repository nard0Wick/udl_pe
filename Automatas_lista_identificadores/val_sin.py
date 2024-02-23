#print("int x, y, z".split(';', -1))  

l = []
def indexOF(word, char): 
    if(char not in word): 
        #return len(word)  
        return -1
    else: 
        return word.index(char) 
    
def sp(str): 
    if(len(str) == 0): 
        return l
    else:
        inx = indexOF(str, ';') 
        if(inx != -1):
            l.append(str[:inx + 1]) 
            return sp(str[inx + 1:])  
        else: 
            l.append(str[:]) 
            return sp("")

def prepare(str): 
    if(',' not in str): 
        return str
    else:
        return [str[:str.index(',')]]
    
#print("ello"[5])
#print(sp("int x1 , x2   ,x3; float x1, x2")) 
print(len("hello"))

for i in sp("x1,x2"): 
    print(prepare(i))