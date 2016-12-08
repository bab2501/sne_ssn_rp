#ENQ
a = 7;
b = 2;


def encr( x,a,b ):
	alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
	r = alphabet.index(x)
	z = (a*r+b)%26
	return alphabet[z]

plaintext = "HALLO YOU ARE HERE HELLO"
ciphertext = ""
for char in plaintext:
	if char == " ":
		char = "X"
	ciphertext = ciphertext + encr( char,a,b )

print ciphertext

#DEC
a = 7;
b = 2;
def dec( x,a,b ):
	alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
	r = alphabet.index(x)	
	w = int(round( ( a**-1 ) * 100 )) +1
	z = w*(r-b)
	return alphabet[z%26]

ciphertext = "ZCBBWHOWMHCREHZEREHZEBBW"
plainout = ""
for char in ciphertext:
	plainout = plainout + dec( char,a,b )

print plainout

