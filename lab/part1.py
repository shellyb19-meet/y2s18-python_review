def hello_world():
	print("hello world")

def greet_by_name(name):
	print("hello", name)

def encode(x):
	return x*3953531
a=encode(2)

def decode(x):
	return x/3953531
b=decode(a)
print(b)