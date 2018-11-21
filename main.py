
import re
inputString= raw_input("Enter your command\n")
print("text = ", inputString)
counter =0
for c in range(len(inputString)):
	if inputString[c]=="|":
		counter+=1
#print(counter)

def getDataFromFile(flag,inputString):
#open file and get data from it
	pureInput= inputString.replace(" ","")
	if(flag ==1):
		assignPosition = pureInput.find("<")
		pureInput= pureInput[assignPosition+1:]
	orPosition = pureInput.find("|")
	fileName= pureInput[:orPosition]
	if(flag==1):
		inputString=pureInput[orPosition+1:]
		file = open(fileName+".txt","r")
		m=file.readline()
		if(m.find("\n")):
			m=m[:-2]
		k=file.readline()
		return m , k , inputString
	if(flag==2):
		bit=""
		for t in range(len(inputString)):
			if(inputString[t].isdigit()):
				bit+=str(inputString[t])
		return bit, inputString

if(counter==1):
	m , k , inputString = getDataFromFile(1,inputString)
	print("m= ", m , " k= ", k , "remaining = ", inputString)
if(counter==2):
	m , k , inputString = getDataFromFile(1,inputString)
	print("m= ", m , " k= ", k , "remaining = ", inputString)
	bit , inputString = getDataFromFile(2,inputString)
	print("Bit =",bit)



def alter(convertedBit, message):

	firstPart=message[:convertedBit-1]
	#print("firstPart = ",firstPart)
	targetedBit=message[convertedBit-1]
	#print("targetedBit = ",targetedBit)
	secondPart=message[convertedBit:]
	#print("secondPart = ",secondPart)
	targetedBitInt=int(targetedBit)
	targetedBitInt =(targetedBitInt^ 1)
	#print("Converted targetedBit = ",targetedBitInt)
	falseMassage=firstPart+str(targetedBitInt)+secondPart
	#print("falseMassage = ",falseMassage)
	return falseMassage;


x = alter(3,"10111")
print("X = ",x)