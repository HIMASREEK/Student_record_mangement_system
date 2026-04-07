from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Course, Student, Mark
from .forms import CourseForm, StudentForm, MarkForm


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'records/course_list.html', {'courses': courses})


def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Course added successfully!")
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'records/course_form.html', {'form': form})


def student_list(request):
    students = Student.objects.all().order_by('name')

    course_id = request.GET.get('course')
    search_query = request.GET.get('search')

    if course_id:
        students = students.filter(course_id=course_id)

    if search_query:
        students = students.filter(name__icontains=search_query)

    courses = Course.objects.all()

    total_students = Student.objects.count()
    total_courses = Course.objects.count()
    total_marks = Mark.objects.count()

    return render(request, 'records/student_list.html', {
        'students': students,
        'courses': courses,
        'total_students': total_students,
        'total_courses': total_courses,
        'total_marks': total_marks,
    })


def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Student added successfully!")
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'records/student_form.html', {'form': form})


def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    marks = student.marks.all()

    total_marks = sum(mark.score for mark in marks)
    subject_count = marks.count()
    average_marks = total_marks / subject_count if subject_count > 0 else 0

    if average_marks >= 90:
        grade = 'A+'
    elif average_marks >= 80:
        grade = 'A'
    elif average_marks >= 70:
        grade = 'B'
    elif average_marks >= 60:
        grade = 'C'
    elif average_marks >= 50:
        grade = 'D'
    else:
        grade = 'F'

    status = 'Pass' if average_marks >= 40 else 'Fail'

    return render(request, 'records/student_detail.html', {
        'student': student,
        'marks': marks,
        'total_marks': total_marks,
        'average_marks': round(average_marks, 2),
        'grade': grade,
        'status': status,
    })


def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Student updated successfully!")
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'records/student_form.html', {'form': form})


def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        messages.success(request, "Student deleted successfully!")
        return redirect('student_list')
    return render(request, 'records/confirm_delete.html', {'object': student})


def add_mark(request):
    if request.method == 'POST':
        form = MarkForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Mark added successfully!")
            return redirect('student_list')
    else:
        form = MarkForm()
    return render(request, 'records/mark_form.html', {'form': form})