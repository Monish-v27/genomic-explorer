from Bio import Entrez, SeqIO
Entrez.email = "monishsuni@gmail.com"

def fetch_gene_record(accession_id):
    """
    Fetches a Genbank record from NCBI, which includes CDS (coding region) information.
    """
    handle = Entrez.efetch(db="nucleotide", id=accession_id, rettype="gb", retmode="text")
    record = SeqIO.read(handle, "genbank")
    handle.close()
    return record

if __name__ == "__main__":
    accession = "NM_000546"
    gene_record = fetch_gene_record(accession)

    print("ID:", gene_record.id)
    print("Description:", gene_record.description)
    print("Sequence length:", len(gene_record.seq))

    for feature in gene_record.features:
        if feature.type == "CDS":
            print("Found CDS feature:")
            print("CDS location:", feature.location)
            print("CDS qualifiers:", feature.qualifiers)