from django.shortcuts import render,get_object_or_404,redirect              # elave edilmeyen sual ve ya cavab olduqda 404 susmaya qarsi

from django.http import HttpResponseRedirect                                # elaqe funksiyasi dasiyir

from django.urls import reverse                                              # urlde yaratdigimiz name sablon adlarindan istifade ucun

from .models import Sual,Cavab                                               # modelde yaratdigimiz sual,cavab modellerinin tanitimi


def esas(request):                                                           # esas sehife funksiyam
    sual_list = Sual.objects.order_by('-cap_tarixi')[:5]                     # qeyd olunan en son 5 sual

    context = {'sual_list': sual_list}

    return render(request, 'sorgu/esas.html', context)                       # html file ile etrafli(detail) sehifeye kecidin yaradilmasi


def etrafli(request, niko_id):                                               # etrafli yeni cavablarin oldugu sehife
    sual = get_object_or_404(Sual, pk=niko_id)

    return render(request, 'sorgu/etrafli.html', {'sual': sual})


def netice(request, niko_id):                                                # sesvermeden sonra acilan sehife
    sual = get_object_or_404(Sual, pk=niko_id)

    return render(request, 'sorgu/netice.html', {'sual': sual})


def vote(request, niko_id):                                                  # vote(sesverme) sehifesi
    sual = get_object_or_404(Sual, pk=niko_id)

    try:

        selected_choice = sual.cavab_set.get(pk=request.POST['cavab57'])

    except (KeyError, Cavab.DoesNotExist):

        return render(request, 'sorgu/etrafli.html', {                       # sesvermenin netice sehifesine yansimasi ucun kecid
            'sual': sual,
            'error_message': " Cavab secin.",
        })

    else:
        selected_choice.votes += 1

        selected_choice.save()

        return HttpResponseRedirect(reverse('sorgu:netice', args=(sual.id,)))






