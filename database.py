import numpy as np                                    #untuk simbol-simbol
from sklearn.linear_model import LinearRegression     #memanggil library regresi linear
import pandas as pd

#database
#x = Data, y = target
x = [[1],[3],[5],[7],[9]] 
y = [2, 6, 10, 14, 18]          
FileDB = 'perkalian.txt'
Database = pd.read_csv(FileDB, sep = ",", header = 0)
print("-----------------------------------------------")
print(Database)
#x = Data, y = target
x = Database[[u'x']]
y = Database.Target

regr = LinearRegression().fit(x,y)                    #untuk fitting grafik
regr.score(x, y)                                      #untuk menentukan grafik

#data uji
predict = np.array([[110 ]])                            #nilai yang di prediksi

#menampilkan data prediksi (menampilkan karakter)
print ("Prediksi") 
print ("input = ", predict)
print ("Output =", regr.predict(predict))
