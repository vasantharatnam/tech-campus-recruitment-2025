# src/extract_logs.py
import sys
import os

def extract_logs(date, input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as infile, \
             open(output_file, 'w', encoding='utf-8') as outfile:
            for line in infile:
                # Only process lines that start with the provided date
                if line.startswith(date):
                    outfile.write(line)
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
        sys.exit(1)
    except Exception as e:
        print(f"Error processing file: {e}")
        sys.exit(1)

def main():
    # Validate that exactly one argument is provided (the date)
    if len(sys.argv) != 2:
        print("Usage: python extract_logs.py YYYY-MM-DD")
        sys.exit(1)

    date = sys.argv[1]


    # Update the path to where your input file is located
    input_file = "test_logs.txt"  # This assumes the file is in the same directory as this script
    
    # Check if the input file exists before proceeding
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found.")
        sys.exit(1)
    
    # Ensure the output directory exists
    output_dir = "../output"  # Adjust path if needed
    os.makedirs(output_dir, exist_ok=True)
    
    output_file = os.path.join(output_dir, f"output_{date}.txt")
    
    print(f"Extracting logs for {date}...")
    extract_logs(date, input_file, output_file)
    print(f"Logs for {date} have been saved to {output_file}")

if __name__ == "__main__":
    main()
