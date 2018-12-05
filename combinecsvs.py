from glob import glob

with open('allBlendcollections.csv', 'a') as singleFile:
    for csv in glob('*.csv'):
        if csv == 'allBlendcollections.csv':
            pass
        else:
            for line in open(csv, 'r'):
                singleFile.write(line)
