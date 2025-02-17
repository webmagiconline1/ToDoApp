from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def mark_completed(self):
        self.completed = True
        self.save()

    def mark_incomplete(self):
        self.completed = False
        self.save()