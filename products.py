import os #operating system

# 讀取檔案
products = []
if os.path.isfile('products.csv'): # 檢查檔案在不在
    print('找到檔案了')
    with open('products.csv', 'r', encoding = 'utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue
            name, price = line.strip().split(',') #刪去換行符號後做切割,存入name跟price清單
            products.append([name, price])  #建立二維清單中的小清單
    print(products)
else:
    print('找不到檔案')

# 讓使用者輸入
while True:
    name = input('請輸入商品名稱: ')
    if name == 'q':
        break
    price = input('請輸入商品價格: ')
    products.append([name, price])  #建立二維清單中的小清單
print(products)

# 印出所有購買紀錄
for p in products:
    print(p[0], '的價格是', p[1])
#for p in products:
    #print(p)
#for p in products:
    #print(p[0]) #印出每個小清單的第0項

# 寫入檔案
with open('products.csv', 'w', encoding = 'utf-8') as f: #如果已經有同名的檔案存在,會直接覆蓋掉，沒有則自動生成
    f.write('商品,價格\n') #在文件第一行產生商品及價格欄位
    for p in products:
        f.write(p[0] + ',' + p[1] + '\n' ) #用"+"做字串合併,csv檔以","做分隔