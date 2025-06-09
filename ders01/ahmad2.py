"""
İstifadəçidən r radiusu oxumaqla başlayan proqram yazın.
Proqramınız radiusu r olan
    - dairənin sahəsini (πr^2)
    - kürənin həcmini (4/3 πr^3) hesablasın, tapılan dəyəri və həcm dəyişkənin data tipini terminalda göstərsin.


Hesablamalarınızda pi-ni sabit kimi tanımlayın və dəyərini 3.14 olaraq verin.
Çalışın kodunuzu kommentlərlə izah edin - çox qısa şəkildə.
"""

radius_of_circle = float(input("Enter radius of circle:"))
radius_of_globe = float(input("Enter radius of globe:"))

PI = 3.14

area_of_circle = (PI * (radius_of_circle ** 2))
volume_of_globe = ((4/3) * PI * (radius_of_globe ** 3))

print("Area of circle:" + str(area_of_circle))
print("Volume of globe:" + str(volume_of_globe))