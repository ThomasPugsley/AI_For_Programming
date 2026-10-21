# AI for Programming

This repository contains programming exercises and analysis notes. The
`copilot_practical/` directory includes small Python scripts for working with
DNA sequences; they use only the Python standard library.

## DNA utilities

- `scripts/gc_content.py` reports GC content for each record in a FASTA file,
  rounded to two decimal places. Empty records are skipped with a warning.
- `scripts/reverse_complement.py` prints the reverse complement of a
  single-record FASTA file.
- `translate.py` translates a DNA sequence entered at the prompt into a protein
  sequence.

Run the scripts from the repository root with Python 3:

```sh
python3 copilot_practical/scripts/gc_content.py copilot_practical/input/multi_seq.fasta
python3 copilot_practical/scripts/gc_content.py --min-gc 50 copilot_practical/input/multi_seq.fasta
python3 copilot_practical/scripts/reverse_complement.py copilot_practical/input/test_seq.fasta
python3 copilot_practical/translate.py
```

`--min-gc` prints only records whose GC percentage is strictly greater than
the supplied threshold (0–100).
