#>90-A
#70-89-B
#60-69-C
#<59-F
score1=input ('Enter core for INS 405:')
score2=input ('Enter core for BUS 360:')
score3=input ('Enter core for DANL 407:')
sum=int(score1)+int(score2)+int(score3)
print(sum)
average=int(sum)/3
print(average)
if(average>90):
    print('A')
elif    (average>=70) and (average<89):
    print('B')
elif    (average>=60 and average<69):
    print('C')
elif    (average<59):
    print('D')
    