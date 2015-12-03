import sys
def arrc(imei_14):
    def digits_of(n):
            return [int(d) for d in str(n)]
    digits = digits_of(imei_14)
    i=digits.__len__()
    return digits
def gen(data):
    sun=0
    for i in range(data.__len__()):
        if(i%2==0):  #diyige
            sun += data[i]
        elif(i%2==1):
            sun+= (data[i]/10)+(data[i]%10)
    return str(sun%10)




print "canshu", sys.argv[0]

for i in range(1, len(sys.argv)):

    print "canshu", i, sys.argv[i]

f = open("./imei.txt", 'a')
while 1:
     imei = raw_input('Please enter 14 characters : ')
     if (imei.__len__() == 14):
         break
print >> f, imei+gen(arrc(imei))
print(imei+gen(arrc(imei)))
f.close()
print("test")

