#fhand = open('mbox.txt')
#for line in fhand:
#    count = count + 1
#       print('Line Count:', count)

#   inp = fhand.read()
#       print(len(inp))

#    if line.startswith('From:'):
#        print(line)


fhand = open('mbox-short.txt')
for line in fhand:
    if line.startswith('FROM STEPHEN.MARQUARD@UCT.AC.ZA SAT JAN 5 09:14:16 2008'):
        print(line)
