import pytest 
from mscg.cli.cgkmc import *

def test_cgkmc(datafile):
    cluster = CG_cluster()
    cluster.beta = 1
    cluster.gamma = 1

    cluster.read_trajectory(datafile("test_a.pdb"), datafile("rmsfit_test_a.xtc"))
    cluster.calculate_rmsf()

    cluster.initialize_labels(10)
    cluster.optimize_chi_square(filename = "test", max_steps=1000, output_interval=1000)
