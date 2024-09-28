#!/bin/bash

base_dir="/home/maulanmi/using-git/data"
output_dir="/home/maulanmi/using-git/RBS_output"

mkdir -p "$output_dir"

for filename in "$base_dir"/*/GCA*; do
    fna_file=$(find "$filename" -name "*.fna")

    if [[ -f "$fna_file" ]]; then
        base_name=$(basename "$fna_file" .fna)
        # Define the output file paths
        output_file="$output_dir/${base_name}_output.fna"

	python gene_finder_with_RBS.py "$fna_file" > "$output_file"
	echo "done"
    fi
done
