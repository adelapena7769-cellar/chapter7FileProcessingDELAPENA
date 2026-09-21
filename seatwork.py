fname = input('Enter a File name: ')
fhand = open(fname)
count = 0
sum = 0

for line in fhand:

    parts = line.split(':')

    if line.startswith('X-DSPAM-Confidence:') and len(parts)>1:
        count += 1
        sum += float(parts[1])
        print(f"{parts[0]} {sum}")

print(f"Count: {count}, Average: {sum/count}")





