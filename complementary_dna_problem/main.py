def return_dna_complement(dna: str) -> str:
    """given a dna string, return string of complementary pairing"""
    pairing_dict = {"A": "T", "T": "A", "G": "C", "C": "G"}
    complement = ""
    dna = dna.upper()
    for letter in dna:
        if letter not in "ATGC":
            raise ValueError("DNA letter must be either A, T, G, C")
        complement += pairing_dict[letter]
    return complement
    ...
