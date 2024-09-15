# Website Text Extractor

This Python script uses Tkinter for a GUI interface to extract text content from multiple websites simultaneously. It leverages the `requests` and `BeautifulSoup` libraries to fetch and parse HTML content.

## Features

* **Multiple Website Extraction:** Enter URLs (one per line) in the text box and extract content from all of them.
* **Progress Bar:** Visualizes the extraction process, showing the progress for each website.
* **Error Handling:** Provides informative error messages for network issues or parsing problems, and logs them to a file.
* **Text Cleaning:** Basic HTML tag removal to improve output readability.
* **Save to File:** Option to save the extracted text to a file (e.g., .txt).
* **User-Friendly GUI:** Built using Tkinter for an easy-to-use interface.


## Usage

1. **Clone the Repository:**
   ```bash
   git clone <repository_url>
   ```

2. **Install Dependencies:**
   ```bash
   pip install requests beautifulsoup4
   ```

3. **Run the Script:**
   ```bash
   python website_extractor.py 
   ```

4. **Enter URLs:** 
   In the text box, paste the URLs of the websites you want to extract content from, one URL per line.

5. **Click "Extract Text":** The script will fetch and parse the content, displaying the extracted text in the output area.
6. **Save to File (Optional):** Click "Save to File" to save the extracted text to a file.

## Example

**Input (URLs in the text box):**

```
https://www.example.com
https://www.anotherwebsite.org
```

**Output (in the text area):**

```
--- https://www.example.com ---
<extracted text from example.com>

--- https://www.anotherwebsite.org ---
<extracted text from anotherwebsite.org>
```

## Improvements

* **Advanced Text Cleaning:** Improve the text cleaning by adding options for removing specific elements or applying more sophisticated text formatting.
* **Error Handling & Logging:** Enhance error handling and logging for better debugging capabilities. 
* **Configuration Options:** Allow users to customize settings like the number of concurrent requests or the output file format.
* **Website-Specific Parsing:** Add logic to handle specific website structures or extract data from elements with unique attributes.


## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, feel free to open an issue or submit a pull request.


## Disclaimer

* Please respect websites' terms of service and robots.txt files. Avoid excessive scraping or overloading websites with requests.
* This script is for educational and personal use. Use it responsibly. 
