from django.db import models


class Question(models.Model):
    content = models.CharField(max_length=200)
    grade = models.IntegerField(default=1)

    def __str__(self):
        return self.content


class Choice(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE
    )
    content = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.content


class Submission(models.Model):
    choices = models.ManyToManyField(Choice)

    def __str__(self):
        return f"Submission {self.id}"
