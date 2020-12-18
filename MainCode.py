import ast 
s="100000000000001"
i=0 
def DictUpdateFunction(e):
    with open('EncodedFile.txt','a') as f:
        f.write(s)
    with open('Dict.txt','r') as DictFileRead:
        EmptyDict=DictFileRead.read()
        dictionary= ast.literal_eval(EmptyDict)
        d[e]=d[e]+1
    with open('Dict.txt','w',encoding='utf-8') as DictFileWrite:
        DictFileWrite.write(str(d))                                
with open('InputText.txt','r') as f: #Opening Text file to read input
    data=f.readline()
    while data:
        #Inserting Code
        InputData=[]
        data=f.readline()





for e in InputData:#Encoding
    if e=='a':
        with open('3DigitCodes.txt','r') as DigitCodeReader:
            DigitCodeData=DigitCodeReader.readlines() 
        y=DigitCodeData[d[e]]   
        s="1{}000000000{}{}{}01".format(y[0],y[1],y[2])
        DictUpdateFunction(e)
    elif e=='b':
        with open('3DigitCodes.txt','r') as DigitCodeReader:
            DigitCodeData=DigitCodeReader.readlines() 
        y=DigitCodeData[d[e]]   
        s="1000000{}{}{}00001".format(y[0],y[1],y[2])
        DictUpdateFunction(e)
    elif e=='c':
        with open('3DigitCodes.txt','r') as DigitCodeReader:
            DigitCodeData=DigitCodeReader.readlines() 
        y=DigitCodeData[d[e]]   
        s="1000{}{}{}00000001".format(y[0],y[1],y[2])
        DictUpdateFunction(e)
    elif e=='d':
        with open('3DigitCodes.txt','r') as DigitCodeReader:
            DigitCodeData=DigitCodeReader.readlines() 
        y=DigitCodeData[d[e]]   
        s="1{}{}{}00000000001".format(y[0],y[1],y[2])
        DictUpdateFunction(e)
    elif e=='e':
        with open('3DigitCodes.txt','r') as DigitCodeReader:
            DigitCodeData=DigitCodeReader.readlines() 
        y=DigitCodeData[d[e]]
        s="100000{}000{}{}001".format(y[0],y[1],y[2])
        DictUpdateFunction(e)
    elif e=='f':
        with open('3DigitCodes.txt','r') as DigitCodeReader:
            DigitCodeData=DigitCodeReader.readlines() 
        y=DigitCodeData[d[e]] 
        s="10{}{}{}0000000001".format(y[0],y[1],y[2])
        DictUpdateFunction(e)
    elif e=='g':
        with open('3DigitCodes.txt','r') as DigitCodeReader:
            DigitCodeData=DigitCodeReader.readlines() 
        y=DigitCodeData[d[e]]   
        s="100{}{}{}000000001".format(y[0],y[1],y[2])
        DictUpdateFunction(e)
    elif e=='h':
        with open('3DigitCodes.txt','r') as DigitCodeReader:
            DigitCodeData=DigitCodeReader.readlines() 
        y=DigitCodeData[d[e]]   
        s="10000{}{}{}0000001".format(y[0],y[1],y[2])
        DictUpdateFunction(e)
    elif e=='i':
        with open('3DigitCodes.txt','r') as DigitCodeReader:
            DigitCodeData=DigitCodeReader.readlines() 
        y=DigitCodeData[d[e]]   
        s="100000{}{}{}000001".format(y[0],y[1],y[2])
        DictUpdateFunction(e)
    elif e=='j':
        with open('3DigitCodes.txt','r') as DigitCodeReader:
            DigitCodeData=DigitCodeReader.readlines() 
        y=DigitCodeData[d[e]]   
        s="10000000{}{}{}0001".format(y[0],y[1],y[2])
        DictUpdateFunction(e)
    elif e=='k':
        with open('3DigitCodes.txt','r') as DigitCodeReader:
            DigitCodeData=DigitCodeReader.readlines() 
        y=DigitCodeData[d[e]]   
        s="100000000{}{}{}001".format(y[0],y[1],y[2])
        DictUpdateFunction(e)
    elif e=='l':
        with open('3DigitCodes.txt','r') as DigitCodeReader:
            DigitCodeData=DigitCodeReader.readlines() 
        y=DigitCodeData[d[e]]   
        s="10000000000{}{}{}1".format(y[0],y[1],y[2])
        DictUpdateFunction(e)
    elif e=='m':
        with open('3DigitCodes.txt','r') as DigitCodeReader:
            DigitCodeData=DigitCodeReader.readlines() 
        y=DigitCodeData[d[e]]   
        s="1{}0{}0{}000000001".format(y[0],y[1],y[2])
        DictUpdateFunction(e)
    elif e=='n':
        with open('3DigitCodes.txt','r') as DigitCodeReader:
            DigitCodeData=DigitCodeReader.readlines() 
        y=DigitCodeData[d[e]]   
        s="10{}0{}0{}00000001".format(y[0],y[1],y[2])
        DictUpdateFunction(e)
    elif e=='o':
        with open('3DigitCodes.txt','r') as DigitCodeReader:
            DigitCodeData=DigitCodeReader.readlines() 
        y=DigitCodeData[d[e]]   
        s="100{}0{}0{}0000001".format(y[0],y[1],y[2])
        DictUpdateFunction(e)
    elif e=='p':
        with open('3DigitCodes.txt','r') as DigitCodeReader:
            DigitCodeData=DigitCodeReader.readlines() 
        y=DigitCodeData[d[e]]   
        s="1000{}0{}0{}000001".format(y[0],y[1],y[2])
        DictUpdateFunction(e)
    elif e=='q':
        with open('3DigitCodes.txt','r') as DigitCodeReader:
            DigitCodeData=DigitCodeReader.readlines() 
        y=DigitCodeData[d[e]]   
        s="10000{}0{}0{}00001".format(y[0],y[1],y[2])
        DictUpdateFunction(e)
    elif e=='r':
        with open('3DigitCodes.txt','r') as DigitCodeReader:
            DigitCodeData=DigitCodeReader.readlines() 
        y=DigitCodeData[d[e]]   
        s="100000{}0{}0{}0001".format(y[0],y[1],y[2])
        DictUpdateFunction(e)
    elif e=='s':
        with open('3DigitCodes.txt','r') as DigitCodeReader:
            DigitCodeData=DigitCodeReader.readlines() 
        y=DigitCodeData[d[e]]   
        s="1000000{}0{}0{}001".format(y[0],y[1],y[2])
        DictUpdateFunction(e)
    elif e=='t':
        with open('3DigitCodes.txt','r') as DigitCodeReader:
            DigitCodeData=DigitCodeReader.readlines() 
        y=DigitCodeData[d[e]]   
        s="10000000{}0{}0{}01".format(y[0],y[1],y[2])
        DictUpdateFunction(e)
    elif e=='u':
        with open('3DigitCodes.txt','r') as DigitCodeReader:
            DigitCodeData=DigitCodeReader.readlines() 
        y=DigitCodeData[d[e]]   
        s="100000000{}0{}0{}1".format(y[0],y[1],y[2])
        DictUpdateFunction(e)
    elif e=='v':
        with open('3DigitCodes.txt','r') as DigitCodeReader:
            DigitCodeData=DigitCodeReader.readlines() 
        y=DigitCodeData[d[e]]   
        s="1{}00{}{}000000001".format(y[0],y[1],y[2])
        DictUpdateFunction(e)
    elif e=='w':
        with open('3DigitCodes.txt','r') as DigitCodeReader:
            DigitCodeData=DigitCodeReader.readlines() 
        y=DigitCodeData[d[e]]   
        s="10{}00{}{}00000001".format(y[0],y[1],y[2])
        DictUpdateFunction(e)
    elif e=='x':
        with open('3DigitCodes.txt','r') as DigitCodeReader:
            DigitCodeData=DigitCodeReader.readlines() 
        y=DigitCodeData[d[e]]   
        s="100{}00{}{}0000001".format(y[0],y[1],y[2])
        DictUpdateFunction(e)
    elif e=='y':
        with open('3DigitCodes.txt','r') as DigitCodeReader:
            DigitCodeData=DigitCodeReader.readlines() 
        y=DigitCodeData[d[e]]   
        s="1000{}00{}{}000001".format(y[0],y[1],y[2])
        DictUpdateFunction(e)
    elif e=='z':
        with open('3DigitCodes.txt','r') as DigitCodeReader:
            DigitCodeData=DigitCodeReader.readlines() 
        y=DigitCodeData[d[e]]   
        s="10000{}00{}{}00001".format(y[0],y[1],y[2])
        DictUpdateFunction(e)  
    elif e=='!':
        with open('3DigitCodes.txt','r') as DigitCodeReader:
            DigitCodeData=DigitCodeReader.readlines() 
        y=DigitCodeData[d[e]]   
        s="10{}0{}{}000000001".format(y[0],y[1],y[2])
        DictUpdateFunction(e)     
    elif e=='@':
        with open('3DigitCodes.txt','r') as DigitCodeReader:
            DigitCodeData=DigitCodeReader.readlines() 
        y=DigitCodeData[d[e]]   
        s="1{}0{}{}0000000001".format(y[0],y[1],y[2])
        DictUpdateFunction(e)
    elif e=='#':
        with open('3DigitCodes.txt','r') as DigitCodeReader:
            DigitCodeData=DigitCodeReader.readlines() 
        y=DigitCodeData[d[e]]   
        s="10{}00{}0{}0000001".format(y[0],y[1],y[2])
        DictUpdateFunction(e)
    elif e=='$':
        with open('3DigitCodes.txt','r') as DigitCodeReader:
            DigitCodeData=DigitCodeReader.readlines() 
        y=DigitCodeData[d[e]]   
        s="100000{}{}00{}0001".format(y[0],y[1],y[2])
        DictUpdateFunction(e)
    elif e=='%':
        with open('3DigitCodes.txt','r') as DigitCodeReader:
            DigitCodeData=DigitCodeReader.readlines() 
        y=DigitCodeData[d[e]]   
        s="10000{}00{}0{}0001".format(y[0],y[1],y[2])
        DictUpdateFunction(e)
    elif e=='^':
        with open('3DigitCodes.txt','r') as DigitCodeReader:
            DigitCodeData=DigitCodeReader.readlines() 
        y=DigitCodeData[d[e]]   
        s="1000{}000{}{}00001".format(y[0],y[1],y[2])
        DictUpdateFunction(e)
    elif e=='&':
        with open('3DigitCodes.txt','r') as DigitCodeReader:
            DigitCodeData=DigitCodeReader.readlines() 
        y=DigitCodeData[d[e]]   
        s="10{}0000{}{}000001".format(y[0],y[1],y[2])
        DictUpdateFunction(e)       
    elif e=='*':
        with open('3DigitCodes.txt','r') as DigitCodeReader:
            DigitCodeData=DigitCodeReader.readlines() 
        y=DigitCodeData[d[e]]   
        s="1000000000{}{}0{}1".format(y[0],y[1],y[2])
        DictUpdateFunction(e)
    elif e=='(':
        with open('3DigitCodes.txt','r') as DigitCodeReader:
            DigitCodeData=DigitCodeReader.readlines() 
        y=DigitCodeData[d[e]]   
        s="100000{}{}{}000001".format(y[0],y[1],y[2])
        DictUpdateFunction(e)
    elif e==')':
        with open('3DigitCodes.txt','r') as DigitCodeReader:
            DigitCodeData=DigitCodeReader.readlines() 
        y=DigitCodeData[d[e]]   
        s="10000{}0{}{}000001".format(y[0],y[1],y[2])
        DictUpdateFunction(e)
    elif e=='_':
        with open('3DigitCodes.txt','r') as DigitCodeReader:
            DigitCodeData=DigitCodeReader.readlines() 
        y=DigitCodeData[d[e]]   
        s="1{}{}0000000000{}1".format(y[0],y[1],y[2])
        DictUpdateFunction(e)
    elif e=='=':
        with open('3DigitCodes.txt','r') as DigitCodeReader:
            DigitCodeData=DigitCodeReader.readlines() 
        y=DigitCodeData[d[e]]   
        s="10{}{}00000000{}01".format(y[0],y[1],y[2])
        DictUpdateFunction(e)
    elif e=='+':
        with open('3DigitCodes.txt','r') as DigitCodeReader:
            DigitCodeData=DigitCodeReader.readlines() 
        y=DigitCodeData[d[e]]   
        s="100{}{}000000{}001".format(y[0],y[1],y[2])
        DictUpdateFunction(e)
    elif e=='-':
        with open('3DigitCodes.txt','r') as DigitCodeReader:
            DigitCodeData=DigitCodeReader.readlines() 
        y=DigitCodeData[d[e]]   
        s="1000{}{}0000{}0001".format(y[0],y[1],y[2])
        DictUpdateFunction(e)
    elif e=='[':
        with open('3DigitCodes.txt','r') as DigitCodeReader:
            DigitCodeData=DigitCodeReader.readlines() 
        y=DigitCodeData[d[e]]   
        s="10000{}{}00{}00001".format(y[0],y[1],y[2])
        DictUpdateFunction(e)
    elif e==']':
        with open('3DigitCodes.txt','r') as DigitCodeReader:
            DigitCodeData=DigitCodeReader.readlines() 
        y=DigitCodeData[d[e]]   
        s="100000{}0{}{}00001".format(y[0],y[1],y[2])
        DictUpdateFunction(e)                              
    elif e=='{':
        with open('3DigitCodes.txt','r') as DigitCodeReader:
            DigitCodeData=DigitCodeReader.readlines() 
        y=DigitCodeData[d[e]]   
        s="1{}{}0{}0000000001".format(y[0],y[1],y[2])
        DictUpdateFunction(e)
    elif e=='}':
        with open('3DigitCodes.txt','r') as DigitCodeReader:
            DigitCodeData=DigitCodeReader.readlines() 
        y=DigitCodeData[d[e]]   
        s="1{}000{}{}00000001".format(y[0],y[1],y[2])
        DictUpdateFunction(e)
    elif e==':':
        with open('3DigitCodes.txt','r') as DigitCodeReader:
            DigitCodeData=DigitCodeReader.readlines() 
        y=DigitCodeData[d[e]]   
        s="1{}0000{}{}0000001".format(y[0],y[1],y[2])
        DictUpdateFunction(e)
    elif e==';':
        with open('3DigitCodes.txt','r') as DigitCodeReader:
            DigitCodeData=DigitCodeReader.readlines() 
        y=DigitCodeData[d[e]]   
        s="1{}00000{}{}000001".format(y[0],y[1],y[2])
        DictUpdateFunction(e)
    elif e=='.':
        with open('3DigitCodes.txt','r') as DigitCodeReader:
            DigitCodeData=DigitCodeReader.readlines() 
        y=DigitCodeData[d[e]]   
        s="1{}000000{}{}00001".format(y[0],y[1],y[2])
        DictUpdateFunction(e)                     
    elif e==',':
        with open('3DigitCodes.txt','r') as DigitCodeReader:
            DigitCodeData=DigitCodeReader.readlines() 
        y=DigitCodeData[d[e]]   
        s="1{}0000000{}{}0001".format(y[0],y[1],y[2])
        DictUpdateFunction(e)                     
    elif e=='<':
        with open('3DigitCodes.txt','r') as DigitCodeReader:
            DigitCodeData=DigitCodeReader.readlines() 
        y=DigitCodeData[d[e]]   
        s="1{}00000000{}{}001".format(y[0],y[1],y[2])
        DictUpdateFunction(e)                     
    elif e=='>':
        with open('3DigitCodes.txt','r') as DigitCodeReader:
            DigitCodeData=DigitCodeReader.readlines() 
        y=DigitCodeData[d[e]]   
        s="1{}000000000{}{}01".format(y[0],y[1],y[2])
        DictUpdateFunction(e)                     
    elif e=='/':
        with open('3DigitCodes.txt','r') as DigitCodeReader:
            DigitCodeData=DigitCodeReader.readlines() 
        y=DigitCodeData[d[e]]   
        s="1{}0000000000{}{}1".format(y[0],y[1],y[2])
        DictUpdateFunction(e)                     
    elif e=='?':
        with open('3DigitCodes.txt','r') as DigitCodeReader:
            DigitCodeData=DigitCodeReader.readlines() 
        y=DigitCodeData[d[e]]   
        s="1000{}00{}00{}0001".format(y[0],y[1],y[2])
        DictUpdateFunction(e)                     
    elif e=="'":
        with open('3DigitCodes.txt','r') as DigitCodeReader:
            DigitCodeData=DigitCodeReader.readlines() 
        y=DigitCodeData[d[e]]   
        s="10{}000{}{}0000001".format(y[0],y[1],y[2])
        DictUpdateFunction(e)                     
    elif e=='"':
        with open('3DigitCodes.txt','r') as DigitCodeReader:
            DigitCodeData=DigitCodeReader.readlines() 
        y=DigitCodeData[d[e]]   
        s="1{}00{}00{}0000001".format(y[0],y[1],y[2])
        DictUpdateFunction(e)                     
    elif e=="|":
        with open('3DigitCodes.txt','r') as DigitCodeReader:
            DigitCodeData=DigitCodeReader.readlines() 
        y=DigitCodeData[d[e]]   
        s="10{}000000{}{}0001".format(y[0],y[1],y[2])
        DictUpdateFunction(e)                     
    elif e=='~':
        with open('3DigitCodes.txt','r') as DigitCodeReader:
            DigitCodeData=DigitCodeReader.readlines() 
        y=DigitCodeData[d[e]]   
        s="10{}0000000{}{}001".format(y[0],y[1],y[2])
        DictUpdateFunction(e)                     
    elif e=='`':
        with open('3DigitCodes.txt','r') as DigitCodeReader:
            DigitCodeData=DigitCodeReader.readlines() 
        y=DigitCodeData[d[e]]   
        s="10{}00000000{}{}01".format(y[0],y[1],y[2])
        DictUpdateFunction(e)
    elif e=='₹':
        with open('3DigitCodes.txt','r') as DigitCodeReader:
            DigitCodeData=DigitCodeReader.readlines() 
        y=DigitCodeData[d[e]]   
        s="1000000{}{}0{}0001".format(y[0],y[1],y[2])
        DictUpdateFunction(e)
    elif e==' ':
        with open('3DigitCodes.txt','r') as DigitCodeReader:
            DigitCodeData=DigitCodeReader.readlines() 
        y=DigitCodeData[d[e]]   
        s="1000{}00{}0000{}01".format(y[0],y[1],y[2])
        DictUpdateFunction(e)      
    elif e=='0':
        with open('3DigitCodes.txt','r') as DigitCodeReader:
            DigitCodeData=DigitCodeReader.readlines() 
        y=DigitCodeData[d[e]]   
        s="1000000{}{}00{}001".format(y[0],y[1],y[2])
        DictUpdateFunction(e)  
    elif e=='1':
        with open('3DigitCodes.txt','r') as DigitCodeReader:
            DigitCodeData=DigitCodeReader.readlines() 
        y=DigitCodeData[d[e]]   
        s="1{}{}00000{}000001".format(y[0],y[1],y[2])
        DictUpdateFunction(e)  
    elif e=='2':
        with open('3DigitCodes.txt','r') as DigitCodeReader:
            DigitCodeData=DigitCodeReader.readlines() 
        y=DigitCodeData[d[e]]   
        s="1{}{}000000{}00001".format(y[0],y[1],y[2])
        DictUpdateFunction(e)
    elif e=='3':
        with open('3DigitCodes.txt','r') as DigitCodeReader:
            DigitCodeData=DigitCodeReader.readlines() 
        y=DigitCodeData[d[e]]   
        s="1{}{}00{}000000001".format(y[0],y[1],y[2])
        DictUpdateFunction(e)  
    elif e=='4':
        with open('3DigitCodes.txt','r') as DigitCodeReader:
            DigitCodeData=DigitCodeReader.readlines() 
        y=DigitCodeData[d[e]]   
        s="1{}{}000{}00000001".format(y[0],y[1],y[2])
        DictUpdateFunction(e) 
    elif e=='5':
        with open('3DigitCodes.txt','r') as DigitCodeReader:
            DigitCodeData=DigitCodeReader.readlines() 
        y=DigitCodeData[d[e]]   
        s="1{}{}0000{}0000001".format(y[0],y[1],y[2])
        DictUpdateFunction(e)  
    elif e=='6':
        with open('3DigitCodes.txt','r') as DigitCodeReader:
            DigitCodeData=DigitCodeReader.readlines() 
        y=DigitCodeData[d[e]]   
        s="1{}{}0000000{}0001".format(y[0],y[1],y[2])
        DictUpdateFunction(e)  
    elif e=='7':
        with open('3DigitCodes.txt','r') as DigitCodeReader:
            DigitCodeData=DigitCodeReader.readlines() 
        y=DigitCodeData[d[e]]   
        s="1{}{}00000000{}001".format(y[0],y[1],y[2])
        DictUpdateFunction(e)  
    elif e=='8':
        with open('3DigitCodes.txt','r') as DigitCodeReader:
            DigitCodeData=DigitCodeReader.readlines() 
        y=DigitCodeData[d[e]]   
        s="1{}{}000000000{}01".format(y[0],y[1],y[2])
        DictUpdateFunction(e)  
    elif e=='9':
        with open('3DigitCodes.txt','r') as DigitCodeReader:
            DigitCodeData=DigitCodeReader.readlines() 
        y=DigitCodeData[d[e]]   
        s="10000{}{}000{}0001".format(y[0],y[1],y[2])
        DictUpdateFunction(e)                               
    s="100000000000001"    
with open("EncodedFile.txt","a") as f5:
    f5.write(RandomNumber) 
a=len(RandomNumber)         
with open("EncodedFile.txt","r") as f2:
    Data=f2.read()
    x=len(Data)
    print(Data[100])
while i<(x-a):
    String=Data[i:i+15]
    i=i+15
    if String[10]!='0' and String[11]!='0' and String[12]!='0':
        with open("DecodedMessage.txt",'a') as f3:
            f3.write('a')
    elif String[7]!='0' and String[8]!='0' and String[9]!='0':    
        with open("DecodedMessage.txt",'a') as f3:
            f3.write('b') 
    elif String[4]!='0' and String[5]!='0' and String[6]!='0': 
        with open("DecodedMessage.txt",'a') as f3:
            f3.write('c') 
    elif String[1]!='0' and String[2]!='0' and String[3]!='0': 
        with open("DecodedMessage.txt",'a') as f3:
            f3.write('d')
    elif String[6]!='0' and String[10]!='0' and String[11]!='0': 
        with open("DecodedMessage.txt",'a') as f3:
            f3.write('e')
    elif String[2]!='0' and String[3]!='0' and String[4]!='0': 
        with open("DecodedMessage.txt",'a') as f3:
            f3.write('f')
    elif String[3]!='0' and String[4]!='0' and String[5]!='0': 
        with open("DecodedMessage.txt",'a') as f3:
            f3.write('g')
    elif String[5]!='0' and String[6]!='0' and String[7]!='0': 
        with open("DecodedMessage.txt",'a') as f3:
            f3.write('h')
    elif String[6]!='0' and String[7]!='0' and String[8]!='0': 
        with open("DecodedMessage.txt",'a') as f3:
            f3.write('i')
    elif String[8]!='0' and String[9]!='0' and String[10]!='0': 
        with open("DecodedMessage.txt",'a') as f3:
            f3.write('j')                                                                       
    elif String[9]!='0' and String[10]!='0' and String[11]!='0': 
        with open("DecodedMessage.txt",'a') as f3:
            f3.write('k')
    elif String[11]!='0' and String[12]!='0' and String[13]!='0': 
        with open("DecodedMessage.txt",'a') as f3:
            f3.write('l')
    elif String[1]!='0' and String[3]!='0' and String[5]!='0': 
        with open("DecodedMessage.txt",'a') as f3:
            f3.write('m')
    elif String[2]!='0' and String[4]!='0' and String[6]!='0': 
        with open("DecodedMessage.txt",'a') as f3:
            f3.write('n')                                
    elif String[3]!='0' and String[5]!='0' and String[7]!='0': 
        with open("DecodedMessage.txt",'a') as f3:
            f3.write('o')
    elif String[4]!='0' and String[6]!='0' and String[8]!='0': 
        with open("DecodedMessage.txt",'a') as f3:
            f3.write('p')
    elif String[5]!='0' and String[7]!='0' and String[9]!='0': 
        with open("DecodedMessage.txt",'a') as f3:
            f3.write('q')
    elif String[6]!='0' and String[8]!='0' and String[10]!='0': 
        with open("DecodedMessage.txt",'a') as f3:
            f3.write('r')
    elif String[7]!='0' and String[9]!='0' and String[11]!='0': 
        with open("DecodedMessage.txt",'a') as f3:
            f3.write('s')                                        
    elif String[8]!='0' and String[10]!='0' and String[12]!='0': 
        with open("DecodedMessage.txt",'a') as f3:
            f3.write('t')
    elif String[9]!='0' and String[11]!='0' and String[13]!='0': 
        with open("DecodedMessage.txt",'a') as f3:
            f3.write('u')
    elif String[1]!='0' and String[4]!='0' and String[5]!='0': 
        with open("DecodedMessage.txt",'a') as f3:
            f3.write('v')
    elif String[2]!='0' and String[5]!='0' and String[6]!='0': 
        with open("DecodedMessage.txt",'a') as f3:
            f3.write('w')
    elif String[3]!='0' and String[6]!='0' and String[7]!='0': 
        with open("DecodedMessage.txt",'a') as f3:
            f3.write('x')
    elif String[4]!='0' and String[7]!='0' and String[8]!='0': 
        with open("DecodedMessage.txt",'a') as f3:
            f3.write('y')
    elif String[5]!='0' and String[8]!='0' and String[9]!='0': 
        with open("DecodedMessage.txt",'a') as f3:
            f3.write('z')
    elif String[2]!='0' and String[4]!='0' and String[5]!='0': 
        with open("DecodedMessage.txt",'a') as f3:
            f3.write('!')
    elif String[1]!='0' and String[3]!='0' and String[4]!='0': 
        with open("DecodedMessage.txt",'a') as f3:
            f3.write('@')                    
    elif String[2]!='0' and String[5]!='0' and String[7]!='0': 
        with open("DecodedMessage.txt",'a') as f3:
            f3.write('#')
    elif String[6]!='0' and String[7]!='0' and String[10]!='0': 
        with open("DecodedMessage.txt",'a') as f3:
            f3.write('$')                    
    elif String[5]!='0' and String[8]!='0' and String[10]!='0': 
        with open("DecodedMessage.txt",'a') as f3:
            f3.write('%')                    
    elif String[4]!='0' and String[8]!='0' and String[9]!='0': 
        with open("DecodedMessage.txt",'a') as f3:
            f3.write('^')                    
    elif String[2]!='0' and String[7]!='0' and String[8]!='0': 
        with open("DecodedMessage.txt",'a') as f3:
            f3.write('&')                    
    elif String[10]!='0' and String[11]!='0' and String[13]!='0': 
        with open("DecodedMessage.txt",'a') as f3:
            f3.write('*')                    
    elif String[6]!='0' and String[7]!='0' and String[8]!='0': 
        with open("DecodedMessage.txt",'a') as f3:
            f3.write('(')                    
    elif String[5]!='0' and String[7]!='0' and String[8]!='0': 
        with open("DecodedMessage.txt",'a') as f3:
            f3.write(')')             
    elif String[1]!='0' and String[2]!='0' and String[13]!='0': 
        with open("DecodedMessage.txt",'a') as f3:
            f3.write('_')
    elif String[2]!='0' and String[3]!='0' and String[12]!='0': 
        with open("DecodedMessage.txt",'a') as f3:
            f3.write('=')                    
    elif String[3]!='0' and String[4]!='0' and String[11]!='0': 
        with open("DecodedMessage.txt",'a') as f3:
            f3.write('+')                    
    elif String[4]!='0' and String[5]!='0' and String[10]!='0': 
        with open("DecodedMessage.txt",'a') as f3:
            f3.write('-')                    
    elif String[5]!='0' and String[6]!='0' and String[9]!='0': 
        with open("DecodedMessage.txt",'a') as f3:
            f3.write('[')                    
    elif String[6]!='0' and String[8]!='0' and String[9]!='0': 
        with open("DecodedMessage.txt",'a') as f3:
            f3.write(']')                    
    elif String[1]!='0' and String[2]!='0' and String[4]!='0': 
        with open("DecodedMessage.txt",'a') as f3:
            f3.write('{')
    elif String[1]!='0' and String[5]!='0' and String[6]!='0': 
        with open("DecodedMessage.txt",'a') as f3:
            f3.write('}')                    
    elif String[1]!='0' and String[6]!='0' and String[7]!='0': 
        with open("DecodedMessage.txt",'a') as f3:
            f3.write(':')                    
    elif String[1]!='0' and String[7]!='0' and String[8]!='0': 
        with open("DecodedMessage.txt",'a') as f3:
            f3.write(';')                    
    elif String[1]!='0' and String[8]!='0' and String[9]!='0': 
        with open("DecodedMessage.txt",'a') as f3:
            f3.write('.')                    
    elif String[1]!='0' and String[9]!='0' and String[10]!='0': 
        with open("DecodedMessage.txt",'a') as f3:
            f3.write(',')                    
    elif String[1]!='0' and String[10]!='0'and String[11]!='0': 
        with open("DecodedMessage.txt",'a') as f3:
            f3.write('<')                    
    elif String[1]!='0' and String[11]!='0' and String[12]!='0': 
        with open("DecodedMessage.txt",'a') as f3:
            f3.write('>')                    
    elif String[1]!='0' and String[12]!='0' and String[13]!='0': 
        with open("DecodedMessage.txt",'a') as f3:
            f3.write('/')                    
    elif String[4]!='0' and String[7]!='0' and String[10]!='0': 
        with open("DecodedMessage.txt",'a') as f3:
            f3.write('?')
    elif String[1]!='0' and String[6]!='0' and String[7]!='0': 
        with open("DecodedMessage.txt",'a') as f3:
            f3.write("'")
    elif String[1]!='0' and String[4]!='0' and String[7]!='0': 
        with open("DecodedMessage.txt",'a') as f3:
            f3.write('"')                    
    elif String[2]!='0' and String[9]!='0' and String[10]!='0': 
        with open("DecodedMessage.txt",'a') as f3:
            f3.write('|')  
    elif String[2]!='0' and String[10]!='0' and String[11]!='0': 
        with open("DecodedMessage.txt",'a') as f3:
            f3.write('~')                    
    elif String[2]!='0' and String[11]!='0' and String[12]!='0': 
        with open("DecodedMessage.txt",'a') as f3:
            f3.write('`')
    elif String[7]!='0' and String[8]!='0' and String[10]!='0': 
        with open("DecodedMessage.txt",'a') as f3:
            f3.write('₹')                                    
    elif String[7]!='0' and String[8]!='0' and String[11]!='0': 
        with open("DecodedMessage.txt",'a') as f3:
            f3.write('0')    
    elif String[1]!='0' and String[2]!='0' and String[8]!='0': 
        with open("DecodedMessage.txt",'a') as f3:
            f3.write('1')                                    
    elif String[1]!='0' and String[2]!='0' and String[9]!='0': 
        with open("DecodedMessage.txt",'a') as f3:
            f3.write('2')                                    
    elif String[1]!='0' and String[2]!='0' and String[5]!='0': 
        with open("DecodedMessage.txt",'a') as f3:
            f3.write('3')                                    
    elif String[1]!='0' and String[2]!='0' and String[6]!='0': 
        with open("DecodedMessage.txt",'a') as f3:
            f3.write('4')                                    
    elif String[1]!='0' and String[2]!='0' and String[7]!='0': 
        with open("DecodedMessage.txt",'a') as f3:
            f3.write('5')                                    
    elif String[1]!='0' and String[2]!='0' and String[10]!='0': 
        with open("DecodedMessage.txt",'a') as f3:
            f3.write('6')                                    
    elif String[1]!='0' and String[2]!='0' and String[11]!='0': 
        with open("DecodedMessage.txt",'a') as f3:
            f3.write('7')                                    
    elif String[1]!='0' and String[2]!='0' and String[12]!='0': 
        with open("DecodedMessage.txt",'a') as f3:
            f3.write('8')                                    
    elif String[5]!='0' and String[6]!='0' and String[10]!='0': 
        with open("DecodedMessage.txt",'a') as f3:
            f3.write('9')
    elif String[4]!='0' and String[7]!='0' and String[12]!='0': 
        with open("DecodedMessage.txt",'a') as f3:
            f3.write(' ')                                                    
    else:
        with open("DecodedMessage.txt",'a') as f3:
            f3.write('WRONGINPUT')                           