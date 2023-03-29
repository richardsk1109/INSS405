temperature=input('Enter Temperature:')
if(float(temperature)>=50):
    print('Hot')
elif    (float(temperature)>=30 and float (temperature)<50):
    print('Warm')
elif    (float(temperature)>=0 and float (temperature)<30):
    print('Cold')
elif    (float(temperature)>=-20 and float (temperature)<30):
    print('Extreme chill cold,shelter in place')
else:
    print('Extreme cold')



