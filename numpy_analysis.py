import numpy as np
from fetch import fetch_gene_record
from translate import get_cds_sequence



def sequence_to_array(seq):
    """
    Converts a DNA sequence (string-like) into a NumPy array of single characters.
    e.g. "ATGC" -> array(['A', 'T', 'G', 'C'])
    """
    return np.array(list(str(seq)))

def base_composition(seq_array):
    """
    Counts A, T, G, C using vectorized comparisons instead of .count() calls.
    """
    counts = {
        "A": np.sum(seq_array == "A"),
        "T": np.sum(seq_array == "T"),
        "G": np.sum(seq_array == "G"),
        "C": np.sum(seq_array == "C"),
    }
    return counts

def sliding_gc_content(seq_array, window_size=30):
    """
    Computes GC% in non-overlapping windows across the sequence.
    Returns a NumPy array of GC% values, one per window.
    """
    is_gc = np.isin(seq_array, ["G", "C"])  # True/False array, same length as sequence

    num_windows = len(seq_array) // window_size
    gc_percentages = []

    for i in range(num_windows):
        window = is_gc[i * window_size : (i + 1) * window_size]
        gc_percent = np.mean(window) * 100  # % of True values in this window
        gc_percentages.append(gc_percent)

    return np.array(gc_percentages)

if __name__ == "__main__":
    accession = "NM_000546"  # TP53
    record = fetch_gene_record(accession)
    cds_seq = get_cds_sequence(record)

    seq_array = sequence_to_array(cds_seq)

    print("Sequence length:", len(seq_array))

    composition = base_composition(seq_array)
    print("Base composition:", composition)

    gc_percent_overall = (composition["G"] + composition["C"]) / len(seq_array) * 100
    print(f"Overall GC%: {gc_percent_overall:.2f}%")

    gc_windows = sliding_gc_content(seq_array, window_size=30)
    print("\nGC% per 30-base window:")
    print(gc_windows)

    print("\nHighest GC window:", np.max(gc_windows), "%")
    print("Lowest GC window:", np.min(gc_windows), "%")
    print("Average across windows:", np.mean(gc_windows), "%")

    from visualize import plot_sliding_gc
    plot_sliding_gc(gc_windows, window_size=30, gene_name="TP53")