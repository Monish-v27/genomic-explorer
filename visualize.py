import pandas as pd
import matplotlib.pyplot as plt

def load_data(csv_path):
    """
    Loads the gene summary CSV into a DataFrame.
    """
    df = pd.read_csv(csv_path)
    return df

def plot_gc_content(df):
    """
    Bar chart of GC% per gene.
    """
    plt.figure(figsize=(8, 5))
    plt.bar(df["accession"], df["gc_content"], color="steelblue")
    plt.xlabel("Gene (Accession)")
    plt.ylabel("GC Content (%)")
    plt.title("GC Content by Gene")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("data/gc_content.png")
    plt.show()

def plot_protein_length(df):
    """
    Bar chart of protein length per gene.
    """
    plt.figure(figsize=(8, 5))
    plt.bar(df["accession"], df["protein_length"], color="darkorange")
    plt.xlabel("Gene (Accession)")
    plt.ylabel("Protein Length (amino acids)")
    plt.title("Protein Length by Gene")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("data/protein_length.png")
    plt.show()

if __name__ == "__main__":
    df = load_data("data/gene_summary.csv")
    print(df)

    plot_gc_content(df)
    plot_protein_length(df)

def plot_sliding_gc(gc_windows, window_size=30, gene_name="Gene"):
    """
    Line chart of GC% across sliding windows of a single gene.
    """
    positions = [i * window_size for i in range(len(gc_windows))]

    plt.figure(figsize=(10, 5))
    plt.plot(positions, gc_windows, color="green", marker="o", markersize=3)
    plt.xlabel("Position in CDS (base pairs)")
    plt.ylabel("GC Content (%)")
    plt.title(f"Sliding Window GC Content: {gene_name}")
    plt.axhline(y=gc_windows.mean(), color="gray", linestyle="--", label="Average")
    plt.legend()
    plt.tight_layout()
    plt.savefig("data/sliding_gc_tp53.png")
    plt.show()