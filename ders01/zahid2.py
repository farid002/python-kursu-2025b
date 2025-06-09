"""
İstifadəçidən r radiusu oxumaqla başlayan proqram yazın.
Proqramınız radiusu r olan
    - dairənin sahəsini (πr^2)
    - kürənin həcmini (4/3 πr^3) hesablasın, tapılan dəyəri və həcm dəyişkənin data tipini terminalda göstərsin.


Hesablamalarınızda pi-ni sabit kimi tanımlayın və dəyərini 3.14 olaraq verin.
Çalışın kodunuzu kommentlərlə izah edin - çox qısa şəkildə.
"""
r = input("Radiusu daxil edin")
PI = 3.14
print(str((float(r)**2) * PI) + "dairenin sahesi")
print(str(4/3 * (float(r)**3) * PI) + " kurenin hecmi")

