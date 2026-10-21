"""Read a single-record FASTA file and print its DNA reverse complement."""

import argparse
from pathlib import Path


_BASES = "ACGTRYMKBDHVNacgtrymkbdhvn"
_COMPLEMENTS = "TGCAYRKMVHDBNtgcayrkmvhdbn"
_COMPLEMENT_TABLE = str.maketrans(_BASES, _COMPLEMENTS)
_VALID_BASES = set(_BASES)


def read_fasta_sequence(path):
    """Return the concatenated sequence from a single-record FASTA file."""
    sequence_lines = []
    found_header = False

    with open(path, encoding="utf-8") as fasta_file:
        for line_number, line in enumerate(fasta_file, start=1):
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                if found_header:
                    raise ValueError("expected a single-record FASTA file")
                found_header = True
            elif not found_header:
                raise ValueError(
                    f"expected a FASTA header ('>') before sequence at line {line_number}"
                )
            else:
                sequence_lines.append("".join(line.split()))

    if not found_header:
        raise ValueError("no FASTA header found")
    return "".join(sequence_lines)


def reverse_complement(seq):
    """Return the reverse complement of a DNA sequence."""
    seq = "".join(seq.split())
    invalid_bases = sorted(set(seq) - _VALID_BASES)
    if invalid_bases:
        raise ValueError(f"unsupported base(s): {''.join(invalid_bases)}")
    return seq.translate(_COMPLEMENT_TABLE)[::-1]


def main():
    parser = argparse.ArgumentParser(
        description="Print the reverse complement of a single-record FASTA file."
    )
    parser.add_argument("input", type=Path, help="input FASTA file")
    args = parser.parse_args()

    try:
        print(reverse_complement(read_fasta_sequence(args.input)))
    except (OSError, UnicodeError, ValueError) as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()