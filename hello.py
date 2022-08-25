day = int(input("введите день недели"))
if (day >= 6) and (day <= 7):
    print ('это выходной день')
elif (day >= 1) and (day <= 5):
    print ('это будний день')
else:
    print ('всего 7 дней в неделе')