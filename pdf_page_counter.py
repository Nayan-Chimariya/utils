import PyPDF2
import os
import glob
from colorama import Fore, Back, Style

total_pages = 0

os.getcwd()

for file in glob.glob("*.pdf"):
    pdfs = PyPDF2.PdfReader(file)
    total_pages += len(pdfs.pages)

print (Fore.GREEN + f"\nTotal Pages: " + Fore.YELLOW + f"{total_pages}")
