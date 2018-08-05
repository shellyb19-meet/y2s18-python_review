def is_prime(x):
	for i in range(2,x):
		if x%i==0:
			return False
	return True

def encode(x, y):
	if((1<y and y<250) and (500<x and x<1000)):
		print("Invalid input: Outside range")
		return 
	else:
		while(!is_prime(x)):
			x=x+1
		if(!(x<1000)):
			print("Invalid input: Outside range")
			return 
		while(!is_prime(y)):
			y=y+1
		if(!(y<250)):
			print("Invalid input: Outside range")
			return 
	return x*y
	


def decode(coded_message):
	for y in range(2,250):
		if(is_prime(y)):
			
