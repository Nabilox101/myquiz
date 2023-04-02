from django.contrib import admin
from .models import Quiz, QuizQuestion, ImageChoice, TextChoice , TextInputQuestion
from django import forms


class ImageChoiceInline(admin.TabularInline):
    model = ImageChoice
    extra = 3  # Set the default number of choices to 3
    fields = ['image', 'is_correct']


class TextChoiceInline(admin.TabularInline):
    model = TextChoice
    extra = 3  # Set the default number of choices to 3
    fields = ['text', 'is_correct']


class QuizQuestionInline(admin.StackedInline):
    model = QuizQuestion
    extra = 1  # Set the default number of questions to 1
    fields = ['question_text', 'question_type']
    inlines = [ImageChoiceInline, TextChoiceInline]


class TextInputQuestionForm(forms.ModelForm):
    class Meta:
        model = TextInputQuestion
        exclude = ['question_type']



@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    inlines = [QuizQuestionInline]
    list_display = ['title']


@admin.register(ImageChoice)
class ImageChoiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'is_correct']
    list_filter = ['question__quiz__title', 'question__question_text', 'is_correct']
    search_fields = ['id', 'question__question_text', 'question__quiz__title']


@admin.register(TextChoice)
class TextChoiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'is_correct']
    list_filter = ['question__quiz__title', 'question__question_text', 'is_correct']
    search_fields = ['id', 'question__question_text', 'question__quiz__title']

@admin.register(TextInputQuestion)
class TextInputQuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'is_correct']
    list_filter = ['question__quiz__title', 'question__question_text', 'is_correct']
    search_fields = ['id', 'question__question_text', 'question__quiz__title']
