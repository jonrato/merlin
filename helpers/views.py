from django.shortcuts import render

def handle_not_found(request,exception):
    return render(request, 'helpers/not_found.html')