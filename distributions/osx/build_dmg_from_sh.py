import os
import sys

about = {}
with open("mindsdb/__about__.py") as fp:
    exec(fp.read(), about)
version = about['__version__']

with open('distributions/osx/dmg_from_sh/src/mindsdb.installer.sh.template', 'r') as fp:
    content = fp.read()
with open('distributions/osx/dmg_from_sh/src/mindsdb.installer.sh', 'w') as fp:
    fp.write(content)

os.system('cd distributions/osx/dmg_from_sh/src && chmod +x build_macos_installer.sh && ./build_macos_installer.sh')

if sys.argv[1] == 'beta':
    prefix = '_Beta'
elif sys.argv[1] == 'release':
    prefix = None

new_names = []
original_name = None
for filename in os.listdir('distributions/osx/dmg_from_sh/build'):
    if '.dmg' in filename:
        new_names = filename
        versioned_filename = filename.replace('.dmg', f'{prefix}.dmg')
        latest_filename = filename.split('_v')[0] + f'{prefix}_Latest.dmg'
        new_names.append(versioned_filename, latest_filename)

for new_name in new_names:
    os.system(f'cp distributions/osx/dmg_from_sh/build/{filename} distributions/osx/dist/{new_name}')
