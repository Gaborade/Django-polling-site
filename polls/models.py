from django.db import models
import datetime
from django.utils import timezone

# this in inheritance by the way. Overriding the models.Model class
# Each model is a subclass of django.db.models.Model

# Each model has a number of class variables, each represent a database field in the model eg model.CharField
# This tells Django what each field holds

# The name of each Field instance eg question_text or votes variable becomes the Field's name
# and the database will use as the column name


class Question(models.Model):
    """ The Question will consist of a question and a publication date"""
    question_text = models.CharField(max_length=200) 
    pub_date = models.DateTimeField('date published') # by passing a string as the first positional argument, to
    # designate to field a human readable name. In this case, Question.pub_date becomes date published

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    """A Choice has two fields: the text of the choice and the vote tally.
    Each Choice is associated to a Question"""
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # the ForeignKey implies that
    # each Choice is related to a single Question. It is a database relationship
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
# Create your models here.
 