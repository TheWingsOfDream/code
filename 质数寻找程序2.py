def check(a):
    checknumber=2
    while checknumber<=a**0.5:
        i=a%checknumber
        if i==0 :
            return 1
        else :
            checknumber=(checknumber+1)
            continue
    return 0
print('输入寻找开始值')
start=int(input())
print('输入寻找终止值')
stopnumber=int(input())
x=start 
counter=0
while x<=stopnumber:
    y=int(check(x))
    if y==1:
        x=(x+1)
        continue
    else:
        print(x)
        counter=counter+1
        x=(x+1)
        continue
print('寻找结束')
print('个数'+str(counter))
