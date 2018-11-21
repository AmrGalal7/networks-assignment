from generator import Generator
from verifier import Verifier

def bitstring(x):  return bin(x)[2:]

def printlongdiv(lhs, rhs):
    rem = lhs
    div = rhs
    origlen = len(bitstring(div))
		# data = ""
    # first shift left until the leftmost bits line up.
    count = 1
    while (div | rem) > 2*div:
        div <<= 1
        count += 1
				
    # now keep dividing until we are back where we started.
    quot = 0
		data = ""
    while count>0:
        quot <<= 1
        count -= 1
        data = data + ("%14s" % bitstring(rem)) + "/n"
        divstr = bitstring(div)
        if (rem ^ div) < rem:
            quot |= 1
            rem ^= div
            data = data + (1, " " * (11-len(divstr)), divstr[:origlen]) + "/n"
        else:
            data = data + (0, " " * (11-len(divstr)), "0" * origlen) + "/n"
        data = data + (" " * (13-len(divstr)), "-" * origlen) + "/n"
        div >>= 1
    data = data + ("%14s <<< remainder" % bitstring(rem)) + "/n"
    data = data + (" -> %10s <<< quotient" % bitstring(quot)) + "/n"

		with open('longDivision.txt', 'w') as f:
				f.write(data)


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
	printlongdiv(int(m, 2), int(k, 2))
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



