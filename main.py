#!/usr/bin/env python3
import argparse

def greet_user(name):
    return f"Hello {name}"

def main():
    parser = argparse.ArgumentParser(description='A simple CLI tool with argument support.')
    parser.add_argument('--name', '-n', default='World', help='Name to greet')
    parser.add_argument('--verbose', '-v', action='store_true', help='Enable verbose output')
    args = parser.parse_args()
    
    greeting = greet_user(args.name)
    if args.verbose:
        print(f"Verbose mode: Greeting {args.name}")
    print(greeting)

if __name__ == "__main__":
    main()
