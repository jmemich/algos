import os
import percolation


path = os.path.join(os.path.dirname(percolation.__file__), 'data')
files = os.listdir(path)
txt_files = [file for file in files if file.endswith('txt')]

# fuck formatting issues - here is quick test
for file in ['input2.txt', 'input7.txt']:
    with open(os.path.join(path, file), 'r') as f:
        lines = f.readlines()
        N = int(lines[0].strip('\n'))
        # `bullshit` arg to coerce to zero-index
        p = percolation.Percolation(N, bullshit=True)
        for line in lines[1:]:
            str_split = line.strip('\n').split(' ')
            if len(str_split) == 2:
                point = tuple([int(i) for i in str_split])
                print(point)
                p.open(point)
            print(p)




