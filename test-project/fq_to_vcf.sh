mkdir -p $3/references
mkdir $4

cp -r $1/* $3/references

bwa mem -R '@RG\tID:fastq1.1\tPU:NA06985.1.SP1\tSM:SP1\tPL:SOLID\tLB:lib1' $3/references/Homo_sapiens_assembly38.fasta $2 > $3/SP1.sam

gatk SortSam -I $3/SP1.sam -O $3/SP1.bam -SORT_ORDER coordinate -CREATE_INDEX true

gatk MarkDuplicates -I $3/SP1.bam -I $3/SP1.bam -O $3/SP1.dedup.bam \
-METRICS_FILE SP1.dedup.metrics.txt \
-REMOVE_DUPLICATES false \
-TAGGING_POLICY All

gatk CreateSequenceDictionary -R $3/references/Homo_sapiens_assembly38.fasta -O $3/references/Homo_sapiens_assembly38.dict

samtools index $3/SP1.dedup.bam

gatk HaplotypeCaller -R $3/references/Homo_sapiens_assembly38.fasta -I $3/SP1.dedup.bam -O $4/SP1.vcf.gz

