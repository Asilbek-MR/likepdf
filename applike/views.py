from django.shortcuts import render
# frontend/views.py
import os
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from .forms import PDFUploadForm
# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_POST, require_GET
from .forms import PDFMergeForm
from PyPDF2 import PdfMerger
import io


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

# def merge(request):
#     return render(request, 'merge.html')
# Constants
MAX_FILES = 5
MAX_SIZE_BYTES = 10 * 1024 * 1024  # 10 MB


from django.http import JsonResponse

def merge_pdfs(request):
    if request.method == "POST":
        files = request.FILES.getlist("pdf_files")

        # === Validatsiya ===
        if len(files) == 0:
            return JsonResponse({"success": False, "message": "❌ Hech qanday fayl yuklanmadi!"})

        if len(files) > 5:
            return JsonResponse({"success": False, "message": "❌ Faqat 5 ta fayl yuklashingiz mumkin!"})

        for f in files:
            if f.size > 5 * 1024 * 1024:
                return JsonResponse({"success": False, "message": f"❌ {f.name} hajmi 5MB dan katta!"})

        # === PDF merge qilish ===
        merger = PdfMerger()
        for f in files:
            merger.append(f)

        buffer = io.BytesIO()
        merger.write(buffer)
        merger.close()
        buffer.seek(0)

        # Session ichida saqlaymiz (faylni keyin yuklash uchun)
        request.session["merged_pdf"] = buffer.getvalue().hex()

        return JsonResponse({
            "success": True,
            "message": "✅ Fayllar muvaffaqiyatli birlashtirildi!",
            "download_url": request.build_absolute_uri("?download=1")
        })

    # Faylni yuklab olish
    if request.GET.get("download"):
        pdf_data = request.session.get("merged_pdf")
        if not pdf_data:
            return HttpResponse("❌ Fayl topilmadi!", status=404)

        buffer = io.BytesIO(bytes.fromhex(pdf_data))
        response = HttpResponse(buffer, content_type="application/pdf")
        response["Content-Disposition"] = 'attachment; filename="merged.pdf"'
        return response

    return render(request, "merge.html")

    # if request.method == "POST":
    #     form = PDFMergeForm(request.POST, request.FILES)
    #     files = request.FILES.getlist("pdf_files")

    #     # === Validatorlar ===
    #     if len(files) == 0:
    #         return HttpResponse({"error": "❌ Hech qanday fayl yuklanmadi!"})

    #     if len(files) > 5:
    #         return JsonResponse({"success": False, "message": "Faqat 5 ta fayl yuklashingiz mumkin!"})

    #     for f in files:
    #         if f.size > 5 * 1024 * 1024:
    #             return JsonResponse({"success": False, "message": f"{f.name} hajmi 5MB dan katta!"})

    #     if form.is_valid() and files:
    #         return JsonResponse({"success": True, "message": "Fayllar muvaffaqiyatli birlashtirildi!"})


    #     if form.is_valid():
    #         merger = PdfMerger()
    #         for f in files:
    #             print(f.name)
    #             merger.append(f)

    #         buffer = io.BytesIO()
    #         merger.write(buffer)
    #         merger.close()
    #         buffer.seek(0)

    #         response = HttpResponse(buffer, content_type="application/pdf")
    #         response["Content-Disposition"] = 'attachment; filename="merged.pdf"'
            
    #         return response
    # else:
    #     form = PDFMergeForm()
    # return render(request, "merge.html", {"form": form})
    


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

    
