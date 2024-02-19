# import string;

# dic = { 
#     'types' : ['int', 'float', 'string', 'char'], 
#     'sep' : ',', 
#     'end' : ';'
# } 

# res = { 
#     'alp' : list(string.ascii_letters + '_'), 
#     'dig' : list('0123456789')
# }

# def check(ident): 
     
#     for i in ident: 
#         if(i not in res['alp'] or i not in res['dig'] ):
#             return False 
    
#     return True

# def clear(list_idt): 
#     cleaned = list_idt[:] 
#     for i in range(len(cleaned)): 
#         cleaned[i] = cleaned[i].split(' ')
#     return cleaned


def cut(l,  res = []):    
    ind = l.find(';')  
    #print(l)
    #print(ind)
    if(len(l) == 0 or ind == -1): 
        return res
    else: 
        res.append(l[0: ind+1]) 
        return cut(l[ind+1:], res) 

#inp = input("Capture la lista de identificadores que desea revisar: ") 

#cutted = cut("int x, y, z; float x1;")

# if(list_ident[-1] == ''):


# list_idt = list_ident[:].split(';') 

# if(len(list_idt) > 1 or list_ident[-1] == ';'): 

# print(clear(list_ident))
# #if(len(list_ident) == 0 ) 

dic = { 
    'types': ['int', 'string', 'float', 'double', 'char']
}

def cut(l, res = []): #l => lista, res => lista resultado
    ind = l.find(';') 
    if(len(l) == 0 or ind == -1): 
        return res 
    else: 
        res.append(l[0: ind+1]) 
        return cut(l[ind+1:], res)
        #ind= list(map(lambda x: l.find(x) if (x in dic['types']) else None)) 
    # else:   
    #     res.append(l[0: ind_t+1])
    #     return cut(l[ind_t+1:], types[1:], res) 

def clean(l): 
    if(l[0] == ''): 
        return  

# def check(l): 
#     copy = l[:] 
#     print(list(map(lambda x: True if(x in copy) else False, l))) 
#     #return all(list(map(lambda x: True if(x in copy) else False, l)))        

inp = "intx,y,    z;               float x1;"
#inside_types = list(x for x in inp if x in dic['types']) 
cutted = cut(inp) 
ident_l = [list(map(lambda x: x.replace(' ', ''), x.split(','))) for x in cutted]  
#ident_l = [x.split(',') for x in cutted] 
print(cutted)
print("dfgdfg → ",ident_l)   

# if(check(inside_types)):  
#     print("Lista de identificadores invalida. \nExiste más de una lista declarada para el mismo tipo de dato.")  
# else: 
#     cutted = cut(inp)
