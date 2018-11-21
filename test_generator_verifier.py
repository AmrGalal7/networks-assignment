from generator import Generator
from verifier import Verifier

############## test case 1 ####################
mString = '10011101'
kString = '1001'
g = Generator(mString, kString)
genOutput = g.encode()
print(genOutput)
g.GeneratorDivisor = g.getDivisor()
v = Verifier(genOutput, g.GeneratorDivisor)
v.verify()
# alter 3rd bit
temp = '10111101100'
v = Verifier(temp, g.GeneratorDivisor)
v.verify()


############## test case 2 ####################
mString = '1101011111'
kString = '10011'
g = Generator(mString, kString)
genOutput = g.encode()
print(genOutput)
g.GeneratorDivisor = g.getDivisor()
v = Verifier(genOutput, g.GeneratorDivisor)
v.verify()
# alter 3rd bit
temp = '10111101100'
v = Verifier(temp, g.GeneratorDivisor)
v.verify()
