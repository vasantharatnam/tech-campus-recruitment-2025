# Discussion

## Solutions Considered

### Approach 1: Streaming Line-by-Line
- **Description:**  
  Read the log file line-by-line and filter lines that start with the provided date.
- **Pros:**  
  - Simple implementation  
  - Low memory usage (only one line is held in memory at a time)
- **Cons:**  
  - May require scanning the entire file for each query, which could be slow with a 1 TB file

### Approach 2: Binary Search / Indexing
- **Description:**  
  Use the chronological order of logs to perform a binary search or build an index mapping dates to file positions.
- **Pros:**  
  - Faster access for repeated queries once the index is built
- **Cons:**  
  - Increased implementation complexity  
  - Requires extra memory and a preprocessing step

## Final Solution Summary

The final solution employs the **Streaming Line-by-Line** approach. This method:
- Keeps the memory footprint low, which is critical when dealing with a 1 TB file.
- Is straightforward to implement and meets the contest requirements.
- Provides acceptable performance for one-off queries.
  
For scenarios involving frequent queries, the binary search/indexing method could be revisited for improved performance.

## Steps to Run the Project

1. **Prerequisites:**
   - Python 3.x must be installed.
   - Ensure the input log file (e.g., `test_logs.txt`) is placed in the correct location (or update the path in the script).

2. **Running the Script:**
   - Open a terminal and navigate to the project root.
   - Run the command:
     ```bash
     python3 src/extract_logs.py YYYY-MM-DD
     ```
     Replace `YYYY-MM-DD` with the desired date (e.g., `2024-12-01`).

3. **Output:**
   - The script writes the filtered logs to the `output` folder as `output_YYYY-MM-DD.txt`.

4. **Future Improvements:**
   - Implementing an indexing mechanism could reduce query time for repeated requests.
