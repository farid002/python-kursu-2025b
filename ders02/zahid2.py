"""
İstifadəçidən cümlə alın (məsələn: "Python proqramlaşdırma dili çox maraqlıdır").
String metodları və əməliyyatları istifadə edərək:

- Cümlədə neçə dəfə "a" hərfi keçdiyini count() ilə tapın və çap edin.
- Cümlədə "çox" sözünün başlanğıc indeksini find() ilə tapın və çap edin.
- Cümlədə "maraqlıdır" sözünü "çox faydalıdır" ilə replace() vasitəsilə əvəz edin və yeni cümləni çap edin.
"""
istifadecinin_cumlesi=input("Cumle yazin.\n Meselen(Python proqramlaşdırma dili cox maraqlıdır)")
print(
      f"Cumlede 'a' herfi {istifadecinin_cumlesi.count("a")} qeder islenib.\n"
      f"Cumlede cox sozu{istifadecinin_cumlesi.find("cox")}\n"
      f"{istifadecinin_cumlesi.replace("maraqlidir","cox faydalidir")}\n"
      )
