message = "Hello World"

print(message)
print(len(message))
print(message[6:])
print(message.lower())
print(message.upper())
print(message.count('l'))
print(message.find('l'))
print(message.replace('H','J'))
new_message = message.replace('World','Universe')
print(new_message)

greeting = 'Hello'
name = 'Sophia'
message = greeting + ', ' + name + '. Welcome!'
print(message)

message = f'{greeting}, {name.upper()}. Welcome to Python!'
print(message)

print(dir(name))
print(help(str))