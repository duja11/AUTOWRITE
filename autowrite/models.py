from django.db import models

class User(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    date_inscription = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class Trend(models.Model):
    mot_cle = models.CharField(max_length=255)
    frequence = models.IntegerField(default=0)
    date_analyse = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.mot_cle}"

class Prompt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contenu = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prompt {self.id}"

class Generation(models.Model):
    prompt = models.ForeignKey(Prompt, on_delete=models.CASCADE)
    contenu_genere = models.TextField()
    date_generation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Generation {self.id}"