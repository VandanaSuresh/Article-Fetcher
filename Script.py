from Bio import Entrez
import pandas as pd
import time

# Set your email (mandatory)
Entrez.email = "setyourmail@gmail.com"  # Replace with your actual email if needed

# Optional: Add your NCBI API key for higher request limits
# Entrez.api_key = "your_ncbi_api_key"

# Search terms based on your query
search_terms = [
    "Machine Learning in xxxxx",
    "Deep Learning in xxxxxxx",
    "Artificial Intelligence in xxxxxx "
]

# Max articles per search term
max_articles = 50

all_articles = []

for term in search_terms:
    # Construct query with additional context for query
    query = f"{term} AND (	search term)"
    print(f"Searching for: {query}")

    # Search PubMed
    handle = Entrez.esearch(db="pubmed", term=query, retmax=max_articles)
    record = Entrez.read(handle)
    handle.close()

    pmids = record['IdList']
    print(f"Found {len(pmids)} articles for '{term}'")

    for pmid in pmids:
        try:
            time.sleep(0.3)  # Polite delay to avoid overwhelming the server
            fetch_data = Entrez.read(Entrez.efetch(db="pubmed", id=pmid, rettype="xml"))

            article = fetch_data['PubmedArticle'][0]
            title = article['MedlineCitation']['Article']['ArticleTitle']
            url = f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"

            all_articles.append({
                "Search Term": term,
                "PubMed ID": pmid,
                "Title": title,
                "URL": url
            })

        except Exception as e:
            print(f"Error fetching {pmid}: {e}")

# Save all articles to Excel
df = pd.DataFrame(all_articles)
df.to_excel("file.xlsx", index=False)

print("✅ Done! Articles saved to 'file.xlsx'")