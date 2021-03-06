# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 11:13:25 2015

@author: pccb
"""
#from alimentos import NutritionFactsCalPerGram
from alimentos import alimentoscsv
from alimentos import alimentosproteinascsv
from alimentos import alimentoscarboidratescsv
from alimentos import alimentosfatcsv
from alimentos import proteins
from alimentos import carboidrates
from alimentos import fat

dados_usuario= open("usuario.csv","r")
leitura=dados_usuario.readlines()


def CalculaTaxaMetabolismoBasal(peso,altura,idade):
    TMB= 88.36+(13.4*weight)+(4.8*height)-(5.7*age)
    return TMB

def CalculaTMBmultAF():
    taoccd=CalculaTaxaMetabolismoBasal(weight,height,age)*1.725
    return taoccd

def ReturnWeight():
    Weight = weight
    return Weight
    
def ReturnHeight2():
    Height2 = height**2
    return Height2
    

def CalculaBMI(ReturnWeight,ReturnHeight2):
    BMI=(ReturnWeight())/(ReturnHeight2())  
    return BMI

def ReturnTypeBMI():
    if CalculaBMI(ReturnWeight,ReturnHeight2)<18.5:
        print("Você está abaixo do peso")
    elif 18.5<=CalculaBMI(ReturnWeight,ReturnHeight2)<25:
        print("Você tem peso ideal")
    elif 25<=CalculaBMI(ReturnWeight,ReturnHeight2)<30:
        print("Você esta ligeiramente acima do peso")
    else:
        print("Você esta muito acima do peso")
        

    
UserFoodGramsWeek={}
UserDayCaloriesWeek={}
UserDayProteinsWeek={}
UserDayCarboidratesWeek={}
UserDayFatWeek={}

userpeaces = leitura[1].split(",")
name = userpeaces[0]
age = int(userpeaces[1])
weight = float(userpeaces[2])
sex = userpeaces[3]
height = float(userpeaces[4])
fator = userpeaces[5]

NutritionFactsCalPerGram = alimentoscsv()
NutritionFactsProteinsPerGram=alimentosproteinascsv()
NutritionFactsCarboidratesPerGram=alimentoscarboidratescsv()
NutritionFactsFatPerGram=alimentosfatcsv()
#print(NutritionFactsCalPerGram)
print(NutritionFactsProteinsPerGram)

def usuariocarboidratoscsv():
    x=0
    for linha in leitura[3:]:
        x+=1
        userpeaces = linha.strip().split(',')
        #print(userpeaces)
        usergramsamount=float(userpeaces[2])
        #print(type(usergramsamount))
        food=userpeaces[1]
        grams=usergramsamount
        date=userpeaces[0]
        #amountofcaloriesperfood=grams*
        UserDayCarboidratesWeek[date]=NutritionFactsCarboidratesPerGram[food]*grams
        for date in UserDayCarboidratesWeek:
            if date in UserDayCarboidratesWeek:
                UserDayCarboidratesWeek[date]+=NutritionFactsCarboidratesPerGram[food]*grams
            else:
                 UserDayCarboidratesWeek[date]+=NutritionFactsCarboidratesPerGram[food]*grams
    #print("UserDayCarboidratesWeek: ",UserDayCarboidratesWeek)
usuariocarboidratoscsv()

def usuariocaloriascsv():
    x=0
    for linha in leitura[3:]:
        x+=1
        userpeaces = linha.strip().split(',')
        usergramsamount=float(userpeaces[2])
        food=userpeaces[1]
        grams=usergramsamount
        date=userpeaces[0]
        UserDayCaloriesWeek[date]=NutritionFactsCalPerGram[food]*grams
        for date in UserDayCaloriesWeek:
            if date in UserDayCaloriesWeek:
                UserDayCaloriesWeek[date]+= NutritionFactsCalPerGram[food]*grams
            else:
                UserDayCaloriesWeek[date]=NutritionFactsCalPerGram[food]*grams
    #print("UserDayCaloriesWeek: ",UserDayCaloriesWeek)
usuariocaloriascsv()

def usuarioproteinascsv():
    x=0
    for linha in leitura[3:]:
        x+=1
        userpeaces = linha.strip().split(',')
        usergramsamount=float(userpeaces[2])
        food=userpeaces[1]
        grams=usergramsamount
        date=userpeaces[0]
        UserDayProteinsWeek[date]=NutritionFactsProteinsPerGram[food]*grams
        for date in UserDayProteinsWeek:
            if date in UserDayProteinsWeek:
                UserDayProteinsWeek[date]+=NutritionFactsProteinsPerGram[food]*grams
            else:
                UserDayProteinsWeek[date]=NutritionFactsProteinsPerGram[food]*grams  
    #print("UserDayProteinsWeek: ",UserDayProteinsWeek)
usuarioproteinascsv()

def usuariofatcsv():
    x=0
    for linha in leitura[3:]:
        x+=1
        userpeaces = linha.strip().split(',')
        usergramsamount=float(userpeaces[2])
        food=userpeaces[1]
        grams=usergramsamount
        date=userpeaces[0]
        UserDayFatWeek[date]=NutritionFactsFatPerGram[food]*grams
        for date in UserDayFatWeek:
            if date in UserDayFatWeek:
                UserDayFatWeek[date]+=NutritionFactsFatPerGram[food]*grams
            else:
                UserDayFatWeek[date]=NutritionFactsFatPerGram[food]*grams  
    #print("UserDayFatWeek: ",UserDayFatWeek)
usuariofatcsv()

'''               
    #print("Sua taxa de metabolismo basal é ",CalculaTaxaMetabolismoBasal(weight,height,sex))
    #print("Seu gasto calorico diário é de ",CalculaTMBmultAF()," calorias.")
    #print("O seu índice de massa corporal é de ",CalculaBMI(ReturnWeight,ReturnHeight2), "Kg/m2")
    #ReturnTypeBMI()    
'''