# frontend/forms.py
from django import forms


class MultiFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True 
    
class PDFUploadForm(forms.Form):
    pdf_file = forms.FileField(
        label="Upload PDF",
        widget=forms.ClearableFileInput(attrs={"accept": "application/pdf"})
    )
    


# frontend/forms.py
class PDFMergeForm(forms.Form):
    print("PDFMergeForm",'++++++++++++++')
    pdf_files = forms.FileField(
        widget=MultiFileInput(attrs={
            "id": "fileInput",             # sening HTML’dagi input bilan mos
            "class": "file-input",         # CSS class
            "multiple": True,              # bir nechta fayl
            "accept": ".pdf"               # faqat PDF
        }),
        required=True
    )
    print(pdf_files)