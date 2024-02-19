import pandas as pd
import openpyxl as opx  
import numpy as np 
import matplotlib.pyplot as plt 




workbook = opx.load_workbook(filename="Libro.xlsx")
sheet = workbook.active 
data_tuples = sheet.values 

 
#1st option O(n) n = number of rows
#mini = min(data[0]) 
#maxi = max(data[0]) 
#length = len(data[0])
##print(len(data)) 
#for i in range(1, len(data)):  
#    #print(i)
#    if(mini > min(data[i])): 
#        mini = min(data[i]) 
#
#    if(maxi < max(data[i])): 
#        maxi = max(data[i]) 
#    
#    length += len(data[i]) 
#
#print(mini, maxi, length) 
#A = (maxi - mini)/length 

#for i in range(no_cls): 
#    #print(i) 
#    data['num_class'].append(i +1) 
#    data['class_range'].append(())

#iter = [(1,2),(3,4)] 

#2nd option O(n+1) n = number of rows 


#data = list(map(lambda x: 0 if(x == None) else x,concat(data_tuples)))  
data = list(value for value in sum(data_tuples, ()) 
                if(value != None))
#print(data)#the problem is that aparently if you don't provide a value on the excel the cill will be auto-filled with none

#basic variables
length = len(data)
mini = min(data)
maxi = max(data) 
no_cls = 6
A = (maxi - mini) / no_cls 

content = {  
    'num_class' : list(range(1,no_cls+1)), 
    'ranges_list': [(mini+A*i, mini+A*(i+1)) for i in range(no_cls)], 
    'abs_frecuency':[0 for i in range(no_cls)]
}  

# absolute frecuency
for i in data: 
    for j in range(no_cls):   
        if(i>= content['ranges_list'][j][0] and i < content['ranges_list'][j][1]): 
            content['abs_frecuency'][j] += 1 
            break

content['abs_frecuency'][-1] += length - sum(content['abs_frecuency']) 
#stored frecuency 
std_frecuency = [sum(content['abs_frecuency'][0:i]) for i in range(1, no_cls + 1)]
content['std_frecuency'] = std_frecuency

#x
x = list(map(lambda x: x[0] + A/2, content['ranges_list']))
content['x'] = x

#relative frecuency 
rel_frecuency = list(map(lambda x: x/length, content['abs_frecuency'])) 
content['rel_frecuency'] = rel_frecuency

#percentages 
content['percentages'] = list(map(lambda x: str(x * 100) + '%', content['rel_frecuency'])) 

#degrees 
content['degrees'] = list(map(lambda x: x * 360, content['rel_frecuency'])) 

#view of table 
print(pd.DataFrame(data=content))

#aritmethic mean  
mean = sum(map(lambda x, y: x*y, content['abs_frecuency'], content['x'])) / length 
#median 
#there are some needed values for median and mode calculous 
line = (length + 1)/2 
match = list(std for std in content['std_frecuency'] 
            if std >= line)[0] 
idx = content['std_frecuency'].index(match)

inferior = content['ranges_list'][idx][0]#it's the value of the lowest limit that holds the current value on line variable
Fi = content['std_frecuency'][idx -1]#means the value for stored frecuency acording to the line varible
fi = content['abs_frecuency'][idx]#refers to the value of the absolute frecuency meaning the value of line variable 
median = inferior + ((length/2 - Fi)/fi) * A 
#print(median, mean)

#mode 
fi_lower = content['abs_frecuency'][idx -1] 
fi_upper = content['abs_frecuency'][idx +1] 
mode = inferior + ((fi - fi_lower) / (fi  - fi_lower + fi - fi_upper)) * A #probably will need a correction
#print(fi, fi_lower, fi_upper)

#standar deviation
deviation = ((sum(list(map(lambda x, y: x * (y - mean)**2, content['abs_frecuency'], content['x'])))) / length -1) **(1/2)
#deviation = list() 

#Printing things done
print(f"\nPrimer Examén de probabilidad y estadística\nICO 821-14 Ramírez Lara Gonzalo Leonardo\nArithmetic mean: {mean}\nMedian: {median}\nMode: {mode}\nEstandar deviation: {deviation}")

#view graphics  
fig, (ax1, ax2) = plt.subplots(1, 2, figsize = (12,6))  
ax1.pie(content['degrees'], labels=content['num_class'], autopct="%.1f%%")  
##ax2.title('Histogram')  
ax2.bar(x=content['num_class'], height=content['abs_frecuency']) 
plt.tight_layout() 
plt.show() 

#plt.figure(figsize=(5,5))  
#plt.pie(content['degrees'], labels=content['num_class'], autopct="%.1f%%")
#plt.show() 
#
#plt.figure(figsize=(5,5))   
#plt.bar(x=content['num_class'], height=content['abs_frecuency'])
#plt.show()


#print(content['abs_frecuency'])
#for i in range(no_cls): 
#    
#
#print(content['ranges_list'])
#newArr = map(lambda x=0: x, iter) 
#print(mini, maxi, length, A)