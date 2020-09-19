products = []
while True:
    name = input('請輸入商品名稱: ')
    if name == 'q':
        break
    price = input('請輸入商品價格: ')
    products.append([name, price])  #建立二維清單中的小清單
print(products)

for p in products:
    print(p[0], '的價格是', p[1])
#for p in products:
    #print(p)
#for p in products:
    #print(p[0]) #印出每個小清單的第0項

with open('products.csv', 'w', encoding = 'utf-8') as f: #如果已經有同名的檔案存在,會直接覆蓋掉，沒有則自動生成
    f.write('商品,價格\n') #在文件第一行產生商品及價格欄位
    for p in products:
        f.write(p[0] + ',' + p[1] + '\n' ) #用"+"做字串合併,csv檔以","做分隔