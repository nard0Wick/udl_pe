import string
# lista = ['a', 'b', 'c', 'd', 'o']
# string = "hola, cómo están" 

# gen = list(x  for x in string if x in lista) 
# print(gen) 
def cut(w, res):   
    ind = w.find(' ')
    if(len(w) == 0): 
            return res;   
    elif(w[0] != ' '): 
        if(ind != -1): 
            res.append(w[: ind])  
            return cut(w[ind +1:], res)
        else: 
            res.append(w[:]) 
            return res
    else: 
            return cut(w[1:], res) 

alf = string.ascii_letters 
dig = "0123456789" 
def check_i(ident): 
    #revisa que un identificador sea sintácticamente correcto 
    bool = list(map(lambda x: False if(x not in alf + dig and x != '_') else True, ident)) 

    if(ident[0] not in alf):
        return(True, "Identificador invalido, el primer valor de " + ident + " debe ser una letra")
    elif(not all(bool)): 
        return(True, "Identificador invalido, no debe contener caracteres especiales \'"+ ident[bool.find(False)] +"\'") 
    else: 
        return(False, "El identificador es sintácticamente correcto") 

types = ['int', 'float', 'string', 'char'] 

#print(list(map(lambda x: cut(x, []), types)))  
# l = []
# for i in range(len(types)): 
#      l.append(cut(types[i]))

# print(l)

def check_l(l): 
    n_l = cut(l[0], []) + l[1:] 
    print(n_l) 
    if(n_l[0] not in types): 
         return (True, "Tipo de dato invalido " + n_l[0]) 
    else: 
         #print("list before: ",n_l[1:]) 
         for i in n_l[1:]:  
            print(i)
            cutted = cut(i, [])
            #print(cutted) 
            checked = check_i(cutted[0]) 
            #print(type(cutted))
            if(len(cutted) > 1): 
                if(checked[0]): 
                    #manejo de resultados 
                    print(checked)      
                else: 
                    #manejo de resultados  
                    print(True, "Error de sintaxis, después de " + cutted[0]) 
                break
            else: 
                #manejo de resultados 
                print(checked)          

 
lista = [x.split(',') for x in " float x ,1yo, z b2    ;    ".split(';')]
print(check_l(lista[0]))



