import os
from pgrid import pgrid

cmd = 'bsub -W 48:00 -n 36 -R "rusage[mem=2000]" -R fullnode -oo log_{0}-{1}-{2}.txt python results_psd_with_augmentation.py {0} {1} {2}'

def launch_simulation(sigma, order, sigma_noise):
    os.system(cmd.format(sigma, order, sigma_noise))

grid = pgrid()
for p in grid:
	launch_simulation(*p)