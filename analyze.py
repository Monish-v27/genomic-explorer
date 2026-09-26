import pandas as pd
from fetch import fetch_gene_record
from translate import get_cds_sequence, translate_cds_to_protein

def build_gene_dataframe(accession_list):
    """
    Fetches, translates, and summarizes multiple genes into a single DataFrame.
    """
    rows = []

    for acc in accession_list:
        try:
            record = fetch_gene_record(acc)
            cds_seq = get_cds_sequence(record)

            if cds_seq is None:
                print(f"No CDS found for {acc}. Skipping.")
                continue

            protein_seq = translate_cds_to_protein(cds_seq)
            gc_count = cds_seq.count("G") + cds_seq.count("C")
            gc_percent = (gc_count / len(cds_seq)) * 100

            rows.append({
                "accession": acc,
                "gene_name": record.annotations.get("organism", "Unknown"),
                "description": record.description,
                "cds_length": len(cds_seq),
                "protein_length": len(protein_seq),
                "gc_content": gc_percent,
                "protein_seq": str(protein_seq)
            })

            print(f"Processed: {acc}")

        except Exception as e:
            print(f"Failed on {acc}: {e}")

    df = pd.DataFrame(rows)
    return df

if __name__ == "__main__":
    accessions = ["NM_000546", "NM_007294", "NM_005228", "NM_002467", "NM_000518"]
    df = build_gene_dataframe(accessions)

    print(df)
    df.to_csv("data/gene_summary.csv", index=False)
    print("\nSaved to data/gene_summary.csv")