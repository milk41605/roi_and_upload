from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

import time
import os

from uploads.core.models import Document
from uploads.core.forms import DocumentForm



def home(request):
    documents = Document.objects.all()
    return render(request, 'core/home.html', { 'documents': documents })


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'core/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'core/simple_upload.html')


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            fileName = time.strftime('%Y%m%d_%H%M%S') + '.' + request.FILES['document'].name.split('.')[-1]
            request.FILES['document'].name = fileName
            DocumentForm(request.POST, request.FILES).save()
            os.makedirs(os.path.join(os.getcwd(), 'original_img', request.POST['location']), exist_ok=True)
            os.rename(os.path.join(os.getcwd(), 'original_img', fileName), os.path.join(os.getcwd(), 'original_img', request.POST['location'], fileName))
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'core/model_form_upload.html', {
        'form': form ,
        'documents' : list(reversed(Document.objects.all()))[:10]
    })
#
#
# def model_form_upload_images(request):
#     if request.method == 'POST':
#         form = DocumentForm_images(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = DocumentForm_images()
#     return render(request, 'core/model_form_upload_images.html', {
#         'form': form
#     })
