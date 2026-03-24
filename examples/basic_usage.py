#!/usr/bin/env python3
"""Basic usage example for cli-tool."""

import subprocess
import sys

def run_cli_tool(args):
    """Run cli-tool with given arguments."""
    cmd = ['cli-tool'] + args
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(f"Output: {result.stdout}")
        return result.returncode
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}", file=sys.stderr)
        return e.returncode

if __name__ == '__main__':
    # Example 1: Process a file
    print("Example 1: Processing file")
    run_cli_tool(['process', '--input', 'sample.txt', '--output', 'out.txt'])
    
    # Example 2: Analyze with verbose mode
    print("\nExample 2: Analyzing with verbose mode")
    run_cli_tool(['analyze', '--verbose', '--threshold', '0.8'])
