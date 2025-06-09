"""
İstifadəçidən müddəti gün, saat, dəqiqə və saniyə kimi oxuyan skript yazın.
Bu müddətlə bərabər olan ümumi saniyə sayını hesablayın və terminalda göstərin.
"""

"""
Məs.:
Gün daxil edin: 2
Saat daxil edin: 12
Dəqiqə daxil edin: 5
Saniyə daxil edin: 30

Cəmi saniyə: 216330
"""

day = int(input("Enter day:"))
hour = int(input("Enter hour:"))
minute = int(input("Enter minute:"))
second = int(input("Enter second:"))

SECOND = 1
MINUTE = 60
HOUR = 3600
DAY = 86400

sum = ((DAY * day)+(HOUR * hour)+(MINUTE * minute)+second)
print(sum)