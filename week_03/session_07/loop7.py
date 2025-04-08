too = int(input("toog oruulna uu\n"))
anhnii_too = True
for i in range(2,too):
    if too%i == 0:
        anhnii_too = False
print(f"{too} anhnii too mun eseh: {anhnii_too}")