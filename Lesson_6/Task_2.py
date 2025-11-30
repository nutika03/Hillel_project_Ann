seconds = int(input("Enter seconds: "))
days = seconds // 86400
seconds %= 86400
hours = seconds // 3600
seconds %= 3600
minutes = seconds // 60
seconds %= 60
seconds_form = str(seconds).zfill(2)
minutes_form = str(minutes).zfill(2)
hours_form = str(hours).zfill(2)
# день - остання цифра 1 (але не 11)
# дні - остання цифра 2,3,4 (але не 11-14)
# днів - всі інші
if days % 10 == 1 and days % 100 != 11:
    day_word = "день"
elif 2 <= days % 10 <= 4 and not (11 <= days % 100 <= 14):
    day_word = "дні"
else:
    day_word = "днів"
result = f"{days} {day_word}, {hours_form}:{minutes_form}:{seconds_form}"
print(result)
