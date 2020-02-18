
# Genetics Project

## Usage Instructions

* run.py reads a VCF file, runs PCA on the variants, then plots the eigenvector values with matplotlib.

## Description of Contents

The project consists of these portions:
```
PROJECT
├── .env
├── .gitignore
├── README.md
├── config
│   ├── data-params.json
│   └── test-params.json
├── data
│   ├── log
│   ├── out
│   ├── raw
│   └── temp
├── lib
├── notebooks
│   └── .gitkeep
├── references
│   └── .gitkeep
├── requirements.txt
├── run.py
└── src
    └── etl.py
```

### `src`

* `data_ingest.sh`: Read VCF file with parameters 
* `process.sh`: Run plink2 PCA function on VCF file

### `config`

* `config.json`: Parameters for run.py
 

### `references`

* Data Dictionaries, references to external sources

### `notebooks`

* Work for A2.
