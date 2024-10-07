with open("cnbc_data.txt") as file:
    data = file.readlines()

symbols = [data[i].split("\n")[0] for i in range(0, len(data) - 1, 2)]
symbols2 = ["_{}".format(data[i].split("\n")[0]) for i in range(0, len(data) - 1, 2)]

for symbol in range(30):
    print(f"[{symbols[symbol]}, {symbols2[symbol]}] = request.security('{symbols[symbol]}','D', [close, close[1]])")

print("")

array = f"closeValues = array.from({','.join(symbols)})"
array2 = f"p_closeValues = array.from({','.join(symbols2)})"

print(array)
print(array2)
