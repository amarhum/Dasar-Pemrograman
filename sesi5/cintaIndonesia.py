kata = ["Aku cinta Indonesia", "", "Aku cinta Indonesia", "", "Aku cinta Indonesia"]

for i,kata in enumerate(kata):
    i += 1
    if i % 2 == 1:
        print(i,kata)