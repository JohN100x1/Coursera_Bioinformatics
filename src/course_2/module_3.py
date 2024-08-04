GENETIC_CODE_MAP = {
    "AAA": "K",
    "AAC": "N",
    "AAG": "K",
    "AAU": "N",
    "ACA": "T",
    "ACC": "T",
    "ACG": "T",
    "ACU": "T",
    "AGA": "R",
    "AGC": "S",
    "AGG": "R",
    "AGU": "S",
    "AUA": "I",
    "AUC": "I",
    "AUG": "M",
    "AUU": "I",
    "CAA": "Q",
    "CAC": "H",
    "CAG": "Q",
    "CAU": "H",
    "CCA": "P",
    "CCC": "P",
    "CCG": "P",
    "CCU": "P",
    "CGA": "R",
    "CGC": "R",
    "CGG": "R",
    "CGU": "R",
    "CUA": "L",
    "CUC": "L",
    "CUG": "L",
    "CUU": "L",
    "GAA": "E",
    "GAC": "D",
    "GAG": "E",
    "GAU": "D",
    "GCA": "A",
    "GCC": "A",
    "GCG": "A",
    "GCU": "A",
    "GGA": "G",
    "GGC": "G",
    "GGG": "G",
    "GGU": "G",
    "GUA": "V",
    "GUC": "V",
    "GUG": "V",
    "GUU": "V",
    "UAA": "",
    "UAC": "Y",
    "UAG": "",
    "UAU": "Y",
    "UCA": "S",
    "UCC": "S",
    "UCG": "S",
    "UCU": "S",
    "UGA": "",
    "UGC": "C",
    "UGG": "W",
    "UGU": "C",
    "UUA": "L",
    "UUC": "F",
    "UUG": "L",
    "UUU": "F",
}
AMINO_ACID_MASS = {
    "G": 57,
    "A": 71,
    "S": 87,
    "P": 97,
    "V": 99,
    "T": 101,
    "C": 103,
    "I": 113,
    "L": 113,
    "N": 114,
    "D": 115,
    "K": 128,
    "Q": 128,
    "E": 129,
    "M": 131,
    "H": 137,
    "F": 147,
    "R": 156,
    "Y": 163,
    "W": 186,
}


def translate_rna(rna: str) -> str:
    """Returns the Amino Acid string from an RNA string."""
    aminos = []
    for i in range(0, len(rna), 3):
        amino_acid = GENETIC_CODE_MAP[rna[i : i + 3]]
        if not amino_acid:
            break
        aminos.append(amino_acid)
    return "".join(aminos)


def reverse_complement_rna(rna: str) -> str:
    """Returns the reverse complement of an RNA pattern."""
    translation_table = str.maketrans("ACGU", "UGCA")
    translated_string = rna.translate(translation_table)
    return translated_string[::-1]


def peptide_encodes(pattern: str, peptide: str) -> list[str]:
    """Returns the substrings in DNA pattern that transcripts to peptide."""
    substrings = []
    rna = pattern.replace("T", "U")
    n, m = len(pattern), len(peptide)
    for i in range(n - 3 * m + 1):
        rna_substring = rna[i : i + 3 * m]
        if peptide == translate_rna(rna_substring):
            substrings.append(pattern[i : i + 3 * m])
        if peptide == translate_rna(reverse_complement_rna(rna_substring)):
            substrings.append(pattern[i : i + 3 * m])
    return substrings


def cyclic_sub_peptide_count(n: int) -> int:
    """Returns the number of sub-peptides in a cyclic peptide of length n."""
    return n * (n - 1)


def linear_sub_peptide_count(n: int) -> int:
    """Returns the number of sub-peptides in a linear peptide of length n."""
    return 1 + n * (n + 1) // 2


def linear_spectrum(peptide: str) -> list[int]:
    """Returns spectrum of a linear peptide."""
    prefix_mass = [0]
    mass = 0
    for amino_acid in peptide:
        mass += AMINO_ACID_MASS[amino_acid]
        prefix_mass.append(mass)
    spectrum = [0]
    for i in range(len(peptide)):
        for j in range(i + 1, len(peptide) + 1):
            spectrum.append(prefix_mass[j] - prefix_mass[i])
    return sorted(spectrum)


def cyclic_spectrum(peptide: str) -> list[int]:
    """Returns spectrum of a cyclic peptide."""
    prefix_mass = [0]
    mass = 0
    for amino_acid in peptide:
        mass += AMINO_ACID_MASS[amino_acid]
        prefix_mass.append(mass)
    spectrum = [0]
    n = len(peptide)
    for i in range(n):
        for j in range(i + 1, len(peptide) + 1):
            spectrum.append(prefix_mass[j] - prefix_mass[i])
            if i > 0 and j < n:
                spectrum.append(
                    prefix_mass[-1] - prefix_mass[j] + prefix_mass[i]
                )
    return sorted(spectrum)


def count_peptides(mass: int) -> int:
    """Return the number of peptides of a given mass."""
    masses = sorted(set(AMINO_ACID_MASS.values()))
    ways = [1] + [0] * mass
    for m in range(mass + 1):
        for amino_mass in masses:
            if m - amino_mass >= 0:
                ways[m] += ways[m - amino_mass]
    return ways[mass]


def cyclo_spectrum(peptide: tuple[int, ...]) -> list[int]:
    """Returns spectrum of a cyclic peptide, given as a mass tuple."""
    prefix_mass = [0]
    mass = 0
    for amino_acid_mass in peptide:
        mass += amino_acid_mass
        prefix_mass.append(mass)
    spectrum = [0]
    n = len(peptide)
    for i in range(n):
        for j in range(i + 1, len(peptide) + 1):
            spectrum.append(prefix_mass[j] - prefix_mass[i])
            if i > 0 and j < n:
                spectrum.append(
                    prefix_mass[-1] - prefix_mass[j] + prefix_mass[i]
                )
    return sorted(spectrum)


def lin_spectrum(peptide: tuple[int, ...]) -> list[int]:
    """Returns spectrum of a linear peptide, given as a mass tuple."""
    prefix_mass = [0]
    mass = 0
    for amino_acid_mass in peptide:
        mass += amino_acid_mass
        prefix_mass.append(mass)
    spectrum = [0]
    for i in range(len(peptide)):
        for j in range(i + 1, len(peptide) + 1):
            spectrum.append(prefix_mass[j] - prefix_mass[i])
    return sorted(spectrum)


def cyclo_peptide_sequencing(spectrum: list[int]) -> list[str]:
    """Returns a list of mass strings corresponding to a peptide."""
    masses = [m for m in spectrum if 0 < m <= 186]  # Highest amino mass is 186

    def expand(peptides: set[tuple[int, ...]]) -> set[tuple[int, ...]]:
        return {p + (mass,) for p in peptides for mass in masses}

    def is_consistent(
        sub_spectrum: list[int], full_spectrum: list[int]
    ) -> bool:
        sub_idx, sub_len = 0, len(sub_spectrum)
        full_idx, full_len = 0, len(full_spectrum)
        while sub_idx < sub_len and full_idx < full_len:
            if sub_spectrum[sub_idx] == full_spectrum[full_idx]:
                sub_idx += 1
            full_idx += 1
        return sub_idx == sub_len

    candidates: set[tuple[int, ...]] = {tuple()}
    final_peptides = set()
    while candidates:
        candidates = expand(candidates)
        remaining = set()
        for peptide in candidates:
            possible = True
            if sum(peptide) == spectrum[-1]:
                if cyclo_spectrum(peptide) == spectrum:
                    final_peptides.add(peptide)
                possible = False
            else:
                linear_spec = lin_spectrum(peptide)
                if not is_consistent(linear_spec, spectrum):
                    possible = False
            if possible:
                remaining.add(peptide)
        candidates = remaining
    return ["-".join(str(x) for x in peptide) for peptide in final_peptides]
