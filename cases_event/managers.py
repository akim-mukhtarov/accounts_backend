
from django.db import models
import random

class PresentsManager(models.Manager):
    def create(self, owner, category):
        present = self.model(
            owner= owner,
            category = category,
            present_in_category=self.__choose_present(category)
            )
        present.save()
        return present

    def __choose_present(self, category):
        presents=self.model.categories.presents_variants[category]
        pos=random.randint( 0, len(presents)-1 )
        present=presents[pos]
        return present


