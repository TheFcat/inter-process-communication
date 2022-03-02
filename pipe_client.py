def calculate_median(data):
    data.sort()
    if len(data) % 2 == 1:
        return data[len(data) // 2]
    else:
        return (data[len(data) // 2] + data[len(data) // 2 + 1]) / 2


print('Client2 is ready')
r = input()
print(calculate_median(eval(r)))