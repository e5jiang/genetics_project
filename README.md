
# Genetics Project

## Usage Instructions

* run.py reads a FASTQ file, converts it to VCF, runs PCA on the variants, then plots the eigenvector values with seaborn.
* Code will create 'interim' and 'outputs' directories in the 'test-project' folder, where intermediate and output files of the code will go. 
* NOTE: in `env.json` the `docker-image` there are double quotes around `latest`, but they are escaped characters in the json format. Please note if copy-pasting. 

## Description of Content

### `config`

* `data-params.json`: Parameters for run.py 
* `env.json`: docker image path and output path

### `notebooks`

* Work for A3.

### `test-project`

* `filter_vcf.sh`: filter vcf with parameters
* `fq_to_vcf.sh`: convert FASTQ to VCF format
* `vcf_to_pca.sh`: run PLINK2 PCA function

### `etl.py`
* functions for the code

### `run.py`
* code to run pipeline
