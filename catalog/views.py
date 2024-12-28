from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

# def contacts(request):
#     return render(request, 'contacts.html')
#
#

def contacts(request):
    success = False
    if request.method == 'POST':
        success = True
    return render(request, 'contacts.html', {'success': success})
