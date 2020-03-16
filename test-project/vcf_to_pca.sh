mkdir interim/pca
mkdir interim/merged

bcftools concat interim/filtered/$1 interim/filtered/$2 -o interim/merged/merged.vcf -O v
plink2 --vcf interim/merged/merged.vcf --pca 2 --out interim/pca/merged_pca