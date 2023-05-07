# -*- coding: utf-8 -*-
"""
Created on Sun May  7 19:46:57 2023

@author: Degoland
"""


import numpy as np
import pandas as pd

    

data=pd.read_excel("C:/Users/Degoland/Downloads/TechKariyer.xlsx", skiprows=1,sheet_name='Data')

#login için datayı pandas ile çekiyorum
df1 = pd.DataFrame(data, columns=['Login Dönemi', 'Firma Kodu','Login Adet'])

#çektiğim datayı liste haline getiriyorum
login_data_list=df1.values.tolist()

login_dict={}

#her bir firma için zaman ve veri yi bir tuple içinde saklayan bir dictionary oluşturuyorum
for ch in login_data_list:
    if ch[1] not in login_dict:
        login_dict[ch[1]]=([ch[0]],[ch[2]])
    else:
        date=ch[0]
        sıklık=ch[2]
        login_dict[ch[1]][0].append(date)
        login_dict[ch[1]][1].append(sıklık)
        

data2=pd.read_excel('C:/Users/Degoland/Downloads/TechKariyer.xlsx', skiprows=1, sheet_name='Data',usecols=[4,5,6])
#aynı şekilde ilan dönemleri için datayı pandas ile çekiyorum
df2=pd.DataFrame(data2)

#listeleme
ilan_data_list=df2.values.tolist()

ilan_dict={}

for ch in ilan_data_list:
    if ch[1] not in ilan_dict:
        ilan_dict[ch[1]]=([ch[0]],[ch[2]])    
    else:
        date=ch[0]
        sıklık=ch[2]
        ilan_dict[(ch[1])][0].append(date)
        ilan_dict[(ch[1])][1].append(sıklık)

#şuan her iki kayıt için tarihler ve adet sayıları için dictionary oluşturdum 
#bundan sonra her iki dictionary için aynı firmaları tarih ve adet sayılarıyla
#karşılaştırarak ikisi arasında korelasyon olup olmadığını görmeye çalışacağız

valuesforlogin=[]
valuesforilan=[]
for ch in login_dict.keys():
    #login dictionary den aldığımız firma kodunu ilan dictionaryde bulup içindeki tarihleri arıyorum
    try:
        for i in range(len(ilan_dict[ch][0])):
            if ilan_dict[ch][0][i] in login_dict[ch][0]:
            #eğer tarihler eşleşiyorsa her ikisi için de adet sayısını oluşturduğum listeye çekeceğim 
            #ve en sonunda aralarında korelasyon arayacağım
                valuesforilan.append(ilan_dict[ch][1][i])
                #tarihin indexini login dict için de bulmaya çalışacağım
                index=login_dict[ch][0].index(ilan_dict[ch][0][i])
                valuesforlogin.append(login_dict[ch][1][index])            
    except:
        pass
                


#numpy ile veriler arasında korelasyon olup olmadığını kontrol edeceğim

korelasyon_matrix=np.corrcoef(valuesforilan,valuesforlogin)

print(korelasyon_matrix)


