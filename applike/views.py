from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return render(request, 'index.html')

def auth(request):
    return render(request, 'auth.html')


# frontend/views.py
import os
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from .forms import PDFUploadForm


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

    
