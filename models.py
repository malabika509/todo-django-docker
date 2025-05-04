from django.db import models

# the model represents a single T?ask in out todo app
# stores title, description, date associated with each task
class Task(models.Model):

    title= models.CharField(max_length=255) # e.g. "Buy Groceries"
    
    description=models.TextField() # detailed description if needed
    
    date=models.DateField() # date when task was created or to be done


    def __str__(self):

        return self.title # makes tasks more readable in the shell