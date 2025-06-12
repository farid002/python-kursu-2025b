"""
İstifadəçidən cümlə alın (məsələn: "Python proqramlaşdırma dili çox maraqlıdır").
String metodları və əməliyyatları istifadə edərək:

- Cümlədə neçə dəfə "a" hərfi keçdiyini count() ilə tapın və çap edin.
- Cümlədə "çox" sözünün başlanğıc indeksini find() ilə tapın və çap edin.
- Cümlədə "maraqlıdır" sözünü "çox faydalıdır" ilə replace() vasitəsilə əvəz edin və yeni cümləni çap edin.
"""
cumle="bu gun heftenin 4 cu gunudur"
print(f"e lerin sayi: {cumle.count("e")}")
print(f"gun sozunun baslangic indeksi: {cumle.find("gun")}")
print(f"deyismek: {cumle.replace("4","5")}")

