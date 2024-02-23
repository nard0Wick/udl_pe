import string 

alf = string.ascii_letters  
dig = "0123456789"

def check_i(ident): 
    #revisa que un identificador sea sintácticamente correcto 
    bool = list(map(lambda x: False if(x not in alf + dig and x != '_') else True, ident)) 

    if(ident[0] not in alf):
        return(True, "Identificador invalido, el primer valor de \'" + ident + "\' debe ser una letra")
    elif(not all(bool)): 
        return(True, "Identificador invalido, no debe contener caracteres especiales \'"+ ident[bool.find(False)] +"\'") 
    else: 
        return(False, "El identificador es sintácticamente correcto") 

print(''.join(['int x', ' ,y ,z ; float x2, y2 , z2  ']).count(','))

def check_l(l): 
    if(len(l) == 0): 
       return 
    else: 
        #incu = l.count(',') 
        incu_l = list(i for i in range(len(inp)) if(len[i] == ','))
        checked = check_i(l[0]) 
        if(checked[0]): 
            return checked 
        return check_l(l[1:])

#         if(len(l) > 0): 
#             check_i(l[0]) 
#             return check_l(l[1:]) 

inp = "int x, ,y ,z ; float x2, y2 , z2  "  

#inp = "int x"  
#print(inp.split(';')) 
if(inp[0] not in alf): 
    print("Error sintáctico cerca de \'"+inp[0]+"\'") 
else: 
    l = list(map(lambda x: x.split(),inp.split(';'))) 
    print(l) 
