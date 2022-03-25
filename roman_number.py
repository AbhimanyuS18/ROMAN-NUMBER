
r = { 1:'I',4:'IV', 5:'V', 9:'IX', 10:'X', 40:'XL', 50:'L', 90:'XC', 100:'C', 400:'CD', 500:'D', 900:'CM', 1000:'M', 4000:'MV̅', 5000:'V̅', 9000:'MX̅', 10000:'X̅', 40000:'X̅L̅', 50000:'L̅', 90000:'X̅C̅', 100000:'C̅' }

v = [ 100000,90000,50000,40000,10000,9000,5000,4000,1000,900,500,400,100,90,50,40,10,9,5,4,1 ]

f = ''

usr = int(input('Enter number: '))

for i in v:
    if usr!=0 and usr<=300000:
        c=usr//i
        if c!=0:
            for j in range(c):
                f+=r[i]
        usr%=i
else:
    print('This programme only works for 3 Lakhs Numbers')
print(f)