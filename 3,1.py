f1 = open("F1.txt", "w+")
f2 = open("F2.txt", "w+")
while True:
    a = input("Enter info: ")
    if a == "":
        break
    if a[0] == "a" or a[0] == "A":
        f2.write(a + "\n")
    f1.write(a + "\n")
f1.seek(0)
f2.seek(0)
print(f"First file: {f1.read()}")
print(f"Second file: {f2.read()}")
f1.close()
f2.close()