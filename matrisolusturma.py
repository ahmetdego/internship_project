# -*- coding: utf-8 -*-
""""
Created on Sun May  7 18:19:"33 2023

@author: Degoland
"""
#importing numpy so that we can concatenate rows
import numpy as np

#creating rows 
firstrow='Aylık Ortama İlan'
secondrow=[' ','Firma Sayıları','0-5 İlan','5-10 İlan','10+ İlan']
thirdrow= ['Aylık','0-10 Login']
fourtrow=['Ortalama','10-100 Login']
fifthrow=['Login','100+ Login']

#create gaps in boxes for empty values
gaps=np.array([' ',' ',' '])
thirdrow=np.hstack([thirdrow,gaps])
fourtrow=np.hstack([fourtrow,gaps])
fifthrow=np.hstack([fifthrow,gaps])

#concatenating rows
table=np.vstack([secondrow,thirdrow,fourtrow,fifthrow])

#creating header
print((15*2-1)*' ',end='|')
print(f'{firstrow.center(43)}','|')
    

#creating table
for row in table:
    for column in row:
        print(f'{column:14s}',end='|')
    print(75*'_')
    