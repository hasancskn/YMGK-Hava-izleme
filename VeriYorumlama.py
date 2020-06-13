# -*- coding: utf-8 -*-
import pandas as pd

data=pd.read_excel("veri.xlsx")#veriokundu

#veri tipinin floata çevrilmesi
data['PM10'] = data['PM10'].astype('float')
data['SO2'] = data['SO2'].astype('float')
data['CO'] = data['CO'].astype('float')
data['NO2'] = data['NO2'].astype('float')
data['NO'] = data['NO'].astype('float')
data['O3'] = data['O3'].astype('float')

#Ortalama değerler bulunuyor 
ortPM10=sum(data['PM10'])/len(data['PM10'])
ortSO2=sum(data['SO2'])/len(data['SO2'])
ortCO=sum(data['CO'])/len(data['CO'])
ortNO2=sum(data['NO2'])/len(data['NO2'])
ortNO=sum(data['NO'])/len(data['NO'])
ortO3=sum(data['O3'])/len(data['O3'])


if ortPM10>=40:
    print("\n Partiküler Madde (PM10) ve çapı 10 mikrometreden küçük diğer tanecikler akciğerlere ulaşarak iltihaplanmaya ya da insanları çok olumsuz etkileyecek kalp ve akciğer hastalıklarına neden olabilirler.")
    print("\n Bu tarihlerde AB standartları üzerinde bir PM10 değeri hesaplanmıştır")
    print("\n Bu bölge COVID-19 yüzünden ölüm oranını yükseltebilir. İnsanların çoğunda akciğer hastalıklarına yatkınlık bulunmakta.")
else:
    print("PM10 değeri standartlara uyuyor. Bu bölgede insanlar daha az akciğer hastalığına yakalanır.")


if ortSO2>=125:
    print("Kükürt dioksit (SO2) insanlar için doğrudan zehirleyicidir; temel olarak solunum fonksiyonlarını etkiler. Sülfürik asit ve sülfat formuna dönüşmesi durumunda insan sağlığını dolaylı olarak tehdit edebilir.")
    print("Sanayi bölgesi olduğundan bu bölgede yoğun bir kullanım vardır.")
else:
    print("SO2 sınırı aşılmamıştır, sanayi bölgesi olmasına rağmen gaz salınımı azdır.")

if ortNO2>=200:
    print("\n Havadaki yüksek NO2 oranının kalp/dolaşım sistemi üzerindeki etkileri genelde kısa vadede ani kalp ölümlerine neden olurken, NO2’ye bağlı olarak gelişen solunum yolları hastalıkları uzun vadede ölüme yol açmakta")
    print("\n Bu bölgede Azot diOksit emisyonu çok fazladır. Bu tarihlerde çok sıkı bir araç trafiği olduğunu anlayabiliriz.")
else:
    print("Bu tarihlerde araç trafiği az olduğundan dizel araç kullanımı bu bölgede azalmıştır.")