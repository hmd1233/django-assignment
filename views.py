from django.shortcuts import render, get_object_or_404
from .models import Course, Question, Choice, Submission


def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)

    if request.method == "POST":
        submission = Submission.objects.create()

        for question in Question.objects.filter(course=course):
            choice_id = request.POST.get(str(question.id))
            if choice_id:
                choice = Choice.objects.get(pk=choice_id)
                submission.choices.add(choice)

        return show_exam_result(request, submission.id)

    questions = Question.objects.filter(course=course)

    return render(
        request,
        "onlinecourse/exam.html",
        {"course": course, "questions": questions},
    )


def show_exam_result(request, submission_id):
    submission = Submission.objects.get(pk=submission_id)

    selected_choices = submission.choices.all()

    total_score = 0

    for choice in selected_choices:
        if choice.is_correct:
            total_score += choice.question.grade

    context = {
        "submission": submission,
        "selected_choices": selected_choices,
        "score": total_score,
    }

    return render(
        request,
        "onlinecourse/exam_result.html",
        context,
    )
