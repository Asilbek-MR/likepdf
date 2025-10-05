from django.shortcuts import render
# frontend/views.py
import os
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from .forms import PDFUploadForm
# Create your views here.
from django.http import HttpResponse, JsonResponse, FileResponse
from django.views.decorators.http import require_POST, require_GET
from .forms import PDFMergeForm
from PyPDF2 import PdfMerger,PdfReader, PdfWriter
import io

def home(request):
    return render(request, 'index.html')

def auth(request):
    return render(request, 'auth.html')


import tempfile
import subprocess
import logging

logger = logging.getLogger(__name__)

def compress(request):
    """
    Complete PDF compression with smart fallback system
    Automatically uses best available method:
    1. Ghostscript (50-70% compression) - BEST
    2. pikepdf (40-60% compression) - GOOD
    3. PyPDF2 (20-30% compression) - BASIC
    """
    
    # GET request - show form
    if request.method == 'GET':
        return render(request, 'compress.html')
    
    # POST request - process compression
    if request.method == 'POST':
        try:
            # Get form data
            pdf_file = request.FILES.get('pdf')
            compression_level = request.POST.get('compression_level', 'medium')
            
            # Validate file
            if not pdf_file:
                return JsonResponse({'error': 'No file uploaded'}, status=400)
            
            if not pdf_file.name.endswith('.pdf'):
                return JsonResponse({'error': 'Only PDF files are allowed'}, status=400)
            
            # Check file size (50MB limit)
            if pdf_file.size > 50 * 1024 * 1024:
                return JsonResponse({'error': 'File too large. Maximum 50MB allowed'}, status=400)
            
            logger.info(f"Compressing {pdf_file.name} with {compression_level} level")
            
            # Try compression methods in order of quality
            compressed_buffer = None
            method_used = None
            
            # Method 1: Try Ghostscript (BEST)
            try:
                compressed_buffer = _compress_ghostscript(pdf_file, compression_level)
                method_used = 'Ghostscript'
                logger.info("Used Ghostscript compression")
            except Exception as e:
                logger.warning(f"Ghostscript failed: {str(e)}")
            
            # Method 2: Try pikepdf (GOOD)
            if compressed_buffer is None:
                try:
                    import pikepdf
                    compressed_buffer = _compress_pikepdf(pdf_file, compression_level)
                    method_used = 'pikepdf'
                    logger.info("Used pikepdf compression")
                except Exception as e:
                    logger.warning(f"pikepdf failed: {str(e)}")
            
            # Method 3: Use PyPDF2 (BASIC - always works)
            if compressed_buffer is None:
                try:
                    compressed_buffer = _compress_pypdf2(pdf_file, compression_level)
                    method_used = 'PyPDF2'
                    logger.info("Used PyPDF2 compression")
                except Exception as e:
                    logger.error(f"All compression methods failed: {str(e)}")
                    return JsonResponse({'error': 'Compression failed'}, status=500)
            
            # Return compressed file
            compressed_buffer.seek(0)
            
            response = FileResponse(
                compressed_buffer,
                as_attachment=True,
                filename=f'compressed_{pdf_file.name}'
            )
            response['Content-Type'] = 'application/pdf'
            response['X-Compression-Method'] = method_used
            
            return response
            
        except Exception as e:
            logger.error(f"Compression error: {str(e)}")
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Invalid request method'}, status=405)


def _compress_ghostscript(pdf_file, compression_level):
    """Ghostscript compression - 50-70% reduction"""
    quality_map = {
        'low': '/printer',
        'medium': '/ebook',
        'high': '/screen'
    }
    quality = quality_map.get(compression_level, '/ebook')
    
    # Create temp files
    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as input_temp:
        for chunk in pdf_file.chunks():
            input_temp.write(chunk)
        input_path = input_temp.name
    
    output_path = tempfile.mktemp(suffix='.pdf')
    
    try:
        gs_command = [
            'gs', '-sDEVICE=pdfwrite', '-dCompatibilityLevel=1.4',
            f'-dPDFSETTINGS={quality}', '-dNOPAUSE', '-dQUIET', '-dBATCH',
            '-dCompressFonts=true', '-dCompressPages=true',
            f'-sOutputFile={output_path}', input_path
        ]
        
        subprocess.run(gs_command, check=True, timeout=60, capture_output=True)
        
        with open(output_path, 'rb') as f:
            buffer = io.BytesIO(f.read())
        
        return buffer
    finally:
        try:
            os.unlink(input_path)
            if os.path.exists(output_path):
                os.unlink(output_path)
        except:
            pass


def _compress_pikepdf(pdf_file, compression_level):
    """pikepdf compression - 40-60% reduction"""
    import pikepdf
    
    pdf_file.seek(0)
    
    with pikepdf.open(pdf_file) as pdf:
        buffer = io.BytesIO()
        
        if compression_level == 'high':
            pdf.save(
                buffer,
                compress_streams=True,
                stream_decode_level=pikepdf.StreamDecodeLevel.generalized,
                object_stream_mode=pikepdf.ObjectStreamMode.generate,
                normalize_content=True,
                recompress_flate=True
            )
        elif compression_level == 'medium':
            pdf.save(
                buffer,
                compress_streams=True,
                stream_decode_level=pikepdf.StreamDecodeLevel.generalized,
                object_stream_mode=pikepdf.ObjectStreamMode.generate,
                recompress_flate=True
            )
        else:
            pdf.save(buffer, compress_streams=True, recompress_flate=True)
        
        return buffer


def _compress_pypdf2(pdf_file, compression_level):
    """PyPDF2 compression - 20-30% reduction"""
    pdf_file.seek(0)
    
    pdf_reader = PdfReader(pdf_file)
    pdf_writer = PdfWriter()
    
    for page in pdf_reader.pages:
        page.compress_content_streams()
        pdf_writer.add_page(page)
    
    if compression_level in ['medium', 'high']:
        pdf_writer.compress_identical_objects()
    
    buffer = io.BytesIO()
    pdf_writer.write(buffer)
    
    return buffer


# ============================================
# REQUIREMENTS.TXT
# ============================================
"""
Django>=4.0.0
PyPDF2>=3.0.0
pikepdf>=8.0.0

# Optional but RECOMMENDED:
# Install Ghostscript for best compression
# Ubuntu/Debian: sudo apt-get install ghostscript
# macOS: brew install ghostscript
"""


# ============================================
# URLS.PY
# ============================================
"""
from django.urls import path
from . import views

urlpatterns = [
    path('compress/', views.compress_pdf, name='compress_pdf'),
]
"""


# ============================================
# SETTINGS.PY (Add these)
# ============================================
"""
# Logging configuration
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'INFO',
        },
    },
}

# File upload settings
DATA_UPLOAD_MAX_MEMORY_SIZE = 52428800  # 50MB
FILE_UPLOAD_MAX_MEMORY_SIZE = 52428800  # 50MB
"""

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
    if request.method == 'POST':
        pdf_file = request.FILES['pdf']
        start_page = int(request.POST['start'])
        end_page = int(request.POST['end'])
        
        # PDF ni o'qish
        pdf_reader = PdfReader(pdf_file)
        pdf_writer = PdfWriter()
        total_pages = len(pdf_reader.pages)
        
        # Backend validation
        if start_page > total_pages:
            return JsonResponse({
                'error': f'Start page ({start_page}) does not exist. PDF has only {total_pages} pages.'
            }, status=400)
        
        if end_page > total_pages:
            return JsonResponse({
                'error': f'End page ({end_page}) does not exist. PDF has only {total_pages} pages.'
            }, status=400)
        
        if start_page > end_page:
            return JsonResponse({
                'error': 'Start page must be less than or equal to end page.'
            }, status=400)
        # Sahifalarni extract qilish (pages are 0-indexed)
        for page_num in range(start_page - 1, end_page):
            if page_num < len(pdf_reader.pages):
                pdf_writer.add_page(pdf_reader.pages[page_num])
        
        # Buffer'ga yozish
        buffer = io.BytesIO()
        pdf_writer.write(buffer)
        buffer.seek(0)
        
        # File response qaytarish
        response = FileResponse(
            buffer,
            as_attachment=True,
            filename=f'split_pages_{start_page}-{end_page}.pdf'
        )
        response['Content-Type'] = 'application/pdf'
        return response
    
    return render(request, 'split.html')

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

    
