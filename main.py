import mean_var_std

# tab1 = [1,2,3,4,5,6,7,8,9]
# tab2 = [1,2,3,4,5,6,7,9]
# print(mean_var_std.calculate(tab1))
# print(mean_var_std.calculate(tab2))
print("Please enter 9 elements, type 'end' to finish:")
tab = []
while True:
    saisie = input("Element: ")
    if(saisie.lower() == "end"):
        break
    else:
        tab.append(int(saisie))
print(mean_var_std.calculate(tab))