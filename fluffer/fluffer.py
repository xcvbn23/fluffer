from pathlib import Path
import requests
from bs4 import BeautifulSoup
import xml.etree.cElementTree as ET

from slugify import slugify

root = ET.Element("source", type="hn")

def hn_plugin(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')

        comments = [
            soup.find_all('div', class_='comment'),
        ]

        extracted_text = []
        for elements in comments:
            for element in elements:
                text = element.get_text(strip=True)
                if text:
                    extracted_text.append(text)
                    ET.SubElement(root, "comment", name="blah").text = text

        full_text = '\n'.join(extracted_text)

        title = soup.title.text
        title = slugify(title)

        return full_text, title

    except requests.RequestException as e:
        print(f"Error extracting text: {e}")
        return None

def extract(url) -> None:
    website_text, title = hn_plugin(url)

    output_directory = Path("output")
    output_directory.mkdir(parents=True, exist_ok=True)

    tree = ET.ElementTree(root)
    path = output_directory / f"{title}.xml"  
    tree.write(path.resolve())

    path = output_directory / f"{title}.txt"  
    path.write_text(website_text)
