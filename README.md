#UZ
# PDFTools - Modern PDF Utility Website

Modern va professional PDF ishlov berish veb-sayti. Bu loyiha ilovepdf.com kabi mashhur PDF xizmatlarining dizayni va funksionalligini takrorlaydi.

## ✨ Xususiyatlari

### 🎨 Dizayn va UI/UX
- **Zamonaviy va responsive dizayn** - barcha qurilmalarda mukammal ishlaydi
- **Intuitive interfeys** - foydalanuvchi uchun oson va tushunarli
- **Smooth animatsiyalar** - hover effektlari va o'tish animatsiyalari
- **Professional rang palitrasi** - qizil va kulrang ranglar asosida

### 📱 Responsive Navigatsiya
- **Desktop versiya**: Logo, menyu linklari, harakatlar tugmalari
- **Mobile versiya**: Hamburger menu bilan
- **Sticky navigation** - sahifani aylantirganda yuqorida qoladi

### 🎯 Hero Seksiyasi
- **Chap tomon**: Asosiy sarlavha, tavsif va CTA tugmalar
- **O'ng tomon**: PDF hujjatlarining 3D vizual ko'rinishi
- **Upload tugmalar**: Fayllarni tanlash va cloud xizmatlardan yuklash

### 📤 Fayl Yuklash Funksiyasi
- **Drag & Drop** - fayllarni sudrab tashlash
- **Ko'p faylni tanlash** - bir vaqtda bir nechta PDF
- **Fayl ro'yxati** - yuklangan fayllar haqida to'liq ma'lumot
- **Progress bar** - jarayon holatini ko'rsatish
- **Fayl boshqaruvi** - o'chirish va qayta nomlash

### 🛠️ PDF Vositalari Grid
- **9 ta turli vosita** - Merge, Split, Compress va boshqalar
- **Responsive grid** - turli ekran o'lchamlari uchun moslashadi
- **Hover effektlari** - interaktiv dizayn elementlari

### 📋 Footer
- **4 ta bo'lim** - vositalar, konvertatsiya, kompaniya, yordam
- **Til tanlash** - 5 ta tilni qo'llab-quvvatlaydi
- **Copyright ma'lumotlari** va ijtimoiy havolalar

## 🚀 O'rnatish va Ishga Tushirish

### Oddiy usul
1. `index.html` faylini kompyuteringizga saqlang
2. Faylni brauzerda oching
3. Tayyor! Sayt ishlay boshlaydi

### Veb-server orqali
```bash
# Python bilan (Python 3.x)
python -m http.server 8000

# Node.js bilan (agar live-server o'rnatilgan bo'lsa)
npx live-server

# PHP bilan
php -S localhost:8000
```

Keyin brauzerda `http://localhost:8000` ga o'ting.

## 💻 Texnologiyalar

- **HTML5** - zamonaviy semantic markup
- **CSS3** - Grid, Flexbox, animatsiyalar
- **Vanilla JavaScript** - kutubxonalarsiz toza JS
- **Font Awesome** - ikonlar uchun
- **Google Fonts** - zamonaviy fontlar

## 📁 Fayl Strukturasi

```
pdf-utility-site/
│
├── index.html          # Asosiy HTML fayl
├── README.md           # Bu fayl
└── assets/             # (ixtiyoriy)
    ├── css/
    ├── js/
    └── images/
```

## ⚙️ Konfiguratsiya

### Ranglarni o'zgartirish
CSS faylida quyidagi o'zgaruvchilarni topib o'zgartiring:
```css
:root {
  --primary-color: #e53e3e;    /* Asosiy rang */
  --secondary-color: #c53030;   /* Ikkinchi rang */
  --background-color: #f8fafc;  /* Fon rangi */
}
```

### Logoni o'zgartirish
HTML faylida `.logo` klassini toping:
```html
<a href="#" class="logo">SizningLogo</a>
```

### Til qo'shish
Footer qismida til selektorga yangi til qo'shing:
```html
<select class="language-selector">
    <option>O'zbekcha</option>
    <option>English</option>
    <!-- ... -->
</select>
```

## 🔧 Funksiyalar Tafsiloti

### Fayl Yuklash
- Faqat PDF fayllarni qabul qiladi
- Fayl o'lchamini ko'rsatadi (KB, MB formatida)
- Har bir fayl uchun alohida harakatlar (o'chirish, qayta nomlash)

### Progress Bar
- JavaScript orqali simulyatsiya qilinadi
- Real vaqtda progress ko'rsatiladi
- Tugagach muvaffaqiyat xabari chiqadi

### Responsive Dizayn
- **Desktop**: 1200px+ (to'liq interfeys)
- **Tablet**: 768px-1199px (moslashtirilgan)
- **Mobile**: 480px-767px (hamburger menu)
- **Small Mobile**: <480px (minimal interfeys)

## 🎨 Dizayn Prinsipalari

1. **Minimalizm** - keraksiz elementlarsiz
2. **Accessibility** - hamma uchun qulay
3. **Performance** - tez yuklanish
4. **User Experience** - foydalanuvchi tajribasi birinchi o'rinda

## 🐛 Ma'lum Muammolar va Yechimlar

### Fayl yuklash ishlamayapti?
- Brauzer konsolini tekshiring
- Faqat PDF fayllar qabul qilinadi
- Fayl o'lchami chegarasini tekshiring

### Mobile da dizayn buzilgan?
- Viewport meta tegini tekshiring
- CSS media query-larini qayta ko'rib chiqing

### JavaScript xatolari?
- Barcha script teglari to'g'ri yozilganini tekshiring
- Console.log orqali debug qiling

## 📞 Yordam va Qo'llab-quvvatlash

Savollar yoki takliflar bo'lsa:
- GitHub Issues orqali muammo bildiring
- Email: asilbekdavid@example.com
- Telegram: @Asilbek_B

## 📄 Litsenziya

MIT License - bepul foydalaning va o'zgartiring.

## 🔄 Yangilanishlar

### v1.0.0 (2024-09-27)
- ✅ Asosiy dizayn va layout
- ✅ Fayl yuklash funksiyasi
- ✅ Responsive dizayn
- ✅ Progress bar simulyatsiyasi
- ✅ Vositalar grid
- ✅ Footer va navigatsiya

### Rejadagi yangilanishlar
- 🔄 Haqiqiy fayl ishlov berish backend
- 🔄 Foydalanuvchi hisobi tizimi
- 🔄 Ko'proq PDF vositalari
- 🔄 Til tarjimalari
- 🔄 Dark mode qo'llab-quvvatlash

---

**Eslatma**: Bu demo versiya bo'lib, haqiqiy PDF ishlov berish backend talab qiladi. Hozirgi versiyada faqat frontend qismi mavjud.

#ENG 
# PDFTools - Modern PDF Utility Website

Modern and professional PDF processing website. This project replicates the design and functionality of popular PDF services like ilovepdf.com.

## ✨ Features

### 🎨 Design & UI/UX
- **Modern responsive design** - works perfectly on all devices
- **Intuitive interface** - easy and clear for users
- **Smooth animations** - hover effects and transition animations
- **Professional color palette** - based on red and gray colors

### 📱 Responsive Navigation
- **Desktop version**: Logo, menu links, action buttons
- **Mobile version**: With hamburger menu
- **Sticky navigation** - stays at top when scrolling

### 🎯 Hero Section
- **Left side**: Main headline, description and CTA buttons
- **Right side**: 3D visual representation of PDF documents
- **Upload buttons**: File selection and cloud service uploads

### 📤 File Upload Functionality
- **Drag & Drop** - drag and drop files
- **Multiple file selection** - several PDFs at once
- **File list** - complete information about uploaded files
- **Progress bar** - shows process status
- **File management** - delete and rename options

### 🛠️ PDF Tools Grid
- **9 different tools** - Merge, Split, Compress and others
- **Responsive grid** - adapts to different screen sizes
- **Hover effects** - interactive design elements

### 📋 Footer
- **4 sections** - tools, conversion, company, support
- **Language selection** - supports 5 languages
- **Copyright information** and social links

## 🚀 Installation and Setup

### Simple Method
1. Save the `index.html` file to your computer
2. Open the file in your browser
3. Done! The website will start working

### Via Web Server
```bash
# With Python (Python 3.x)
python -m http.server 8000

# With Node.js (if live-server is installed)
npx live-server

# With PHP
php -S localhost:8000
```

Then go to `http://localhost:8000` in your browser.

## 💻 Technologies

- **HTML5** - modern semantic markup
- **CSS3** - Grid, Flexbox, animations
- **Vanilla JavaScript** - pure JS without libraries
- **Font Awesome** - for icons
- **Google Fonts** - modern typography

## 📁 File Structure

```
pdf-utility-site/
│
├── index.html          # Main HTML file
├── README.md           # This file
└── assets/             # (optional)
    ├── css/
    ├── js/
    └── images/
```

## ⚙️ Configuration

### Changing Colors
Find and modify these variables in the CSS file:
```css
:root {
  --primary-color: #e53e3e;    /* Primary color */
  --secondary-color: #c53030;   /* Secondary color */
  --background-color: #f8fafc;  /* Background color */
}
```

### Changing Logo
Find the `.logo` class in the HTML file:
```html
<a href="#" class="logo">YourLogo</a>
```

### Adding Languages
Add new language to the language selector in footer:
```html
<select class="language-selector">
    <option>English</option>
    <option>Español</option>
    <!-- ... -->
</select>
```

## 🔧 Feature Details

### File Upload
- Only accepts PDF files
- Shows file size (in KB, MB format)
- Individual actions for each file (delete, rename)

### Progress Bar
- Simulated through JavaScript
- Shows real-time progress
- Success message appears when completed

### Responsive Design
- **Desktop**: 1200px+ (full interface)
- **Tablet**: 768px-1199px (adapted)
- **Mobile**: 480px-767px (hamburger menu)
- **Small Mobile**: <480px (minimal interface)

## 🎨 Design Principles

1. **Minimalism** - clean without unnecessary elements
2. **Accessibility** - comfortable for everyone
3. **Performance** - fast loading
4. **User Experience** - user experience first

## 🐛 Known Issues and Solutions

### File upload not working?
- Check browser console
- Only PDF files are accepted
- Check file size limits

### Design broken on mobile?
- Check viewport meta tag
- Review CSS media queries

### JavaScript errors?
- Check all script tags are correctly written
- Debug using console.log

## 📞 Help and Support

For questions or suggestions:
- Report issues via GitHub Issues
- Email: your-asilbekdavid@example.com
- Telegram: @Asilbek_B

## 📄 License

MIT License - use and modify freely.

## 🔄 Updates

### v1.0.0 (2024-09-27)
- ✅ Basic design and layout
- ✅ File upload functionality
- ✅ Responsive design
- ✅ Progress bar simulation
- ✅ Tools grid
- ✅ Footer and navigation

### Planned Updates
- 🔄 Real file processing backend
- 🔄 User account system
- 🔄 More PDF tools
- 🔄 Language translations
- 🔄 Dark mode support

---

**Note**: This is a demo version and requires a real PDF processing backend. The current version only includes the frontend part.
