import os
import glob
indicator='docked'
for ligand in glob.glob('*.pdbqt'):
	if ligand!='test.pdbqt' and ligand.startswith('docked')==False:
		lig='ligand='+ligand
		log='log='+ligand.replace('.pdbqt','.log')
		out='out='+indicator+'&'+ligand
		conf=file('conf').read().split('\n')
		for i in range(len(conf)):
			if conf[i].startswith('ligand'):
				conf[i]=lig
			if conf[i].startswith('log'):
				conf[i]=log
			if conf[i].startswith('out'):
				conf[i]=out
		confw=open('conf','w')
		confw.write('\n'.join(conf))
		confw.close()
		os.system('vina --config conf')
		

