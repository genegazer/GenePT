#!/usr/bin/env python
# coding: utf-8

import io
import pandas as pd

def df_from_genes(file_path):
    with open(file_path, 'r') as f:
        content = f.readlines()

    # Filter the lines that start with #
    header_lines = [x for x in content if x.startswith("#")]

    # If there are no header lines, raise an error
    if not header_lines:
        raise ValueError("No header lines found in file")

    # Check if the file is from Ancestry
    is_ancestry = any("AncestryDNA" in line for line in header_lines)
  
    #you might need to use on_bad_lines='skip' depending on your python/pandas version

    if is_ancestry:
        # Ancestry data format
        headers = ['rsid', 'chromosome', 'position', 'allele1', 'allele2']
        content = [x for x in content if not x.startswith("#")]
        file = io.StringIO("\n".join(content))
        genetic_data = pd.read_csv(file, sep='\t', names=headers, error_bad_lines=False)
  
        # Combine allele1 and allele2 into genotype
        genetic_data['genotype'] = genetic_data['allele1'] + genetic_data['allele2']
        genetic_data.drop(columns=['allele1', 'allele2'], inplace=True)
    else:
        # 23andMe data format
        header_line = header_lines[-1]
        header_line = header_line.replace("#", "").strip()
        headers = header_line.split("\t")
  
        content = [x for x in content if not x.startswith("#")]
        file = io.StringIO("\n".join(content))
        genetic_data = pd.read_csv(file, sep='\t', names=headers, error_bad_lines=False, dtype='unicode')

    return genetic_data


# read the genetic raw data from the text file into a dataframe
genetic_data = df_from_genes('gene.txt')


# read the CSV which has all the 23andMe RSIDs and their associated pub med IDs. 
rsid_pmid_23andme = pd.read_csv('rsid_pmid_23andme.csv')


# Filter the combined DataFrame to keep only rows with count_pmids >= 1
filtered_rsid_pmid = rsid_pmid_23andme[rsid_pmid_23andme['count_pmids'] >= 1]

# Merge the filtered DataFrame with the genetic data DataFrame on the 'rsid' column
merged_data = pd.merge(genetic_data, filtered_rsid_pmid, on='rsid', how='inner')

# merged_data.shape

#this takes only the 4 headers which are used by 23andMe's data format, which is also what the custom GPT uses
merged_data[['rsid', 'chromosome', 'position', 'genotype']].to_csv('data_for_gpt.csv', index=False)

# [Custom Genetics Analysis GPT Model to use 'data_for_gpt.csv'](https://chat.openai.com/g/g-UpAdVFI1R-genept)
