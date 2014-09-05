from django.http import JsonResponse
from django.http import HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from distributor.models import make_dist_adv_list, Distributor, Advertisement
from weighted_choice import advert_choice, advert_choice_pid
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from distributor.serializers import AdvertSerializer

persistent = {}

@csrf_exempt
def advert_select(request):
    """view for lookup adverts"""
    if request.method == 'POST':
        distr_percent_advs_list = make_dist_adv_list()
        aa = advert_choice(distr_percent_advs_list)
        a = Advertisement.objects.get(id=aa[1])
        distributor = Distributor.objects.get(name=a.distributor.name)
        distributor.shown_adverts += 1
        distributor.save()
        response = JsonResponse({'distributor': a.distributor.name,
                                 'banner': a.banner.url,
                                 'banner_link': a.banner_link})
    else:
        return HttpResponseNotFound('<h1>use Post instead of GET method</h1>')
    return response


@csrf_exempt
def advert_select_pid(request):
    """view for lookup adverts"""
    if request.method == 'POST':
        distr_percent_advs_list = make_dist_adv_list()
        aa = advert_choice_pid(distr_percent_advs_list, persistent)
        distributor = Distributor.objects.get(name=aa[0])
        a = Advertisement.objects.get(distributor=distributor, id=aa[1])
        distributor.shown_adverts = persistent[distributor.name]
        distributor.save()
        response = JsonResponse({'distributor': a.distributor.name,
                                 'banner': a.banner.url,
                                 'banner_link': a.banner_link})
    else:
        return HttpResponseNotFound('<h1>use Post instead of GET method</h1>')
    return response
