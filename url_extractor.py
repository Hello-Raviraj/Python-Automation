import requests
import re
url = "http://testphp.vulnweb.com/"
x =  requests.get(url)
word = "https"
if word in x.text:
    # Extract all href links using regex
    links = re.findall(r'href=["\'](http[s]?://[^"\']+)', x.text)
    unique_links = list(set(links))
    # Save links to file
    f = open("url.txt", "w")
    for link in unique_links:
        f.write(link + "\n")
    f.close()

    print("✅ Links saved to url.txt")
else:
    print("❌ Keyword not found in page")

       
