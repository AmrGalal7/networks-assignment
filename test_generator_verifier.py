from generator import Generator
from verifier import Verifier


mString = '10001'
kString = '11'
g = Generator(mString, kString)
genOutput = g.encode()
print(genOutput)
g.GeneratorDivider = g.getDivider()
v = Verifier(genOutput, g.GeneratorDivider)
v.verify()
temp = '1000011'
v = Verifier(temp, g.GeneratorDivider)
v.verify()
