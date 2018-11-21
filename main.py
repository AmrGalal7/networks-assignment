from generator import Generator
from verifier import Verifier

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


inputString= input("Enter your command\n")
counter =0
for c in range(len(inputString)):
	if inputString[c]=="|":
		counter+=1

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
			m=m[:-1]
		k=file.readline()
		return m , k , inputString
	if(flag==2):
		bit=""
		for t in range(len(inputString)):
			if(inputString[t].isdigit()):
				bit+=str(inputString[t])
		return int(bit), inputString

# case of generator and verifier
if(counter==1):
	m , k , inputString = getDataFromFile(1,inputString)
	g = Generator(m, k)
	genOutput = g.encode()
	g.GeneratorDivider = g.getDivider()
	v = Verifier(genOutput, g.GeneratorDivider)
	v.verify()
# case of generator, alter, and verifier
if(counter==2):
	m , k , inputString = getDataFromFile(1,inputString)
	g = Generator(m, k)
	genOutput = g.encode()
	g.GeneratorDivider = g.getDivider()
	bit , inputString = getDataFromFile(2,inputString)
	messageAltered = alter(bit, genOutput)
	v = Verifier(messageAltered, g.GeneratorDivider)
	v.verify()

