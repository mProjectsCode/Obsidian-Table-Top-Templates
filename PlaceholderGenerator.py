import os

print('Creating .gitkeep files in:')
for root, dirs, files in os.walk('.'):
    if root.__contains__('.git'):
        continue

    if dirs.__len__() == 0 and files.__len__() == 0:
        print(root)
        f = open(os.path.join(root, '.gitkeep'), 'w')
        f.write('Needed so that git keeps track of the folder')
        f.close()
