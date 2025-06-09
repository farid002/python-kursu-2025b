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
gun=input("gun")
saat=input("saat")
deq=input("deq")
saniye=input("saniye")
print(
    str(
    int(gun)*24*60*60 + 
    int(saat)*60*60 +
    int(deq)*60 +
    int(saniye) )
    + " cemi saniye"
      )
#cox sagolun run elemirem sehflik cixmasin xeta varsa gormurem indi
#problem yoxdur, indi duzelt run elemesen de olar
# printin daxilinde "Cəmi saniyə" sozunu elave edersen