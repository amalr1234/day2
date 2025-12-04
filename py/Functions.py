# Functions with parameters

def greet_person(name):
    print(f"Hello,{name}!")

greet_person("Amal")

#Functions with return values
def add_numbers(a, b):
    return a + b

result = add_numbers (5, 3)
print(result)

#default parameters

def greet_with_title(name, title="Mr"):
    return f"Hello,{ title} {name}!"

print(greet_with_title("Smith"))
print(greet_with_title("Johnson", "Dr."))

#args (variable number of arguments)

def sum_all(*args):
    return sum (args)
print(sum_all(1, 4, 7, 8, 5, 2 ,3, 6, 9))

#kwargs- keyword arguments

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    
print_info(name= "Amal" , age= "25" , city= "Kota Bharu")

#combing args + kwargs

def flexible_function(*args, **kwargs):
    print("Positional Arguments:", args)
    print("Keyword Arguments:", kwargs)

flexible_function(1,2,3, name="Amani" , age=17)

#lambda

square = lambda x: x**2
print(square(5))

add = lambda x, y: x + y
print(add(3,4))

#Exercise
#Write a functions that checks if a number is prime.

def is_prime (n:int) ->bool:   # definisikan is prime yang terima n | n:int type hint n dijangka intiger | bool:jawapan boleh jadi True/False
    if not isinstance(n, int): #semak n jika n adalah integer
        return False           #jika n bukan integer, False
    if n<=1:                   #check kalau n=1 atau less than 1
        return False           #nombor perdana(n) kena lebih besar dari 1, kalau n=1, jawapan akan jadi False
    if n%2 == 0:               #check if n boleh dibahagi dengan 2
        return False           #False, kalau n genap
    
    i=3                 #tetapkan i(pemboleh ubah) =3,guna i sebagai pembahagi start dari 3 (check no ganjil sahaja)
    while i * i<=n:     # selagi i x i tak lebih besar dar n, kita kena check
        if  n % i==0:   #kalau nombor boleh bahagi dengan nombor i tanpa baki, maksudnya bukan prime
            return False #False kalau takde baki
        i  += 2          # untuk check ganjil,
        return True
    
tests = [-1, 2, 3, 4, 5, 8, 9, 66, 39, 17, 45, 100]
for t in tests:
    print(f"{t} : {"Prime" if is_prime(t) else "Not Prime"}")



