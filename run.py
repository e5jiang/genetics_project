import json
import sys
from etl import *


if __name__ == "__main__":
    args = sys.argv
    env = json.load(open('../config/env.json'))
    
    os.chdir(args[1])

    data_params = json.load(open('../config/data-params.json'))

    chmod_files()

    build_vcf(data_params, env)

    filter_rename(data_params)

    build_pca(data_params)
    
    plot_pca(env)

