ip = int(input('Enter no of people in the room: '))
handshakes = 0
for i in range(1,ip+1):
    handshakes += (ip - (i))

print(handshakes)

