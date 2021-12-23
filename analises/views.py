from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from .forms import UploadFileForm
from .models import FileUpload

from django.contrib.auth.decorators import login_required

@login_required
def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
    return render(request, 'dashboard-admin/analises.html', context)

@login_required
def upload_list(request):
    files = FileUpload.objects.all()
    return render(request, 'dashboard-analises.html',
    {'files':files}
    )

@login_required
def upload_list_dashboard(request):
    files = FileUpload.objects.all()
    return render(request, 'upload_book.html',
    {'files':files}
    )

@login_required
def upload_book(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard-analises-dashboard')
    else:
        form = UploadFileForm()
    return render(request, 'upload_upload_book.html', {'form':form})

#Link p/ deletar arquivos
## https://www.youtube.com/watch?v=roYopMO4Eo8