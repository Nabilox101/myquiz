from django.db import models

class Quiz(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class QuizQuestion(models.Model):
    QUESTION_TYPES = (
    ('image_choice', 'Image Choice'),
    ('text_choice', 'Text Choice'),
    ('textinputquestion', 'Text Input'),
    )
    
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    score = models.IntegerField(default=1)
    question_type = models.CharField(max_length=20, choices=QUESTION_TYPES)

    def __str__(self):
        return self.question_text

class ImageChoice(models.Model):
    def image_upload_path(instance, filename):
        return f"quiz_images/{instance.question.quiz.id}/{instance.question.id}/{filename}"

    question = models.ForeignKey(QuizQuestion, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_upload_path, blank=True, null=True)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.image.url

class TextChoice(models.Model):
    question = models.ForeignKey(QuizQuestion, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text

class TextInputQuestion(models.Model):
    question = models.ForeignKey(QuizQuestion, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)


    def __str__(self):
        return self.answer_text

    