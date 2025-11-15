#!/bin/bash
# This script sets up the environment for Day 2 of AI Engineering

# How many CSV files exist in the entire project directory (including subdirectories)?

NUM_CSV_FILES=$(find . -name "*.csv" | wc -l)
echo "Number of CSV files in the project directory: $NUM_CSV_FILES"

# What is the total number of data samples across ALL CSV files? (Each line represents one data sample, excluding the header line in each file)
TOTAL_SAMPLES=$(find . -name "*.csv" -exec wc -l {} + | sed '1d' |awk '{sum += $1} END {print sum}')
echo "Total number of data samples across all CSV files: $TOTAL_SAMPLES"

#Which single CSV file contains the most data samples?
MAX_SAMPLES_FILE=$(find . -name "*.csv" -exec wc -l {} + | sort -nr | sed '1d' | head -n 1)
echo "CSV file with the most data samples: $MAX_SAMPLES_FILE"

# how many total lines are there in all processed files combined?
TOTAL_PROCESSED_LINES=$(cat processed/* | wc -l)
echo "Total number of lines in all processed files combined: $TOTAL_PROCESSED_LINES"

#FINAL:
TOTAL=$((NUM_CSV_FILES *100 + TOTAL_PROCESSED_LINES + TOTAL_SAMPLES))
echo "Final calculated total: $TOTAL"