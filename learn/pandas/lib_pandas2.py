#only for html tables
#pip install lxml
import pandas as pd
import ssl

ssl._create_default_https_context = ssl._create_unverified_context #fixes potential errors

scraper = pd.read_html("https://en.wikipedia.org/wiki/Comparison_of_Linux_distributions")

for idx, table in enumerate(scraper):
    pass
    #print("********************************")
    #print(idx)
    #print(table)
    
#print(scraper)
print(scraper[3])
