from skimage.measure import compare_ssim
import imutils #Kenar algılama işlemleri için kullanılır.
import cv2 #Görüntü işleme, görüntüler üzerinde çizim yapma amaçlı kullanılır.
from selenium import webdriver #Bir web sitesinde otomatikleştirilecek işlemler için kullanılır.
from datetime import datetime #Zaman verilerinin alınması için kullanılır.
import os #Dosya işlemleri için kullanılır.


#Başakşehir Hava izleme istasyonuna ait web sitesi
url='https://sim.csb.gov.tr/Services/Details?id=6d169752-eabc-4f7e-87ea-6cf10b452486'


#yeni screenshot alınacak görüntü için anlık tarih ve saat bilgisini döner.
def time():

    timenow = datetime.now()
    timenowpath = str(timenow).replace(":", ".")#dosya adı oluşturulurken ":" kullanılmadığından replace kullanarak "." işareti ile değiştirilir.

    os.mkdir(timenowpath) #çalıştırıldığı anda ki gün,ay,yıl ve saat bilgilerini içeren bir dosya oluşturulur.

    return timenowpath #geri dönüş olarak oluşturulan dosya adı verilir.


#Verilen URLde bulunan web sayfasına ait ekran görüntüsünü alır.
def ss(URL):

    options = webdriver.ChromeOptions()#Özel ayarların kullanılabilmesini sağlar.
    options.headless = True
    driver = webdriver.Chrome(options=options)
    driver.get(URL)


    #Açılacak web sayfasının tamamına ait ekran görüntüsü elde ederiz.
    S = lambda X: driver.execute_script('return document.body.parentNode.scroll' + X)#Web sayfasına ait en ve boy değerleri bulunur.
    driver.set_window_size(S('Width'), S('Height'))#Bulunan en ve boy değerleri windows penceresine göre boyutlandırılır.


    #Eğer dizinde oldss.png dosyası yoksa alınan ilk ss oldss.png ve newss.png dosyası olarak atanır.
    if os.path.exists(os.getcwd() + "/oldss.png") == False:
        oldss = driver.find_element_by_tag_name('body').screenshot('oldss.png')
        newss = driver.find_element_by_tag_name('body').screenshot('newss.png')


    # Eğer bulunulan dizinde newss.png dosyası var ise önce oldss değişkenine atanır daha sonra newss dosyası oluşturulur.
    elif os.path.exists(os.getcwd() + "/oldss.png") == True and os.path.exists(os.getcwd()+"/newss.png")==True:
        oldss=cv2.imread("newss.png")
        newss=driver.find_element_by_tag_name('body').screenshot('newss.png')#Sayfanın tamamına ait ekran görüntüsü kaydedilir.
        cv2.imwrite("oldss.png",oldss)#Eski ekran görüntüsü kaydedilir.


    else:
        newss = driver.find_element_by_tag_name('body').screenshot('newss.png')  # Sayfanın tamamına ait ekran görüntüsü kaydedilir.

    driver.quit()
    return os.getcwd() #İçinde bulunduğumuz dizin adı string olarak döndürülür.


#İki resim arasında fark alınacağından ve kenar bulma algoritması kullanıldığından X,Y değerleri fonksiyon içerisinde hesaplanmaktadır.
def different(URL):
    ss(URL) # Dönüş değerleri bir değişkende saklanır.

    imageA = cv2.imread("oldss.png")
    imageB = cv2.imread("newss.png")
    h,w,channel=imageA.shape

    # İki resim arasında karşılaştırılma yapmadan önce boyutları eşit hale getirilir.
    imageB=cv2.resize(imageB,(w,h))
    grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY) #Resimler griye dönüştürülür.
    grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY) #Resimler griye dönüştürülür.
    (score, diff) = compare_ssim(grayA, grayB, full=True) #Resimler arasındaki farklar ve fark değeri hesaplanır.
    diff = (diff * 255).astype("uint8")

    # Piksel değerlerini eşik değerine göre ayarlar.
    thresh = cv2.threshold(diff, 0, 255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

    #Belirli bir alanda çizim işleminin gerçekleştirilmesini sağlar.
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    # Çizimlerin gerçekleştirildiği kod bloğu.
    for c in cnts:
        (x, y, w, h) = cv2.boundingRect(c)  #Her piksel için moment değeri hesaplanır.
        #Çizimin yapılacağı noktalar belirlendi ve her iki dosya için farklı olan yerler işaretlendi.
        cv2.rectangle(imageA, (x, y), (x + w, y + h), (0, 0, 255), 3)
        cv2.rectangle(imageB, (x, y), (x + w, y + h), (0, 0, 255), 3)


    #Görüntüleri görmek istersek açılacak kod bloğudur.
    #cv2.imshow("Original", imageA)
    #cv2.imshow("Modified", imageB)

    # Dosyaların o anda ki gün,ay,yıl ve saat bilgileri ile açılmış dizine geçilir ve old.png ve new.png dosyaları oluşturulur.
    os.chdir(time())
    cv2.imwrite("old.png",imageA)
    cv2.imwrite("new.png", imageB)

    cv2.waitKey(0)



#Ana kod bloğudur. Farklılıkların hesaplanacağı different fonksiyonu çağırılır.
def main():
    different(url)

main()