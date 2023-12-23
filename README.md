# Project Title: GenePT Analysis Tool

## Introduction
GenePT is a tool designed to offer simple yet insightful genetic data analysis. This tool combines the power of GPT with a bit of bioinformatics to provide users with personalized insights into their commercially available genetic data.

The custom GPT is available here: [GenePT](https://chat.openai.com/g/g-UpAdVFI1R-genept)

If you'd like to use the pre-filtered file of my genetics data it is available in the file `data_for_gpt.csv`

## Preparing Your Genetic Data
Ensure your genetic data is in a CSV format with columns: "rsid", "chromosome", "position", and "genotype". The provided pandas code is designed to reduce the size of the raw genetic data to a size which is easy for the sandboxed GPT code analysis features to perform operations.

The `genetics_gpt_pandas.py` file contains the necessary scripts. I've included a copy of my own genetics titled 'my_23andme_data.txt' if you would like to try this tool without using personal genetic data and 'rsid_pmid_23andme.csv' has the data to filter the raw genetics data. 

This script has also been made into a web app available at [yrusad.com/gene_to_pmid](https://yrusad.com/gene_to_pmid)

## Running the Analysis

- Use the `df_from_genes` function to parse your genetic data file. The script will automatically handle AncestryDNA, or 23andMe data.
- Then read the filter's CSV file, and merge that with the raw genetic data.
- Finally, output the columns 'rsid', 'chromosome', 'position', and 'genotype' to a new CSV which can be used easily by GPT. This should reduce the raw 15mb text file to about a 1mb in CSV format. 

## Getting Insights
For best results use the starting prompt, "Could you take a look at my raw genetic data?" Then, in the next prompt upload the formatted CSV of genetic data.

After this, GPT will use pandas to look at the data, hopefully only taking a few seconds. After this, prompt GPT with questions about your genetic data.

The GPT can find specific polymorphisms: "Please tell me if I have the MTHFR c677t polymorphism."

GPT can also find polymorphisms based on a biochemical system: "Would you check for any common, well studied polymorphisms in serotonin or dopamine receptors?"

Or look for changes based on a specific disease: "Would you check for risks of heart disease?"

## Important Reminder
GenePT is not a substitute for professional medical advice. This tool is entirely for educational and entertainment purposes.
