"Aşağıdakı NumPy arrayindeki bütün mənfi ədədləri sıfıra çevir."
import numpy as np
a = np.array([3, -1, 5, -7, 0, 2])

"TAPŞIRIQ 1 - Tutaq ki, bizdə bir şəhərdə gündəlik temperatur ölçmələri var (santigrad dərəcə ilə):"
import numpy as np
temps = np.array([14.5, 17.2, -3.0, 0.0, 5.6, 12.1, -7.8, 21.4])

"""
Əgər temperatur 0-dan aşağıdırsa, həmin dəyəri np.nan (not a number) ilə əvəz et,
Qalan dəyərləri olduğu kimi saxla.
np.nan dəyərləri nəzərə almadan bu array üçün orta temperaturu hesabla.

np.where() ilə şərti əvəz etmə apar.
np.nanmean() funksiyası nan olan dəyərləri saymadan orta dəyəri qaytarır.
"""




"TAPŞIRIQ 2 - Bir neçə tələbənin imtahan nəticələri belədir:"
grades = np.array([35, 87, 59, 100, 49, 76, 62])

"""
Əgər qiymət:
60 və ya yuxarıdırsa: “✅ Keçdi”
əks halda: “❌ Kəsildi”
bu məlumatları ayrı bir arrayde simvol kimi saxla: result = np.where(grades >= 60, "✅ Keçdi", "❌ Kəsildi")
Daha sonra, neçə nəfər keçib, neçə nəfər kəsilib — bunları say və çap et.

np.count_nonzero(result == "✅ Keçdi") ilə keçənləri saya bilərsən.
"""


