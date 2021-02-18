from django.contrib import admin
import nested_admin
from .models import Quiz, Question, Answer, Quizzer, Response

class AnswerInline(nested_admin.NestedTabularInline):
	model = Answer
	extra = 4
	max_num = 4

class QuestionInline(nested_admin.NestedTabularInline):
	model = Question
	inlines = [AnswerInline,]
	extra = 19

class QuizAdmin(nested_admin.NestedModelAdmin):
	inlines = [QuestionInline,]

class ResponseInline(admin.TabularInline):
	model = Response

class QuizzerAdmin(admin.ModelAdmin):
	inlines = [ResponseInline,]

admin.site.register(Quiz, QuizAdmin)
admin.site.register(Quizzer, QuizzerAdmin)
admin.site.register(Response)