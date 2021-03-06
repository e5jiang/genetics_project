import json
import sys
from src.etl import *


if __name__ == "__main__":
    args = sys.argv
    data_params = json.load(open('config/data-params.json'))

    os.chdir(args[1])

    chmod_files()

    build_vcf(data_params)

    filter_rename(data_params)

    build_pca(data_params)
    
    plot_pca()

    with open("../config/env.json", "r") as f:
        env = json.load(f)

    env['output-paths'] = ['test-project/outputs/SP1.vcf.gz', 'test-project/outputs/pca.png']

    with open("../config/env.json", "w") as f:
        json.dump(env, f)



