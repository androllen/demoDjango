import datetime

from django.db import models
from django.utils import timezone


# 问题描述和发布时间
class Question(models.Model):
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.question_time >= timezone.now()-datetime.timedelta(days=1)

    question_text = models.CharField(max_length=200)
    question_time = models.DateTimeField("date published")


# 选项描述和当前票数
class Choice(models.Model):
    def __str__(self):
        return self.choice_text
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
