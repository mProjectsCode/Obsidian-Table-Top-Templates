import os
import shutil
from distutils.dir_util import copy_tree


VaultFolderStructureFolder = 'VaultTemplateFolderStructure'
NoteTemplateFolder = 'NoteTemplates'
TemplateVaultFolder = 'VaultTemplate'
Snippets = 'Snippets'

print()

if os.path.exists(VaultFolderStructureFolder):
    print('VaultTemplateFolderStructure folder exists')
else:
    raise Exception('VaultTemplateFolderStructure folder does not exist')

if os.path.exists(NoteTemplateFolder):
    print('NoteTemplate folder exists')
else:
    raise Exception('NoteTemplate folder does not exist')

if os.path.exists(TemplateVaultFolder):
    print('VaultTemplate folder exists')
else:
    raise Exception('VaultTemplate folder does not exist')

if os.path.exists(Snippets):
    print('Snippets folder exists')
else:
    raise Exception('Snippets folder does not exist')


print('\nClearing VaultTemplate...')
for f in os.listdir(TemplateVaultFolder):
    if f != '.obsidian':
        path = os.path.join(TemplateVaultFolder, f)
        print('removing: ' + path)
        if (os.path.isfile(path)):
            os.remove(path)
        else:
            shutil.rmtree(path)

print('\nCopying VaultTemplateFolderStructure to VaultTemplate...')
copy_tree(VaultFolderStructureFolder, TemplateVaultFolder)

print('\nCreating folders in VaultTemplate...')
os.mkdir(os.path.join(TemplateVaultFolder, 'Obsidian', 'Templates'))
os.mkdir(os.path.join(TemplateVaultFolder, 'Obsidian', 'Snippets'))

print('\nCopying templates...')
copy_tree(NoteTemplateFolder,
          os.path.join(TemplateVaultFolder, 'Obsidian', 'Templates'))

print('\nCopying snippets...')
copy_tree(Snippets,
          os.path.join(TemplateVaultFolder, 'Obsidian', 'Snippets'))


print('Finished')
