from django.shortcuts import render

def main(request):
    return render(request, 'page_photo.html')