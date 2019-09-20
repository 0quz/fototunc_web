from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect, Http404
from .models import Tracking
from .forms import TrackingForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.utils.text import slugify
from django.db.models import Q
from django.core.mail import send_mail

# Create your views here.
# Ana sayfa düzenleme görünüm
# request kullanıcı ile ilgili bilgiler getiren parametre
# url bölümüne home_view import ettik

def tracking_index(request):
    # eğer misafirse
    if not request.user.is_authenticated:
        tracking_list = Tracking.objects.all()
        query2 = request.GET.get('q')
        # ve query2 için misafir aramada tam takip kodu girerse listele
        if query2:
            tracking_list = tracking_list.filter(tracking_number__exact=query2).distinct()
        else:
        # eğer index'e başka yoldan ulaşmaya çalışırsa hata mesajı gönder
            return Http404()
        return render(request, 'tracking/index.html', {'trackings': tracking_list})

    else:
        # eğer kullanıcı admin ise
        tracking_list = Tracking.objects.all()
        query = request.GET.get('q')
        # filter methodu sorgulama yaparak liste döndürür
        if query:
            tracking_list = tracking_list.filter(
                Q(tracking_number__icontains=query) |
                Q(name__icontains=query) |
                Q(surname__icontains=query)
            ).distinct()

        paginator = Paginator(tracking_list, 12) # Show 5 contacts per page

        page = request.GET.get('sayfa')
        trackings = paginator.get_page(page)

        return render(request, 'tracking/index.html', {'trackings': trackings})


def tracking_detail(request, slug):
    tracking = get_object_or_404(Tracking, slug=slug)
    context = {
        'tracking': tracking,
    }

    return render(request, 'tracking/detail.html', context)


def tracking_create(request):
    if not request.user.is_authenticated:
        return Http404()
    # if request.method == "POST":
    #    print(request.POST)

    # name = request.POST.get('name')
    # surname = request.POST.get('surname')
    # tracking_number = request.POST.get('tracking_number')

    """
    if request.method == "POST":
        # Formdan gelen bilgileri kaydet
        # form değişkeni post nesnesi haline geldi
        form = TrackingForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        # Formu kullanıcıya göster
        form = TrackingForm()

    context = {
        'form': form,
    }
    """

    form = TrackingForm(request.POST or None)
    if form.is_valid():
        # kayıt et
        tracking = form.save(commit=False)
        # request nesnesinin yardımı ile istek yapan kullanıcı geliyor bunu da yazar olarak atıyoruz
        tracking.user = request.user
        # send_mail('Başlık', tracking.tracking_number, 'oguz.28414@gmail.com', ['nestuhurke@desoz.com'], fail_silently=False)
        tracking.save()
        messages.success(request, 'Başarılı bir şekilde oluşturuldu.')
        # kayıt edilen dosyanın içeriğine git
        return HttpResponseRedirect(tracking.get_absolute_url())

    context = {
        'form': form,
    }

    return render(request, 'tracking/form.html', context)


def tracking_update(request, slug):
    if not request.user.is_authenticated:
        return Http404()

    # tracking getirme komutu yani id numarasını
    tracking = get_object_or_404(Tracking, slug=slug)
    # form getirme komutu # tracking den bilgileri aldık instance ile
    form = TrackingForm(request.POST or None, instance=tracking)
    if form.is_valid():
        form.save()
        messages.success(request, 'Başarılı bir şekilde güncellendi.')
        return HttpResponseRedirect(tracking.get_absolute_url())

    context = {
        'form': form,
    }

    return render(request, 'tracking/form.html', context)


def tracking_delete(request, slug):
    if not request.user.is_authenticated:
        return Http404()

    tracking = get_object_or_404(Tracking, slug=slug)
    tracking.delete()
    # yönlendirme yaptık
    return redirect('tracking:index')