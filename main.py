import tkinter as tk
from tkinter import ttk
import requests
from bs4 import BeautifulSoup
import logging
import os

# Configure logging
logging.basicConfig(filename="extractor.log", level=logging.ERROR,
                    format="%(asctime)s - %(levelname)s - %(message)s")

def extract_text():
    """Extracts text from the entered URLs and displays it in the text area."""
    urls = text_entry.get("1.0", tk.END).splitlines()
    extracted_text = ""
    progress_bar["value"] = 0  # Reset progress bar
    progress_bar["maximum"] = len(urls)  # Set max value

    for i, url in enumerate(urls):
        try:
            response = requests.get(url)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, "html.parser")
            text = soup.find_all(text=True)
            cleaned_text = " ".join(t for t in text if t.strip() and not t.parent.name in ["style", "script"])

            extracted_text += f"\n--- {url} ---\n{cleaned_text}\n"

        except requests.exceptions.RequestException as e:
            extracted_text += f"Error accessing {url} (Request Exception): {e}\n"
            logging.error(f"Error accessing {url}: {e}")
        except BeautifulSoup.BeautifulSoupError as e:
            extracted_text += f"Error parsing {url} (Parsing Error): {e}\n"
            logging.error(f"Error parsing {url}: {e}")
        finally:
            progress_bar["value"] += 1
            root.update_idletasks()  # Update progress bar visually

    text_area.delete("1.0", tk.END)
    text_area.insert(tk.END, extracted_text)

def save_to_file():
    """Saves the extracted text to a file."""
    file_path = tk.filedialog.asksaveasfilename(
        defaultextension=".txt", 
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(text_area.get("1.0", tk.END))

# Create main window
root = tk.Tk()
root.title("Website Text Extractor")

# Text entry for URLs
text_entry_label = ttk.Label(root, text="Enter URLs (one per line):")
text_entry_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
text_entry = tk.Text(root, height=5, width=50)
text_entry.grid(row=1, column=0, padx=5, pady=5)

# Extract button
extract_button = ttk.Button(root, text="Extract Text", command=extract_text)
extract_button.grid(row=2, column=0, padx=5, pady=5)

# Progress bar
progress_bar = ttk.Progressbar(root, mode="determinate")
progress_bar.grid(row=3, column=0, padx=5, pady=5, sticky="ew")

# Text area for displaying extracted text
text_area_label = ttk.Label(root, text="Extracted Text:")
text_area_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
text_area = tk.Text(root, wrap=tk.WORD, height=20, width=50)
text_area.grid(row=5, column=0, padx=5, pady=5)

# Save to File button
save_button = ttk.Button(root, text="Save to File", command=save_to_file)
save_button.grid(row=6, column=0, padx=5, pady=5)


root.mainloop() 
