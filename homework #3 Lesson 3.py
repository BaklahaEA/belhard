name = "Eugene"
age = 28
city = "Minsk"
text = "Hello! My name is {name}. I am {age} years old. I am live in {city}.".format(name = name, age = age, city = city)# способ 1
text2 = f"Hello! My name is {name}. I am {age} years old. I am live in {city}."# способ 2
text3 = "Hello! My name is {}. I am {} years old. I am live in {}".format(name, age, city) # способ 3
print(text)
print(text2)
print(text3)