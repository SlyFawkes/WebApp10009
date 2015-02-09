from django.db import models

# Create your models here.
class Question(models.Model):
    # ...
    def __unicode__(self):              # __unicode__ on Python 2
        return self.question_text

class Choice(models.Model):
    # ...
    def __unicode__(self):              # __unicode__ on Python 2
        return self.choice_text