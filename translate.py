from Bio import SeqIO
from fetch import fetch_gene_record

def get_cds_sequence(record):
    """
    Finds the CDS feature in a GenBank record and returns just that slice of DNA.
    """
    for feature in record.features:
        if feature.type == "CDS":
            cds_seq=feature.extract(record.seq)
            return cds_seq
    return None

def translate_cds_to_protein(cds_seq):
    """
    Translates a CDS DNA sequence into a protein sequence.
    """
    protein_seq=cds_seq.translate(to_stop=True)
    return protein_seq

if __name__ == "__main__":
    accession = "NM_000546"
    record = fetch_gene_record(accession)

    cds_seq = get_cds_sequence(record)
    print("CDS length:", len(cds_seq))
    print("CDS first 60 bases:", cds_seq[:60])

    protein_seq = translate_cds_to_protein(cds_seq)
    print("Translated protein:", protein_seq)