# Mission 1

for i in range(5):
    print("*"  * 1)

for i in range(1,6):
    print("*"  * 1)

for i in range(1,6,1):
    print("*"  * 1)

for i in range(1,6,2):
    print("*"  * 1)

for i in range(1,6,3):
    print("*"  * 1)


# Mission 2
name = input("ismin nedir?")
lenght = len(name) + 2

print("*"* lenght)
print("*"+ name + "*")
print("*"* lenght)

# Misson 3  

n = int(input("Lütfen bir sayıya basınız: "))
total = 0

for i in range(1, n +1):
     total += i
print(f"toplam: {total}")

