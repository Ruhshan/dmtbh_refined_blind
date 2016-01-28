import os
import glob
indicator='docked'
completed=open("completed.txt","w")
clist=file("completed.txt").read().split()
for ligand in glob.glob('*.pdbqt'):
	if ligand not in clist and ligand.startswith('docked')==False:
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
		os.system('./vina --config conf')
		completed=open("completed.txt","a")
		completed.write(ligand+'\n')
		completed.close()
		

