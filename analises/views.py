from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage

def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStimport osorage()
        name = fs.save(uploaded_file.name, uploaded_file)
    return render(request, 'dashboard-admin/analises.html', context)

def upload_list(request):
    return render(request, 'dashboard-analises.html')

def upload_book(request):
    return render(request, 'upload_book.html')