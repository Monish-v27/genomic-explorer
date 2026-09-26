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
genomic_explorer/
├── fetch.py # NCBI data fetching (Biopython/Entrez)
├── translate.py # CDS extraction + DNA-to-protein translation
├── analyze.py # Pandas aggregation, GC% calculation, CSV export
├── visualize.py # Matplotlib charts
├── numpy_analysis.py # NumPy-based sliding-window GC content analysis
├── data/ # Output CSVs and charts
└── requirements.txt


## Setup

```bash
python -m venv venv
venv\Scripts\activate      # Windows
pip install -r requirements.txt
```

## Usage

```bash
python analyze.py            # fetch, translate, and summarize genes
python visualize.py           # generate comparison charts
python numpy_analysis.py       # sliding-window GC analysis for a single gene
```

## Example output

- `data/gene_summary.csv` — table of gene stats (GC%, protein length, etc.)
- `data/gc_content.png` — GC% comparison across genes
- `data/protein_length.png` — protein length comparison across genes
- `data/sliding_gc_tp53.png` — GC% variation across TP53's coding sequence

## Tools used

Python, Biopython, NumPy, Pandas, Matplotlib, NCBI Entrez API

## Notes

Built as a learning project to practice real-world data pipeline patterns: 
fetching from an external API, transforming/cleaning data, structured 
analysis, and visualization — organized into single-responsibility modules.
