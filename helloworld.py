a = 2
b = 5
print(a + b)
xx = "LHQ"
print(xx[0])

c = 11.22356
print(f"{c:.2f}")

e = "Hello"
d = "ok"
print(d and e)
order_count = 5
orderID = str(order_count).rjust(8,"0")
print(orderID)

symbols = ['IF2009', "IF2010", "IF2012", "IF2103"]
print(symbols)
print(symbols[0])
print(symbols[3])
print(symbols[-1])  #get last data, the same as above, 从后面往前数

for s in symbols:
    print(s)

symbols.append("IH2089")
print(symbols)

ih_symbols = list()
print(ih_symbols)
ih_symbols.append("IF2099")
print(ih_symbols)

for i in range(0, len(symbols)):
    print(i, symbols[i], "ok", "good")