# GC Content Script

`gc_content.py` takes a FASTA file path and reads all sequence records in the file, including multiline sequences. For each non-empty record, it prints the FASTA header and GC content as a percentage rounded to two decimal places. Empty sequences are skipped with a warning.

The optional `--min-gc <float>` argument filters the output to records whose GC percentage is strictly greater than the given threshold. The threshold must be between 0 and 100. Without this option, all non-empty records are reported.
