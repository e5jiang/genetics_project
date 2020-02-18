import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import sys


if __name__ == "__main__":
    args = sys.argv
    if args[1] == 'data-test':
        os.system('chmod 700 src/data_ingest.sh')
        os.system('./src/data_ingest.sh')
    
    if args[2] == 'process':
        os.system('chmod 700 src/process.sh')
        os.system('./src/process.sh')
    
    cfg = json.load(open('config/config.json'))
    #read in eigenvector file and save scatter plot of values
    vectors = pd.read_csv(cfg['eigenvectors'], delimiter=' ', names=['loc1','loc2','x','y'])
    plt.scatter(vectors['x'], vectors['y'], s=2)
    plt.savefig(cfg['plotdir'])
