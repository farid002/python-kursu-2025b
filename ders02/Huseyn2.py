"""
İstifadəçidən cümlə alın (məsələn: "Python proqramlaşdırma dili çox maraqlıdır").
String metodları və əməliyyatları istifadə edərək:

- Cümlədə neçə dəfə "a" hərfi keçdiyini count() ilə tapın və çap edin.
- Cümlədə "çox" sözünün başlanğıc indeksini find() ilə tapın və çap edin.
- Cümlədə "maraqlıdır" sözünü "çox faydalıdır" ilə replace() vasitəsilə əvəz edin və yeni cümləni çap edin.
"""
cumle= input("Cumle yazin: ")

print(cumle.count("a"))
print(cumle.find("çox"))
print(cumle.replace("maraqlıdır", "çox maraqlıdır"))