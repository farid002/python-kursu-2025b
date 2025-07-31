# Pandas Əsasları - Tam Skript (Azərbaycan dilində şərhlərlə)

# 1. Pandas kitabxanasının qurulması (yalnız bir dəfə lazımdır)
# pip install pandas

# 2. Pandas-ı import edirik
import pandas as pd

# 3. Series yaradılması
print("=== Series ===")
s = pd.Series([10, 20, 30, 40, 40, 40, 41])
print(s)
print()

# 4. DataFrame yaradılması
print("=== DataFrame ===")
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Paris', 'London']
}
df = pd.DataFrame(data)
print(df)
print()

# 5. Verilərə baxış
print("=== Head və Tail ===")
print(df.head(2))  # İlk 5 sətr
print(df.tail(1))  # Son 5 sətr
print()

# 6. DataFrame haqqında məlumat
print("=== Info və Təsvir ===")
print(df.info())
print(df.describe())
print()

# 7. Sütunlara giriş
print("=== Sütuna giriş ===")
print(df['Age'][2])
print()

# 8. Sətrlərə giriş
print("=== Sətirə giriş (loc ilə) ===")
print(df.loc[1])  # Sətri etiketlə əldə edirik
print()

print("=== Sətirə giriş (iloc ilə) ===")
print(df.iloc[1])  # Sətri indekslə əldə edirik
print()

# 9. Verilərin filtrdən keçirilməsi
print("=== Filtrləmə ===")
print(df[df['Age'] > 28])
print()

# 10. Yeni sütun əlavə etmək
print("=== Yeni Sütun Əlavə Etmək ===")
df['Country'] = ['USA', 'France', 'UK']
print(df)
print()

# 11. Dəyərləri yeniləmək
print("=== Dəyərləri Yeniləmək ===")
df.at[1, 'Age'] = 31
print(df)
print()

# 12. Sütun silmək
print("=== Sütun Silmək ===")
df = df.drop(columns=['City'])
print(df)
print()

# 13. Sütun adlarını dəyişmək
print("=== Sütun Adlarını Dəyişmək ===")
df = df.rename(columns={'Name': 'Full Name'})
print(df)
print()

# 14. Sıralama
print("=== Yaşa görə sıralamaq ===")
print(df.sort_values(by='Age'))
print()

# 15. Çatışmayan məlumatların idarə edilməsi
print("=== Çatışmayan Məlumatlar ===")
# Çatışmayan məlumat əlavə edirik
df.loc[2] = [None, 45, None]
print(df)

print("\nÇatışmayan dəyərləri tapmaq:")
print(df.isnull())

print("\nÇatışmayan dəyərləri doldurmaq:")
print(df.fillna('Bosh info'))

print("\nÇatışmayan dəyərləri silmək:")
print(df.dropna())
print()

# 16. Fayl oxuma və yazma
# Qeyd: Demo zamanı real fayl yoxdursa, sadəcə kodu göstər
print("=== Fayl Oxuma və Yazma (nümunə kod) ===")
# Fayl oxuma
# df = pd.read_csv('fayl.csv')
# Fayl yazma
# df.to_csv('output.csv', index=False)

# 17. GroupBy və Agreqasiya
print("=== GroupBy Nümunəsi ===")
data2 = {
    'Category': ['A', 'A', 'B', 'B', 'B'],
    'Values': [10, 15, 10, 20, 30]
}
df2 = pd.DataFrame(data2)
print(df2)

print("\nKateqoriyaya görə cəmləmək:")
print(df2.groupby('Category').sum())
print()

# 18. Sadə Vizualizasiya (istəyə bağlı)
print("=== Çizim Nümunəsi (matplotlib lazımdır) ===")
# Lazımdırsa qur: pip install matplotlib
import matplotlib.pyplot as plt

df2.groupby('Category').sum().plot(kind='bar')
plt.title('Kateqoriya üzrə Cəmlər')
plt.show()