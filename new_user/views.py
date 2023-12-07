from django.shortcuts import render

def main(request):
    return render(request, 'new_user.html')