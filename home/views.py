from django.shortcuts import render, HttpResponse


# Create your views here.
# Ana sayfa düzenleme görünüm
# request kullanıcı ile ilgili bilgiler getiren parametre
# url bölümüne home_view import ettik

def home_view(request):
    # Eğer kullanıcı giriş yaptı ise ismini yazdır yapmadı ise Misafir olarak tanımla
    if request.user.is_authenticated:
        # içerikler birden fazla ise bu şekilde tanımlamak daha iyi olur
        # isim anahtar ilişkisine dayalı olacak
        context = {
            'isim': 'Oğuz',
        }
    else:
        context = {
            'isim': 'Misafir',
        }
    # home.html dosyası
    # home.html dosyasını templatesden home klasörüne çağırıyoruz
    # view fonksiyonlarından html dosyalarına içerik göndereceğiz içeriği dinamikleştirmek için
    return render(request, 'home.html', context)
