"""Calculate GC content for each sequence in a FASTA file."""

import argparse
import sys
from pathlib import Path


def read_fasta_records(path):
    """Yield (header, sequence) pairs from a multi-record FASTA file."""
    header = None
    sequence_lines = []

    with Path(path).open(encoding="utf-8") as fasta_file:
        for line_number, line in enumerate(fasta_file, start=1):
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                if header is not None:
                    yield header, "".join(sequence_lines)
                header = line
                sequence_lines = []
            elif header is None:
                raise ValueError(
                    f"expected a FASTA header ('>') before sequence at line {line_number}"
                )
            else:
                sequence_lines.append("".join(line.split()))

    if header is not None:
        yield header, "".join(sequence_lines)


def main():
    parser = argparse.ArgumentParser(
        description="Print GC content for every sequence in a FASTA file."
    )
    parser.add_argument("input", type=Path, help="input FASTA file")
    parser.add_argument(
        "--min-gc",
        type=float,
        default=None,
        metavar="FLOAT",
        help="only print records with GC content strictly above this threshold",
    )
    args = parser.parse_args()

    if args.min_gc is not None and not 0 <= args.min_gc <= 100:
        parser.error("--min-gc must be between 0 and 100")

    try:
        records = read_fasta_records(args.input)
        found_record = False
        for header, sequence in records:
            found_record = True
            if not sequence:
                print(f"Warning: skipping empty sequence for {header}", file=sys.stderr)
                continue
            gc_count = sum(base.upper() in {"G", "C"} for base in sequence)
            gc_percent = gc_count / len(sequence) * 100
            if args.min_gc is None or gc_percent > args.min_gc:
                rounded_gc_percent = round(gc_percent, 4)
                print(f"{header}: {rounded_gc_percent:.4f}%")
        if not found_record:
            parser.error("no FASTA records found")
    except (OSError, UnicodeError, ValueError) as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
