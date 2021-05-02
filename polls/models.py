from django.db import models
import datetime

from django.utils import timezone

# Create your models here.
class Question(models.Model):
            # fields of the model 
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
        # renames the instances of the model with their question_text  
    def __str__(self): # add  __str__() method to both Question and Choice to make data more readable
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    ## optional work for making admin Ui more readable
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class GeeksModel(models.Model): 
    title = models.CharField(max_length = 200) 
    description = models.TextField() 
    last_modified = models.DateTimeField(auto_now_add = True) 
    img = models.ImageField(upload_to = "images/") 

    def __str__(self): 
        return self.title 



    


