n = input()
convert_n = list(n)
s = []
for i in range(len(convert_n)):
    if convert_n[i] == "1" or convert_n[i] == "2" or convert_n[i] == "3" or convert_n[i] == "1" or convert_n[i] == "4"or convert_n[i] == "5" or convert_n[i] == "6" or convert_n[i] == "7" or convert_n[i] == "8" or convert_n[i] == "9" or convert_n[i] == "0":
        s.append(convert_n[i])
print(s)