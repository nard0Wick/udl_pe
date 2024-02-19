import string

def cut(w, res =[]):   
    ind = w.find(' ')
    if(len(w) == 0): 
            return res;   
    elif(w[0] != ' '): 
        if(ind != -1): 
            res.append(w[: ind])  
            return cut(w[ind +1:])
        else: 
            res.append(w[:]) 
            return res
    else: 
            return cut(w[1:]) 
         
alf = string.ascii_letters 
dig = "0123456789" 

def check(ident): 
    #revisa que un identificador sea sintácticamente correcto 
    bool = list(map(lambda x: False if(x not in alf + dig and x != '_') else True, ident)) 

    if(ident[0] not in alf):
        return(True, "Identificador invalido, el primer valor de " + ident + " debe ser una letra")
    elif(not all(bool)): 
        return(True, "Identificador invalido, no debe contener caracteres especiales \'"+ ident[bool.find(False)] +"\'") 
    else: 
        return(False, "El identificador es sintácticamente correcto") 

#inp = input("Capture una o varias listas de identificadores: ") 
#l_ident = [x.split(',') for x in ("int x, y z;").split(';')] 
l_ident = [x.split(',') for x in "int x, y z;".split(';')] 

for i in l_ident: 
    print(i)

#print(cut(l_ident[0][1]))


#-- Lista anidada de elementos, de acuerdo a divisiones de vez primera por ';' 
#posteriormente por ',' -- 

#next step: validar la sintaxis de cada lista de identificadores(sublista)


