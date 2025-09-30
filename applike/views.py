from django.shortcuts import render
# frontend/views.py
import os
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from .forms import PDFUploadForm
# Create your views here.
from django.http import HttpResponse

def home(request):
    return render(request, 'index.html')

def auth(request):
    return render(request, 'auth.html')

def compress(request):
    return render(request, 'compress.html')

def convert(request):
    return render(request,'convert.html')

def editpdf(request):
    return render(request, 'editpdf.html')

def merge(request):
    return render(request, 'merge.html')

def pdftojpg(request):
    return render(request,'pdftojpg.html')

def pdftoword(request):
    return render(request,'pdftoword.html')

def price(request):
    return render(request,'price.html')

def protect(request):
    return render(request,'protect.html')

def signpdf(request):
    return render(request,'signpdf.html')

def split(request):
    return render(request,'split.html')

def unlock(request):
    return render(request,'unlock.html')



def upload_pdf(request):
    """Handle AJAX PDF upload."""
    if request.method == "POST" and request.FILES.get("pdf_file"):
        form = PDFUploadForm(request.POST, request.FILES)
        if form.is_valid():
            pdf = form.cleaned_data["pdf_file"]

            # Save file to MEDIA_ROOT/uploads/
            upload_dir = os.path.join(settings.MEDIA_ROOT, "uploads")
            os.makedirs(upload_dir, exist_ok=True)
            file_path = os.path.join(upload_dir, pdf.name)

            with open(file_path, "wb+") as dest:
                for chunk in pdf.chunks():
                    dest.write(chunk)

            return JsonResponse({
                "status": "success",
                "message": "File uploaded successfully!",
                "file_url": settings.MEDIA_URL + "uploads/" + pdf.name
            })
        else:
            return JsonResponse({"status": "error", "message": "Invalid form data."})
    return JsonResponse({"status": "error", "message": "Invalid request."})

    
