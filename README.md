# Article-Fetcher

This Python script fetches PubMed articles related to fetch articles related on AI/ML/DL.
## Purpose
The script searches PubMed for relevant articles, extracts metadata (PubMed ID, title, abstract, URL), and saves results to an Excel file.

## Requirements
- Python 3.x
- Libraries: `biopython`, `pandas` (`pip install biopython pandas`)
- A valid email for NCBI Entrez API access
- Optional: NCBI API key for higher request limits

## Usage
1. Update the `Entrez.email` field with your email.
2. Optionally, add your NCBI API key.
3. Run the script: `python fetch_pubmed_articles.py`
4. Results are saved 
