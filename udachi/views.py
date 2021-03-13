from django.shortcuts import render

# Create your views here.
from udachi.models import Bluda


def render_page_home(request):

    bluda_iz_topa = Bluda.objects.order_by('kolvo_dobavlenia_v_korzinu')[0:7]

    return render(request, 'udachi/home.html', {
        'bluda_iz_topa':bluda_iz_topa
    })

def render_page_bluda_lv(request):

    bluda = Bluda.objects.filter(ne_pokazivat=False)

    return render(request, 'udachi/bluda_lv.html', {
        'bluda':bluda
    })