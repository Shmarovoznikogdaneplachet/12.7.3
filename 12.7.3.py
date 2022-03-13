print("ТКБ 5,6%, СКБ 5,9%, ВТБ 4,28%, СБЕР 4,0%")
money = int(input ("Введите сумму вклада:"))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = [round(money*0.056, 2), round(money*0.059, 2), round(money*0.0428, 2), round(money*0.04, 2)]
print(deposit)

max_number = max(deposit)
print("Максимальная сумма которую вы можете заработать:", max_number)




