old_traj = open('CG.lammpstrj', 'r')
tl = old_traj.readlines()
traj = open('CG_reorder.lammpstrj', 'w')
natoms = int(tl[3])
nframes = int(len(tl)/(natoms+9))
head = ['1', '4']
tail = ['6', '8']
CHOL = []
DOPS = []
DOPC = []
tblock = natoms +9
for i in range(0,nframes):
    ai = 0
    CHOL = []
    DOPS = []
    DOPC = []
    for j in range(tblock*i, tblock*i + 9):
        traj.write(tl[j])
    for j in range(tblock*i + 9, tblock*(i+1)):
        vals = tl[j].split()
        if vals[1] == '1':
            DOPC.append(tl[j])
            DOPC.append(tl[j+1])
            DOPC.append(tl[j+2])
            DOPC.append(tl[j+3])
            DOPC.append(tl[j+4])
            DOPC.append(tl[j+5])
        elif vals[1] == '5':
            DOPS.append(tl[j])
            DOPS.append(tl[j+1])
            DOPS.append(tl[j+2])
            DOPS.append(tl[j+3])
            DOPS.append(tl[j+4])
            DOPS.append(tl[j+5])
    ai = 0
    for c in CHOL:
        ai +=1
        vals = c.split()
        nstr = '%s%s' %(ai, c[len(vals[0]):])
        traj.write(nstr)
    for c in DOPC:
        ai +=1
        vals = c.split()
        nstr = '%s%s' %(ai, c[len(vals[0]):])
        traj.write(nstr)
    for c in DOPS:
        ai +=1
        vals = c.split()
        nstr = '%s%s' %(ai, c[len(vals[0]):])
        traj.write(nstr)
