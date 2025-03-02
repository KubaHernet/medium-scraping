import sys

from scraping.output import dump_to_file
import scraping.main as scraping

def default():
    print(sys.argv)
    
    results = scraping.scrape(int(sys.argv[1]))
    dump_to_file(results)