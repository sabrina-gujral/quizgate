from django.db import models
from django.contrib.auth.models import User

class Quiz(models.Model):
	name = models.CharField(max_length=250)
	question_count = models.IntegerField(default=0)
	description = models.CharField(max_length=500)
	date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	slug = models.SlugField()
	roll_out = models.BooleanField(default=False)

	class Meta:
		ordering = ['date_created',]

	def __str__(self):
		return self.name

class Question(models.Model):
	question = models.ForeignKey(Quiz, on_delete=models.CASCADE)
	label = models.CharField(max_length=100)
	order = models.IntegerField(default=0)

	def __str__(self):
		return self.label

class Answer(models.Model):
	answer = models.ForeignKey(Question, on_delete=models.CASCADE)
	content = models.CharField(max_length=500)
	correct = models.BooleanField(default=False)

class Quizzer(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
	correct = models.IntegerField(default=0)
	incorrect = models.IntegerField(default=0)
	unattempted = models.IntegerField(default=0)
	completed = models.BooleanField(default=False)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.username

class Response(models.Model):
	quiztaker = models.ForeignKey(Quizzer, on_delete=models.CASCADE)
	question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, blank=True)
	answer = models.ForeignKey(Answer, on_delete=models.CASCADE, null=True, blank=True)

	def __str__(self):
		return self.question.label




