import ast 
import re


def getPatternDictionary():
    with open('DictCodes.txt', 'r') as patternData:        
        patterns = ast.literal_eval( patternData.read() )
    return patterns



def getZeroCodesDictionary():
    with open('Dict.txt', 'r') as codeData:        
        codes_dict = ast.literal_eval( codeData.read() )
    return codes_dict    


def setZeroCodesDictionary(codes_dict):
    with open('Dict.txt', 'w') as codeData:
        codeData.write(str(codes_dict)) 

def get3DigitCodes():
    with open('3DigitCodes.txt','r') as digitCodeReader:
        digitCodeData = digitCodeReader.readlines()
    return digitCodeData


def setDatatoEncodedFile(encoded_single_char):
    with open('InputText.txt_encodedFile.txt', 'a') as encodingFile:
        encodingFile.write(encoded_single_char)

def getEncodedData():
    with open('InputText.txt_encodedFile.txt','r') as encodedCodeReader:
        encodedData=encodedCodeReader.read()
    return encodedData   
def decodeDictionary():
    with open('decodingDictFile.txt','r') as decodeDictionaryReaader:
        decodingData=decodeDictionaryReaader.read()
        decodingDictionaryData=ast.literal_eval(decodingData)  
    return decodingDictionaryData   
   

def encodeFile(filename):
    print("started encoding "+filename)
    with open(filename, 'r') as inputfile: 
        encoded_single_char = ""
        singleLine = inputfile.readline()
        patternCodes = getPatternDictionary()
        codes_of_chars = getZeroCodesDictionary()
        digit3codes = get3DigitCodes()
        while singleLine:        

            for singleChar in singleLine:                        
                
                if singleChar in patternCodes:

                    dict_key_usage =codes_of_chars[str(singleChar)]
                    if dict_key_usage==8:
                        dict_key_usage=0
                        codes_of_chars[singleChar]=dict_key_usage

                    dict_pattern =patternCodes[str(singleChar)]
                    codes_of_chars[str(singleChar)] = codes_of_chars[str(singleChar)] + 1                                
                    digit3code_singleChar = digit3codes[dict_key_usage]
                    if singleChar.isupper():
                        encoded_single_char = dict_pattern.format(digit3code_singleChar[0], digit3code_singleChar[1], digit3code_singleChar[2],'1')
                    else:
                        encoded_single_char = dict_pattern.format(digit3code_singleChar[0], digit3code_singleChar[1], digit3code_singleChar[2],'0')   
                    setDatatoEncodedFile(encoded_single_char)                    
                else:
                    print("char doesnot exist in patterncodes"+singleChar)            
            singleLine = inputfile.readline()
    setZeroCodesDictionary(codes_of_chars)
    print("completed encoding "+filename) 


def decoding():
    i=0
    dataEncoded=getEncodedData()
    dictData=decodeDictionary()
    dictKeys=list(dictData.keys())
    dictValues=list(dictData.values())
    while i<len(dataEncoded):
        string=dataEncoded[i:i+16]
        i+=16
        j=0
        for e in dictValues:
            match=re.fullmatch(dictValues[j],string)
            if match!=None:
                msg=dictKeys[j]
                with open('DecodedMessage.txt','a') as decodeMsgWritter:
                    decodeMsgWritter.write(msg) 
            j+=1
encodeFile('InputText.txt')
 
decoding()        
 



    



