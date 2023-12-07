from django.shortcuts import render

def main(request):
    return render(request, 'sent_list.html')