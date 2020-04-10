# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import pandas as pd

data=pd.read_excel("veri.xlsx")#veriokundu

#veri tipinin floata çevrilmesi
data['PM10'] = data['PM10'].astype('float')
data['SO2'] = data['SO2'].astype('float')
data['CO'] = data['CO'].astype('float')
data['NO2'] = data['NO2'].astype('float')
data['NO'] = data['NO'].astype('float')
data['O3'] = data['O3'].astype('float')


plt.figure(figsize=(40,40))
plt.subplot(2,2,1)
plt.plot(data.Tarih,data.PM10,color="red")
plt.plot(data.Tarih,data.SO2,color="blue")
plt.plot(data.Tarih,data.NO2,color="black")
plt.plot(data.Tarih,data.NO,color="orange")
plt.plot(data.Tarih,data.O3,color="gray")
plt.xlabel("Tarih")
plt.ylabel("PM10-SO2-NO2-NO-O3 Miktarı")
plt.title("Zamana Göre PM10(Red)-SO2(Blue)-NO2(Black)-NO(Orange)-O3(Gray) değişimi")

plt.subplot(2,2,2)
plt.plot(data.Tarih,data.CO,color="green")
plt.xlabel("Tarih")
plt.ylabel("CO Miktarı")
plt.title("Zamana Göre CO değişimi")

plt.show()


