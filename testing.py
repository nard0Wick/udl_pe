import pandas as pd
import openpyxl as opx  
import numpy as np 
import matplotlib.pyplot as plt 

workbook = opx.load_workbook(filename="Libro.xlsx")
sheet = workbook.active 
data_tuples = sheet.values 

set_tuples = data_tuples 
result = list(value for value in sum(set_tuples, ()) 
            if (value != None))
print(result))  
#print(data_tuples)