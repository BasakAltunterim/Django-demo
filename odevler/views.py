from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import TeslimForm
from .models import exam, deadline, Student

@login_required(login_url='giris')
def home(request):
    odevler = exam.objects.all()
    return render(request, 'odevler/homepage.html', {'exam': odevler})

@login_required(login_url='giris')
def exam_detail(request, exam_id):
    odev = exam.objects.get(id=exam_id)
    form = TeslimForm()
    today = timezone.now().date()

    if request.method == 'POST':
        form = TeslimForm(request.POST, request.FILES)
        if form.is_valid():
            teslim = form.save(commit=False)
            teslim.sinav = odev
            teslim.save()
            return redirect('home')

    return render(request, 'odevler/exam_detail.html', {
        'exam': odev,
        'form': form,
        'today': today
    })
@login_required(login_url='giris')
def teslim_edilen_list(request):
    ogrenci_id=request.GET.get('ogrenci')
    teslimler=deadline.objects.all()

    if ogrenci_id:
        teslimler=teslimler.filter(ogrenci__id=ogrenci_id)

    ogrenciler=Student.objects.all()

    return render(request, 'odevler/teslim_edilen_list.html', {'teslimler': teslimler,'ogrenciler': ogrenciler})


def student_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error_message = "Geçersiz kullanıcı adı veya şifre."
            return render(request, 'odevler/student_login.html', {'error_message': error_message})
    return render(request, 'odevler/student_login.html')

def kullanici_cikis(request):
    logout(request)
    return redirect('giris')




from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentSerializer, ExamSerializer, DeadlineSerializer

@api_view(['GET'])
def api_students(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def api_exams(request):
    exams = exam.objects.all()
    serializer = ExamSerializer(exams, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def api_deadlines(request):
    deadlines = deadline.objects.all()
    serializer = DeadlineSerializer(deadlines, many=True)
    return Response(serializer.data)    

