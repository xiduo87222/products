products = []
while True:
    name = input('請輸入商品名稱: ')
    if name == 'q':
        break
    price = input('請輸入商品價格: ')
    products.append([name, price])  #建立二維清單中的小清單
print(products)

for p in products:
    print(p)
for p in products:
    print(p[0]) #印出每個小清單的第0項
for p in products:
    print(p[0], '的價格是', p[1])