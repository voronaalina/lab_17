import pandas 

df = pandas.read_csv("c:\\lab17\\masiv.csv", header=None)
row_sums = df.sum(axis=1)

with open("c:\\lab17\\res.txt", 'w') as f:
    for sum_value in row_sums:
        f.write(str(sum_value) + "\n")

print("Суми рядків записано у res.txt")
