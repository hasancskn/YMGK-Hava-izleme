# YMGK-Hava-ızleme

#Kullanılan Kütüphaneler ve Kurulumları

cmd üzerinde ilk yazılan yükleme seçenekleri, Terminal için ikinci yazılan yükleme seçenekleri kullanılmalıdır.
-from skimage.measure import compare_ssim #pip install scikit-image -or- sudo apt-get install python-skimage
-import imutils							  #pip install imutils -or- sudo apt-get install imutils
-import cv2								  #pip install opencv-python -or- sudo apt install python3-opencv
-import selenium						  #pip install selenium -or- Adım1:sudo apt-get install python-pip Adım2:sudo pip install selenium
-import pandas 							  #pip install pandas 
-import matplotlib.pyplot				  #pip install matplotlib
-import datetime
-import os



#Selenium kütüphanesinin kullanacağı webdriver için;

"https://chromedriver.storage.googleapis.com/index.html?path=83.0.4103.39/" 
web sitesi üzerinden işletim sistemimize uygun olan dosya indirilir.

Windows için:

Bilgisayar => Özellikler => Gelişmiş Sistem Ayarları => Ortam Değişkenleri pencereleri açılır.
Sistem Değişkenleri bölümünden Path değişkeni seçilir yeni diyerek indirdiğimiz dosyanın bulunduğu yol buraya eklenir.

Linux için; 

İndirilen driverın bulunduğu dosya dizininde terminali açarak echo "export PATH=$(pwd):\${PATH}" &gt;&gt; ~/.bashrc komutu
çalıştırılır.

###########################################################################################################################################

28.03.2020-03.04.2020 tarihleri arasında PM10-SO2-CO-NO2-NO-O3 verileri sırasıyla http://www.havaizleme.gov.tr/ sitesi üzerinden elde edildi.

Elde edilen veri seti sanayi bölgesine ait verilerdir. Bu sayede, COVID-19 tedbirlerinin alındığı dönemde iş yerlerinin gaz salınımı, araç trafiklerinin ne durumda olduğu ile alakalı sonuçlar çıkarılabilir.

Günlük olarak gaz salınımının değişimi grafikselleştirilerek gösterilmiştir.

#havaizleme.py 
Verilerin görselleştirilmesini ve günlük değişimin kullanıcı tarafından görüntülenmesini sağlar

#Max-Min.py
Verilerin maksimum ve minimum olduğu tarih aralıklarını bulur.

#CrossValidation.py
Veriler üzerinde hem sınıflandırma hem de öğrenme işlemi yaparak çapraz doğrulama yöntemi ile doğru veri tahmini skoru elde edilir.

#VeriYorumlama.py
Verilere ait ortalama değerleri kullanarak son kullanıcıya yorumlanan verinin gösterimini ekrana yazar.

#degisim.py
İstasyona ait web sitesinde ki değişimi güncel olarak ekran görüntüsü olarak alıp ve değişikliklerin bulunduğu noktaları işaretler. Başlangıçta hazır ekran görüntüsü kullanılmaz sistem tamamen otomatikleştirilmiş 
şekilde işlemlerini yapar. Her çalıştırıldığında bulunduğu zaman bilgilerini içeren bir klasör adı oluşturulur ve bu klasör içerisine eski ve yeni ekran görüntülerinde farkların çizildiği şekli atanır.
Görüntü işleme teknolojileri kullanılmıştır.
