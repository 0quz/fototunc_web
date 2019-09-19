from django.db import models
from django.core.validators import RegexValidator
from django.urls import reverse
from django.utils.text import slugify
#from phone_field import PhoneField

# Create your models here.

class Tracking(models.Model):
    user = models.ForeignKey('auth.User', verbose_name='Yazar', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name='Ad')
    surname = models.CharField(max_length=100, verbose_name='Soyad')
    email = models.EmailField(verbose_name='Email', blank=True)
    phone_number = models.CharField(verbose_name='Telefon Numarası', max_length=11,
                                    validators=[RegexValidator(r'^\d{11}$')], blank=True)
    # phone_number = PhoneField(max_length=11, blank=True)
    tracking_number = models.CharField(verbose_name='Takip Kodu', max_length=10,
                                       validators=[RegexValidator(r'^\d{10}$')])
    status = models.TextField(verbose_name='Durum')
    information = models.TextField(verbose_name='Açıklama', blank=True)
    publishing_date = models.DateTimeField(verbose_name='Yükleme Tarihi', auto_now_add=True)
    # başlık bilgisinin yer aldığı bölüm slug True dememizin sebebi artık id yerine slug alanı kullanacağız
    # slug = models.SlugField(unique=True, editable=False)
    slug = models.SlugField(unique=True, editable=False)

    def __str__(self):
        return '{self.name} {self.surname}'.format(self=self)

    def get_absolute_url(self):
        # 'id' detail.urlsinde tanıttığımız id
        return reverse('tracking:detail', kwargs={'slug': self.slug})

    def get_create_url(self):
        return reverse('tracking:create')

    def get_update_url(self):
        # 'id' detail.urlsinde tanıttığımız id
        return reverse('tracking:update', kwargs={'slug': self.slug})

    def get_delete_url(self):
        # 'id' detail.urlsinde tanıttığımız id
        return reverse('tracking:delete', kwargs={'slug': self.slug})

    # bu kısım aynı slugdan yani tracking_numberdan varsa sağ kısmına +1 sayısı ekler
    #def get_unique_slug(self):
    #    slug = slugify(self.tracking_number)
    #    unique_slug = slug
    #    counter = 1
    #    while Tracking.objects.filter(slug=unique_slug).exists():
    #        unique_slug = '{}-{}'.format(slug, counter)
    #        counter +=1
    #    return unique_slug

        #slug kaydı için
    def save(self, *args, **kwargs):
        # tracking_number artık sayfa numarası olarak gözükecek
        # if not self.slug: başlık değiştiğinde slug alanı değişmesin
            # self.slug = self.get_unique_slug()
        self.slug = slugify(self.tracking_number)
        return super(Tracking, self).save(*args, **kwargs)

    class Meta:
        # yayınlanma tarihine göre sıralama
        ordering = ['-publishing_date']