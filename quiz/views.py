from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Quiz, QuizQuestion, ImageChoice, TextChoice , TextInputQuestion

def quiz_list(request):
    quizzes = Quiz.objects.all()
    context = {'quizzes': quizzes}
    return render(request, 'quiz_list.html', context)

def question_quiz_list(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    questions = QuizQuestion.objects.filter(quiz=quiz)

    # loop through the questions and retrieve their choices
    for question in questions:
        image_choices = question.imagechoice_set.all()
        text_choices = question.textchoice_set.all()
        text_input_question = question.textinputquestion_set.all()


        # check if the question has image choices
        if image_choices:
            question.has_image_choices = True
            question.choices = image_choices
        else:
            question.has_image_choices = False

        # check if the question has text choices
        if text_choices:
            question.has_text_choices = True
            question.text_choices = text_choices
        else:
            question.has_text_choices = False

         # check if the question has text input choices
        if text_input_question:
            question.has_text_input_question = True
            question.text_input_question = text_input_question
        else:
            question.has_text_input_question = False    

    context = {'questions': questions, 'quiz': quiz}
    return render(request, 'question_quiz_list.html', context)



def result(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    questions = QuizQuestion.objects.filter(quiz=quiz)

    user_responses = {}
    score = 0

    if request.method == 'POST':
        for question in questions:
            user_response = request.POST.get('question_{}'.format(question.id))
            user_responses[question.id] = user_response
            if question.question_type == 'image_choice':
                correct_choice = ImageChoice.objects.filter(question=question, is_correct=True).first()
                if correct_choice is not None and user_response == str(correct_choice.id):
                    score += question.score
            if question.question_type == 'text_choice':
                correct_choice = TextChoice.objects.filter(question=question, is_correct=True).first()
                if correct_choice is not None and user_response == str(correct_choice.id):
                    score += question.score
            if question.question_type == 'textinputquestion':
                correct_answer = TextInputQuestion.objects.get(question=question, is_correct=True)
                if user_response.lower() == correct_answer.answer_text.lower():
                    score += question.score
        context = {'user_responses': user_responses, 'quiz': quiz, 'score': score, 'total_questions': len(questions)}
        return render(request, 'result.html', context)
    else:
        for question in questions:
            if isinstance(question, TextInputQuestion):
                question.field_name = 'question_{}'.format(question.id)
            else:
                choices = []
                image_choices = question.imagechoice_set.all()
                text_choices = question.textchoice_set.all()
                if image_choices.exists():
                    for choice in image_choices:
                        choices.append({'id': choice.id, 'image': choice.image.url, 'is_correct': choice.is_correct})
                elif text_choices.exists():
                    for choice in text_choices:
                        choices.append({'id': choice.id, 'text': choice.text, 'is_correct': choice.is_correct})
                question.choices = choices

        return render(request, 'question_quiz_list.html', {'quiz': quiz, 'questions': questions})
