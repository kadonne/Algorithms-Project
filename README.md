# Algorithms Project: Password Cracker Optimization

A comparative analysis of data structure performance for password cracking operations using Python. This project benchmarks Dictionary, Trie Tree, and Self-Balancing Tree implementations to evaluate their efficiency in insertion, searching, and sorting operations.

## Overview

This project implements and compares three different data structures for cracking SHA-256 hashed passwords through brute force dictionary attacks. The password patterns follow common conventions: dictionary words combined with symbols and digits (e.g., `password!5`, `football3@`).

## Team Members

* **Ammar**: Dictionary implementation (author of `decrypt.py`, `3D_parse.py`, and `make_data.py`)
* **Dan**: Trie Tree data structure implementation
* **Kailey**: Self-Balancing Tree implementation

## Project Structure

```
Algorithms-Project/
├── decrypt.py                 # Dictionary-based password cracker
├── make_data.py               # Test data generator
├── 3D_parse.py                # Results visualization script
├── words-original.txt         # Original wordlist (140,000+ English words)
├── words.txt                  # Generated test wordlist (filtered)
├── encrypted_passwords.txt    # SHA-256 hashed passwords to crack
└── decrypted_passwords.txt    # Output file with cracked passwords
```

## Features

### Data Structure Implementations

1. **Dictionary (Hash Table)**: Fast O(1) average lookup time
2. **Trie Tree**: Prefix-based search structure
3. **Self-Balancing Tree**: Maintains sorted order with O(log n) operations

### Password Patterns

The cracker tests two common password patterns:
* `word + symbol + digit` (e.g., `hello!5`)
* `word + digit + symbol` (e.g., `hello5!`)

Supported symbols: `! @ # $ % ^ & * ( ) { } | : ; [ ] ? >`  
Supported digits: `0-9`

### Memory Management

The dictionary implementation processes passwords in batches of 20 million hashes to optimize RAM usage, comparing and clearing the cache periodically.

## Requirements

```
Python 3.x
hashlib (standard library)
time (standard library)
random (standard library)
math (standard library)
sys (standard library)
```

## Usage

### 1. Generate Test Data

Create sample wordlists and encrypted passwords for testing:

```bash
python make_data.py  
```

**Parameters:**
* `sample_size`: Total number of words to generate
* `size_factor`: Number of sampling segments

**Example:**
```bash
python make_data.py 10000 5
```

This generates:
* `words.txt`: Filtered wordlist for testing
* `encrypted_passwords.txt`: SHA-256 hashed passwords to crack

### 2. Run Password Cracker

Execute the dictionary-based cracker:

```bash
python decrypt.py
```

**Output:**
* `decrypted_passwords.txt`: Contains cracked passwords in format: `<hash> <password>`
* Console output showing timing metrics:
  ```
  Insert time:    X.XXXXXXs
  Search time:    X.XXXXXXs
  Sort time:      X.XXXXXXs
  ```

### 3. Visualize Results

Generate 3D performance graphs from trie tree results:

```bash
python 3D_parse.py
```

## Algorithm Details

### Dictionary Implementation (decrypt.py)

**Hash Generation:**
1. Reads words from `words.txt`
2. Generates all combinations of `word + symbol + digit` and `word + digit + symbol`
3. Hashes each combination using SHA-256
4. Stores in dictionary with hash as key, password as value

**Search Process:**
1. Sorts the generated hash dictionary
2. Uses binary search to find matches with target hashes
3. Processes in 20-million hash batches to manage memory
4. Writes successful matches to output file

**Performance Metrics:**
* **Insert time**: Time to generate and store password hashes
* **Search time**: Time to find matches using binary search
* **Sort time**: Time to sort the hash dictionary

## Performance Comparison

The project measures three key metrics across all data structures:

| Metric | Description |
|--------|-------------|
| **Insertion** | Time to generate and store password hashes |
| **Search** | Time to locate target hashes in the structure |
| **Sorting** | Time to organize data (where applicable) |

Results are documented and visualized in 3D graphs showing the relationship between data structure choice, operation type, and performance.

## Security Note

⚠️ **Educational Purpose Only**

This project is designed for educational purposes to understand:
* Data structure performance characteristics
* Algorithmic complexity in real-world scenarios
* SHA-256 hashing and password security concepts

**Do not use this tool for:**
* Unauthorized access to systems
* Cracking passwords without explicit permission
* Any illegal activities

Always follow ethical guidelines and legal requirements when working with security tools.

## Limitations

* Only cracks passwords matching specific patterns (word + symbol + digit)
* Requires significant computational resources for large wordlists
* Memory-intensive for dictionary and tree implementations
* Single-threaded execution (multiprocessing commented out)

## Future Improvements

* [ ] Implement multiprocessing for parallel hash generation
* [ ] Add support for additional password patterns
* [ ] Optimize memory usage in tree implementations
* [ ] Add GPU acceleration for hash computation
* [ ] Implement rainbow table support
* [ ] Add configuration file for customizable parameters

## License

Educational project - check with repository owner for usage terms.

## Acknowledgments

Original wordlist sourced from common English dictionary collections.
