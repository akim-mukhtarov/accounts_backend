from django.db import models
from django.db.models import Sum
from .managers import PresentsManager
from .categories import Categories
import json
import datetime

class Partisipant(models.Model):
    tg_id = models.IntegerField()
    
    def get_available_categories(self):
        resp_obj = {}
        resp_obj['exceeded'] = self.is_exceeded()

        available_categories = tuple(filter(
            lambda x: self.sum_for_cases>=x['required_amount'],
            PartisipantPresent.categories.conditions
        ))
    
        resp_obj['available_categories']=available_categories
        
        return json.dumps(
                obj=resp_obj,
                ensure_ascii=False
                )


    def is_exceeded(self):
        if self.opened_today_count() >= 30:
            return True
        return False
    
    @property
    def sum_for_cases(self):
        return self.pays_today_sum-self.opened_today_sum

    @property
    def pays_today_sum(self):
        return PartisipantPay.objects.filter(
            date=datetime.date.today()
            ).aggregate(sum=Sum('amount'))['sum'] or 0
            
    @property
    def opened_today_sum(self):
        return PartisipantPresent.objects.filter(
            date=datetime.date.today()
            ).aggregate(sum=Sum('category'))['sum'] or 0

    def opened_today_count(self):
        return PartisipantPresent.objects.filter(
            date=datetime.date.today()
            ).count()


class PartisipantPay(models.Model):
    account = models.ForeignKey(
        Partisipant,
        models.CASCADE
        )
    amount = models.DecimalField(
        max_digits = 8,
        decimal_places = 2
        )
    date = models.DateField(
        auto_now = True
        )

class PartisipantPresent(models.Model):
    owner = models.ForeignKey(
        Partisipant,
        models.CASCADE
        )
    date = models.DateField(
        auto_now = True
        )
    '''
    BASE = 250
    BOYAR = 500
    RICH = 1000
    MECENAT = 2000

    CATEGORIES_CHOICES = (
        (BASE, 'базовый'),
        (BOYAR, 'боярский'),
        (RICH, 'богач'),
        (MECENAT, 'меценат'),
    )
    
    CATEGORIES = (
        BASE,
        BOYAR,
        RICH,
        MECENAT
    )

    PRESENTS_IN_CATEGORY = {
        BASE: [],
        BOYAR: [],
        RICH: [],
        MECENAT: []
    }
    '''
    categories = Categories()

    category = models.IntegerField(
        choices = categories.choices
        )
    present_in_category = models.CharField(
        max_length=50
        )

    objects = PresentsManager()
