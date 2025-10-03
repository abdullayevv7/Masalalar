##Pythonda arifmetik operatorlar mavzusidan algoritmik masalalar
##I. Oddiy matematik masalalar
##1
# a = input("Sonni kiriting: ")
# b = input("Sonni kiriting: ")
# summa = a + b
#
# print(f"Yig'indi: {summa}")


##2
# l = int(input("Uchburchakning uzunligini kiriting: "))
# w = int(input("Uchburchakning enini kiriting: "))
# area = l * w
# print(f"Uchburchak yuzasi: {area}")


##3
# a = int(input("Birinchi sonni kiriting: "))
# b = int(input("Ikkinchi sonni kiriting: "))
# c = int(input("Uchinchi sonni kiriting: "))
# avarage = (a + b + c) / 2
# print(f"O'rta arifmetik: {avarage}")


##4
# a = int(input("Sonni kiriting: "))
# b = int(input("Sonni kiriting: "))
# perimetr = 2 * (a + b)
# print(f"To‘g‘ri to‘rtburchak perimetri: {perimetr}")


##5
# h = int(input("Soatni kiriting: "))
# m = int(input("Daqiqani kiriting: "))
# total_min = h * 60 + m
# print(f"Umumiy daqiqalar: {total_min}")


##6
# usd = int(input("USD miqdorini kiritng: "))
# sum = usd * 12000
# print(f"{sum}so'm")


##7
# a = int(input("Sonni kiriting: "))
# b = int(input("Sonni kiriting: "))
# diff = abs(a - b)
# print(f"Diff = {diff}")


##8
# x = int(input("X'ni kiriting: "))
# n = int(input("N'ni kiriting: "))
# power = x**n
# print(f"X'ning N - darajasi: {power}")


##9
# a = int(input("Sonni kiriting: "))
# b = int(input("Sonni kiriting: "))
# quotient = a // b
# print(f"Bo‘linma va qoldiq = {quotient}")


##10
# a = int(input("Sonni kiriting: "))
# b = int(input("Sonni kiriting: "))
# a, b = b, a
# print(f"A = {a}, B = {b}")


##II. Hayotiy muammolar
##1
# n = int(input("Sonni kiriting: ")) ## n - summani necha oyga bo'lib to'lash
# total_rent = int(input("Oylik ijara to'lovi: ")) ## total_rent - oylik ijara to'lovi
# per_month = total_rent / n
# print(f"Oylik to'lov: {per_month}")


##2
# d = int(input("Masofani kiriting (km): ")) ## d - masofa km da
# v = int(input("Tezlikni kiriting (km/soat): ")) ## v - tezlik km/soat da
# time = d / v
# print(f"Safar vaqti: {time} soat")


##3
# seats = int(input("Mavjud o'rindiqlar soni: "))
# passengers = int(input("Yo'lovchilar soni: "))
# per_person = seats // passengers
# left = seats % passengers
# print(f"Har bir yo'lovchiga {per_person} o'rindiq to'g'ri keladi, {left} o'rindiq band.")


##4
# consumption = int(input("Yoqilg'i sarfini kiriting (l/100km): ")) ## consumption - yoqilg'i sarfi l/100km da
# d = int(input("Masofani kiriting (km): ")) ## d - bosib o'tilgan masofa km da
# fuel = (consumption * d) / 100
# print(f"Yoqilg'i sarfi: {fuel} litr")


##5
# salary = int(input("Oylik maoshni kiriting: ")) ## salary - oylik maosh
# net = salary * (1 - 0.12)
# print(f"Sof maosh: {net}")