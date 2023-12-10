f = 'input.txt'
signal = open(f).read()

for i in range(len(signal)-3):
    s = signal[i:i+14]
    print(s)
    if len(set(s)) == 14:
        print(i+14)
        break

