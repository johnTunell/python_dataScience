lines = open('transactions1000.nt.txt').read().splitlines()
transactions = [map(int, line.split()) for line in lines]
print transactions[:1] # first correct
print transactions[-1:] # last correct
