"""
İstifadəçidən sadəcə adını alın. String metodları, əməliyyatları edərək:

1- Adının ilk hərfini böyük hərf edin, capitalize() funksiyası ilə. Alınan dəyəri eyni dəyişkəndə tutun.
2. Adının ilk 2 hərfini çap edin
3. Adının son hərfini çap edin
"""
user_name=input("Adiniz")


# 1-ci
user_name = user_name.capitalize()
# 2-ci
print(f"Adinizin ilk iki herfi: {user_name[0:2]}")
# 3-cu
print(f"Adinizin son herfi: {user_name[-1]}")