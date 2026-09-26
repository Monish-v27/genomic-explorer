# Genomic Variant & Expression Explorer

A small end-to-end data pipeline that fetches real gene sequences from NCBI, 
translates coding regions into proteins, computes sequence-level statistics, 
and visualizes the results — built as a hands-on project to practice core 
Python data tools (web APIs, NumPy, Pandas, Matplotlib) using bioinformatics 
as the working domain.

## What it does

1. **Fetch** — pulls GenBank records for a list of genes directly from NCBI 
   using Biopython's Entrez API
2. **Translate** — extracts the coding sequence (CDS) from each record and 
   translates it into a protein sequence
3. **Analyze** — computes GC content, protein length, and other summary 
   statistics across genes; aggregates everything into a Pandas DataFrame 
   and saves it as CSV
4. **Visualize** — generates bar charts comparing genes, and a NumPy-powered 
   sliding-window GC-content plot that reveals how GC content varies across 
   a single gene (rather than one flat average)

## Genes included by default

TP53, BRCA1, EGFR, MYC, HBB

## Project structure
