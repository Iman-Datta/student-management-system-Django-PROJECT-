from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from studentAPP.models import Marksheet

# def calculate_grade(marks):
#     if marks is None:
#         return 'Absent'
#     elif marks >= 90:
#         return 'A+'
#     elif marks >= 80:
#         return 'A'
#     elif marks >= 70:
#         return 'B+'
#     elif marks >= 60:
#         return 'B'
#     elif marks >= 50:
#         return 'C+'
#     elif marks >= 40:
#         return 'C'
#     else:
#         return 'F'
    
# @login_required
# def result(request):
#     if request.method == 'POST':
#         reg_number = request.POST.get('reg_number')
#         subjects = ['maths', 'chemistry', 'computer', 'physics', 'english']
#         exam_date = request.POST.get('exam_date')
#         for  sub in subjects:
#             marks = request.POST.get(sub)
#             if marks:
#                 try:
#                     marks = int(marks)
#                     grade = calculate_grade(marks)
#                 except ValueError:
#                     marks = None
#                     grade = 'Absent'
#             else:
#                 marks = None
#                 grade = 'Absent'

#             Marksheet.objects.create(
#                 student_id=reg_number,
#                 subject= sub,
#                 marks=marks,
#                 grade=grade,
#                 exam_date= exam_date
#             )
#         return render(request, 'teacherAPP/result.html', {'success': True, 'message': 'Result added successfully'})

#     return render(request, 'teacherAPP/result.html')

# @login_required
# def view_results(request):
    # if request.method == 'GET':
    #     results = Marksheet.objects.all
    #     return render(request, 'teacherAPP/view_results.html', {'results': results, 'reg_number': reg_number})
    # elif request.method == 'POST':
    #     reg_number = request.POST.get('reg_number')
    #     results = Marksheet.objects.filter(student_id=reg_number)
    #     return render(request, 'teacherAPP/view_results.html', {'results': results, 'reg_number': reg_number})   
    # return render(request, 'teacherAPP/view_results.html')