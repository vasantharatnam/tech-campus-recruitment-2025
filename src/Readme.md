# Source Directory

Make sure that your source code is in the `src` directory.


# Source Code
This folder contains the source code for the log extraction project.

## Files

- **extract_logs.py:**  
  The main Python script that:
  - Accepts a date argument in the format `YYYY-MM-DD`
  - Reads the log file line-by-line
  - Filters and extracts log entries that match the specified date
  - Saves the extracted logs to the output folder

## How to Run

1. **Prepare the Log File:**
   - Ensure your log file (e.g., `test_logs.txt`) is available.  
     If you prefer to keep it in a different location, update the file path in `extract_logs.py` accordingly.

2. **Execute the Script:**
   - Open a terminal in the project root.
   - Run the script with:
     ```bash
     python3 src/extract_logs.py YYYY-MM-DD
     ```
   - Replace `YYYY-MM-DD` with the date you wish to query.

3. **Output:**
   - The extracted logs will be saved in the `output` folder as `output_YYYY-MM-DD.txt`.

## Dependencies

- Python 3.x
