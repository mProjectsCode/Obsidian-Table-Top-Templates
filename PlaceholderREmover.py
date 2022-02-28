import os

print('Removing .gitkeep files in:')
for root, dirs, files in os.walk('.'):
    if root.__contains__('.git'):
        continue

    for file in files:
        if file == '.gitkeep':
            print(root)
            os.remove(os.path.join(root, file))
