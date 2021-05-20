from django.shortcuts import render
from django.contrib.auth.decorators import login_required


#DASHBOARD HOME
@login_required
def admin_dashboard(request):
    return render(request, 'dashboard-admin/index.html')

@login_required
def analitico_dashboard(request):
    return render(request, 'dashboard-admin/analitico.html')

@login_required
def artigos_dashboard(request):
    return render(request, 'dashboard-admin/artigos.html')

@login_required
def forum_dashboard(request):
    return render(request, 'dashboard-admin/forum.html')

@login_required
def produtos_dashboard(request):
    return render(request, 'dashboard-admin/produtos.html')

@login_required
def usuarios_dashboard(request):
    return render(request, 'dashboard-admin/usuarios.html')

@login_required
def vendas_dashboard(request):
    return render(request, 'dashboard-admin/vendas.html')