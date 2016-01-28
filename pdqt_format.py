import os

import glob

for f in glob.glob('*.pdbqt'):
	old=file(f).read().split('\n')
	for i in range(len(old)):
		if old[i].startswith('USER'):
			old[i]=''
		if old[i].startswith('TER'):
			old[i]=''
	new=open(f,'w')
	new.write('\n'.join(old))
	new.close()
