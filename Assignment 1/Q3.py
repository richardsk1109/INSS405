courses=12
sum=0.00
for x in range (courses):
    score=input('enter final score:')
    sum=sum+int(score)
average= sum/12
print('total sum=',sum)
print('Average=',average)
if (float(average)>90):
    print('A')
elif(float(average)>80):
    print("B")
elif(float(average)>=75 and float(average)<=79):
    print('C')
elif(float(average)>60):
    print('D')
elif(float(average)<59):
    print('F')


