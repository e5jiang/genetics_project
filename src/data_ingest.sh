mkdir -p data/interim

plink2 \
  --vcf /datasets/dsc180a-wi20-public/Genome/vcf/sample/chr22_test.vcf.gz \
  --make-bed \
  --snps-only \
  --maf 0.09 \
  --geno 0.05 \
  --mind 0.1 \
  --recode \
  --out data/interim/sample-chr22

