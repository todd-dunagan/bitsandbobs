import os
from bs4 import BeautifulSoup

def strip_html_from_file(file_path):
    try:
        # Attempt to open and read the file
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            
            # Parse the content and strip HTML
            soup = BeautifulSoup(content, 'html.parser')
            text_only = soup.get_text()

        # Optionally, write the stripped content back to the file or another file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(text_only)

    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except PermissionError:
        print(f"Permission denied: {file_path}")
    except Exception as e:
        # Catch any other exception and print the error message
        print(f"Error reading {file_path}: {e}")


def strip_html_from_directory(directory):
    # Loop through each file in the given directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Check if it's a file (ignore directories)
        if os.path.isfile(file_path):
            strip_html_from_file(file_path)
            print(f"Stripped HTML from: {file_path}")

# Replace 'your_directory' with the directory containing your files
directory = '/Users/todd/Library/Mobile Documents/iCloud~md~obsidian/Documents/dunagan'
strip_html_from_directory(directory)