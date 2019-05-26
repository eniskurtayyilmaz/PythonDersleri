import decimal
import math

# object references when called Identifier
degiskenAdi = "veri"

# five different objects
TAXRATE = "veri1"
Taxrate = "veri2"
TaxRate = "veri3"
taxRate = "veri4"
taxrate = "veri5"
print(TAXRATE)
print(Taxrate)
print(TaxRate)
print(taxRate)
print(taxrate)

# not allowed keywords example
# for, if etc.

# dir built-in function
print(dir(TAXRATE))

# using underscore
for _ in (0, 1, 2, 3, 4, 5):
    print("Hello")

# integers operators and functions.
sayi1 = 2
sayi2 = 3
print(sayi1 + sayi2)
print(sayi1 ** sayi2)
print(pow(sayi1, sayi2))

sayi1 = 10.49999
print(round(sayi1, 2))

# using abs
sayi1 = -10
print(abs(sayi1))

# integer conversion
deger = "0"  # input("Bir sayı gir: ")
print(type(deger))
sayi1 = int(deger)
print(type(sayi1))
print(sayi1 + sayi2)

# boolean
boolDegisken1 = True
boolDegisken2 = False

# 1 ve 0 = false
# 0 ve 1 = false
# 0 ve 0 = false
# 1 ve 1 = true
print(boolDegisken1 | boolDegisken2)

# using decimal
a = decimal.Decimal(9876)
b = decimal.Decimal("54321.012345678987654321")
c = a + b
print(c)

# using str
strDegisken = "selam ben Kurtay"
strDegisken = """selam ben "Kurtay" """
print(strDegisken)
# " veri "
# """ veri """
# ' veri '
print('veri')
print(''' 'veri' ''')

# backslash
strDegisken = "Selam Kurtay,\tnasılsın"
print(strDegisken)

t = "This is not the best way to join two long strings " + \
    "together since it relies on ugly newline escaping"
print(t)

# unicode example
unicodeExample = "\N{euro sign}10"
print(unicodeExample)

# slicing
strDegisken = "abcdefghıijklmno"
print(strDegisken[-5])
print(strDegisken[11])

strDegisken = "selam kurtay nasılsın"
print(strDegisken[6:13:2])

# string methods and operators.
strDegisken = "s"
for i in range(0, 10):
    strDegisken += str(i)
print(strDegisken)

# * property
print("selam " * 5)

treatises = ["Arithmetica", "Conics", "Elements"]
print(" ".join(treatises))

s = "=" * 5

print(s)

s *= 10
print(s)

# upper example
strDegisken = "kurtay"
print(strDegisken.upper())

# lower example
strDegisken = "KURTAY"
print(strDegisken.lower())

# format example
strDegisken = "selam {0} nasılsın".format("kurtay")
print(strDegisken)

strDegisken = "selam {name} nasılsın".format(name="kurtay")
print(strDegisken)

strDegisken = "selam {{name}} nasılsın".format(name="kurtay")
print(strDegisken)

strDegisken = "Language: {} Number: {} Type:{}".format("Python", "3", "5")
print(strDegisken)

# format spesific
strDegisken = "{0:^25}".format("kurtay") # minimum width 25
print(strDegisken)


