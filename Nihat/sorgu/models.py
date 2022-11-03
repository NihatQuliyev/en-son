from django.db import models
import datetime                                                                   # sual modelmizin icine elave olunan 'bu yaxin' funksiyasi ucun :)
from django.utils import timezone                                                 # zona vaxti ucun
class Sual(models.Model):                                                         # sual modelim
    sual_text = models.CharField(max_length=200)                                  # daxil etdiyim sual_text
    cap_tarixi = models.DateTimeField('cap olundu :')                             # cap tarixiqeyd etmek ucun
    def __str__(self):                                                            # yaradilan sualin  ustunde qeyd olunmasi
        return self.sual_text

    def bu_yaxin(self):
        return self.cap_tarixi >= timezone.now() - datetime.timedelta(days=1)

class Cavab(models.Model):                                                        # cavab modelim
    sual = models.ForeignKey(Sual, on_delete=models.CASCADE)                      # verilen suala kecid modeli
    cavab_text = models.CharField(max_length=200)                                 # daxil etdiyim cavab_text
    votes = models.IntegerField(default=0)                                        # ses modeli
    def __str__(self):                                                            # yaradilan cavabin ustunde , yazilan yavabin eks olunmasi
        return self.cavab_text