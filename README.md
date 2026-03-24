# CLI Tool

This is a simple CLI tool with command-line argument support.

## New Features

- Added greeting function: `greet_user` that returns a personalized greeting.
- Added command-line argument parsing using `argparse`.

## Usage

Run the tool with optional arguments:

```bash
python main.py [--name NAME] [--verbose]
```

### Arguments

- `--name`, `-n`: Name to greet (default: 'World')
- `--verbose`, `-v`: Enable verbose output

### Examples

```bash
python main.py
# Output: Hello World

python main.py --name Alice
# Output: Hello Alice

python main.py --name Bob --verbose
# Output:
# Verbose mode: Greeting Bob
# Hello Bob
```
