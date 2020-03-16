mkdir interim/filtered

plink2 \
  --vcf /datasets/dsc180a-wi20-public/Genome/vcf/$1 \
  --make-bed \
  --snps-only \
  --maf 0.05 \
  --geno 0.05 \
  --mind 0.15 \
  --recode vcf\
  --out interim/filtered/filtered_$1
  
mv interim/filtered/filtered_$1.vcf interim/filtered/$2