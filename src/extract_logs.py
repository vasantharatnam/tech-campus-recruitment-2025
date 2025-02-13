# src/extract_logs.py
import sys
import os

def extract_logs(date, input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as infile, \
             open(output_file, 'w', encoding='utf-8') as outfile:
            for line in infile:
                if line.startswith(date):
                    outfile.write(line)
    except Exception as e:
        print(f"Error processing file: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print("Usage: python extract_logs.py YYYY-MM-DD")
        sys.exit(1)

    date = sys.argv[1]
    input_file = "test_logs.txt"  # Update path if your log file is elsewhere
    
    # Ensure the output directory exists
    output_dir = "../output"  # Adjust path if needed
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, f"output_{date}.txt")

    print(f"Extracting logs for {date}...")
    extract_logs(date, input_file, output_file)
    print(f"Logs for {date} have been saved to {output_file}")

if __name__ == "__main__":
    main()
