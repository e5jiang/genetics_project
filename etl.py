import os
import pandas as pd
import seaborn as sb 
import matplotlib.pyplot as plt

def chmod_files():
    os.system('chmod 700 fq_to_vcf.sh')
    os.system('chmod 700 filter_vcf.sh')
    os.system('chmod 700 vcf_to_pca.sh')

def build_vcf(params, env):
    os.system('./fq_to_vcf.sh '+params['fasta-path']+' '+params['fastq-path']+' '+params['imterim-path']+' '+env['output-paths'])

def filter_rename(params):
    os.system('./filter_vcf.sh '+params['vcf-paths'][0]+' '+params['renames'][0])
    os.system('./filter_vcf.sh '+params['vcf-paths'][1]+' '+params['renames'][1])

def build_pca(params):
    os.system('./vcf_to_pca.sh '+params['renames'][0]+' '+params['renames'][1])

def plot_pca(env):
    vectors = pd.read_csv('interim/pca/merged_pca.eigenvec',delimiter=' ', names=['first','id','x','y'])
    vectors = vectors.drop(columns=['first'])

    igsr = pd.read_csv('igsr_samples.tsv',delimiter='\t')
    igsr = igsr[['Sample name', 'Superpopulation code']].rename(columns={'Sample name': 'id', 'Superpopulation code':'code'})

    combined = vectors.set_index('id').join(igsr.set_index('id'), how='inner')

    fig, ax = plt.subplots(figsize=(10,8))
    pca_plot = sb.scatterplot(x="x", y="y", hue="code", ax=ax, data=combined)
    plt.savefig(env['output-paths']+'/pca.png')
