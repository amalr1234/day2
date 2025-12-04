text = "Amal Rumaisha"

print (text[0])
print (text[-1])
print (text[0:6])
print (text[:6])
print (text[7:])

name = "Leo The Cat"

print(len(name))
print(name.strip())
print(name.upper())
print(name.lower())
print(name.title())
print(name.replace("Leo" , "Biscoff"))

name = "Aisyah Maryam"
age = 25

message_1 = f"My name is {name} and I am {age} years old."
message_2 = "My name is {} and I am {} years old." .format(name,age)
message_3 = "My name is %s and I am %d years old. " % (name, age)

print(message_1)
print(message_2)
print(message_3)

text = """Python is a powerful programming language. It's easy to learn and versatile!
You can use Python for web development, data science and automation. The syntax is clean and readable.
This make Python perfect for beginners and experts alike"""

characters = len (text)
words = len(text.split())
sentences= text.count(".") + text.count("!")

print(f"The text above has {characters} characters ,{words} words and it has {sentences} sentences. It is perfect")
                           
