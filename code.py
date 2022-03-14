import csv 
import pandas as pd     

df=pd.read_csv("data1.csv")

final_data=df.dropna()
final_data.isnull().sum()

mass=final_data["Mass"].tolist()
radius=final_data["Radius"].tolist()
gravity=[]

def conversion(radius,mass):
    for i in range(0,len(radius)-1):
        mass[i]=mass[1] * 6.957e+8
        radius[1]= radius[1] * 6.957e+8
conversion(radius,mass)

def calculation(radius,mass):
    G=6.674e-11
    for i in range(0,len(mass)-1):
        try:
            print(radius[i])
            g=(mass[i]*G ) / ((radius[i])**2)
            gravity.append(g)
        except:
            pass
calculation(radius,mass)

df["Gravity"] = gravity