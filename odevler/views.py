from django.shortcuts import render, redirect
from .models import exam, deadline
from .forms import TeslimForm

def home(request):
    odevler = exam.objects.all()
    return render(request, 'odevler/homepage.html', {'exam': odevler})

def exam_detail(request, exam_id):
    odev = exam.objects.get(id=exam_id)
    form = TeslimForm()

    if request.method == 'POST':
        form = TeslimForm(request.POST, request.FILES)
        if form.is_valid():
            teslim = form.save(commit=False)
            teslim.sinav = odev
            teslim.save()
            return redirect('home')

    return render(request, 'odevler/exam_detail.html', {'exam': odev, 'form': form})


def teslim_edilen_list(request):
    teslimler=deadline.objects.all()
    return render(request, 'odevler/teslim_edilen_list.html', {'teslimler': teslimler})