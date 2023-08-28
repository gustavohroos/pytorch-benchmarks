#!/bin/bash

batch_sizes="1 4 8 16 32"

for j in {0..10}; do
    for index in {0..12}; do
        for batch_size in $batch_sizes; do
            python3 orchestrator.py --index $index --batch-size $batch_size
        done
    done
done