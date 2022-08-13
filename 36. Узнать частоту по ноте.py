note = input("Введите название ноты в виде буквы и цифры: ")

C4_FREQ = 261.63
D4_FREQ = 293.66
E4_FREQ = 329.63
F4_FREQ = 349.23
G4_FREQ = 392.00
A4_FREQ = 440.00
B4_FREQ = 493.88

b = note[0]
x = int(note[1])
f = 2 ** 4 - x
    
if b == "C":
 freq = C4_FREQ
elif b == "D":
 freq = D4_FREQ
elif b == "E":
 freq = E4_FREQ
elif b == "F":
 freq = F4_FREQ
elif b == "G":
 freq = G4_FREQ
elif b == "A":
 freq = A4_FREQ
elif b == "B":
 freq = B4_FREQ

freq = freq / 2 ** (4 - x)
print("Частота ноты", note, "равна", freq)
