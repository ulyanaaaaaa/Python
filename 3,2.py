results = []
with open("comp_results.txt", encoding="utf-8") as file:
    for line in file:
        line = line.split()
        results.append((line[0], line[1]))

results.sort(key = lambda x: x[1])

print(f"{results[0][1]} место:")
print(f"Фамилия: {results[0][0]}")

print(f"{results[1][1]} место:")
print(f"Фамилия: {results[1][0]}")

print(f"{results[2][1]} место:")
print(f"Фамилия: {results[2][0]}")


