price = int(input('Enter price: '))
discount = int(input('Enter discount %: '))
price_final = float(price - (price * discount // 100))
print('price with discount: ', price_final)
