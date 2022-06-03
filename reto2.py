medic1=int(input())
medic2=int(input())
med1pac = 0
med2pac = 0
contPaci=0
while medic1 > 0 and medic2 > 0:
    contPaci += 1
    sist=int(input())
    diast=int(input())
    if sist < 72 and diast < 65:
        medic2 = medic2 - 4
        med2pac += 1
    elif (124 <= sist < 138) and (81 <= diast < 93):
        medic1 = medic1 - 2
        med1pac += 1
    elif (138 <= sist < 156) and (93 <= diast < 102):
        medic1 = medic1 - 4
        med1pac += 1
    elif (156 <= sist < 175) and (102 <= diast < 114):
        medic1 = medic1 - 8
        med1pac += 1
    elif (175 <= sist) and (114 <= diast):
        medic1 = medic1 - 16
        med1pac += 1
    elif (136 <= sist) and (92 > diast):
        medic1 = medic1 - 12
        med1pac += 1
if contPaci > 0:
    porc1 = (med1pac/contPaci)*100
    porc2 = (med2pac/contPaci)*100
else:
    porc1 = 0.00
    porc2 = 0.00
print(contPaci)
print(med1pac, "{:.2f}%".format(porc1))
print(med2pac, "{:.2f}%".format(porc2))