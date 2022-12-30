while True:
    wt = float(input('Enter you weight (in Kg) : '))
    ht = float(input('Enter you weight (in cm/m/feet) : '))
    if (300>ht>100):
        ht = ht/100
    elif(3.28084<ht<9.84252):
        ht = ht*30.48
    else:
        ht = ht
    bmi = wt/(ht**2)
    print("Your bmi is ", bmi)
    if bmi<18:
        print('Your bmi is too low!')
    elif 18<=bmi<=25:
        print("What's up! fit person")
    else
        print("Please start excercising")
