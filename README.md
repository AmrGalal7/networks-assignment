# networks-assignment
Computer Networks course assignemnt, Fall 2018.
CRC based message encoder and error detector.

## running
Open main.exe
- type `generator < file | verifier` to encode the message and have it checked by the verifier.
- type `generator < file | alter pos | verifier` to invert the 'pos' bit in the encoded message, where 'pos' is a number from 1 to message length, then run the verifier.

*make sure 'file' is in the same directory as main.exe, and use only the file name (i.e. without '.txt')*
#### using terminal:
type `python3 main.py`, then use the same commands as above.

### input
- **file**: a .txt file with two lines: the first is the message to be encoded, and the second is the key/ polynomial

### output:
- **transmitted_msg.txt**: a .txt file with the encoded message.
- **longDivision.txt**: a .txt file with the long division steps.

