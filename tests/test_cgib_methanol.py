import pytest
from mscg.cli import cgib

def test_2s(datafile):
    
    dfs = cgib.main(
        top     = datafile("methanol_1728_2s.data"),
        traj    = datafile("methanol_1728_2s.trr,frames=500"),
        names   = 'CH3,OH',
        cut     = 10.0,
        pair    = ['CH3,CH3,min=2.8,max=10.0,bins=200', 'CH3,OH,min=2.8,max=10.0,bins=200', 'OH,OH,min=2.5,max=10.0,bins=200'],
        bond    = ['CH3,OH,min=1.35,max=1.65,bins=60'],
        verbose = 0,
        save    = 'return'
    )
        
    print("")
    
    benchmarks = [
        [-0.35198275, -0.35789919, -0.370159, -0.3777962,  -0.37918443, -0.37901999, -0.37652943, -0.36803416, -0.36553039, -0.36208924],
        [-0.1904293, -0.16301842, -0.13927964, -0.11312445, -0.09150904, -0.06571954, -0.04184394, -0.0217612,  -0.00566529,  0.0096957],
        [0.64323166,  0.62145166, 0.6097216, 0.57885123, 0.55916755, 0.52626581, 0.50684728,  0.48196789, 0.44785871, 0.42115728],
        [4.61175648e-04, 2.03246518e-02, 6.00428379e-02, 1.08651735e-01, 1.82962576e-01, 2.62147215e-01, 3.59980819e-01, 4.74724111e-01, 6.07295276e-01, 7.32176752e-01]
    ]
    
    for i in range(4):
        d = dfs[i]['data'][30:40,2]
        #print(','.join([str(_) for _ in d[:10]]))
        
        for j in range(10):
            assert abs(d[j]-benchmarks[i][j])<0.001