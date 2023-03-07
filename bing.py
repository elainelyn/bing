import requests
from bs4 import BeautifulSoup

# Specify the search query and the number of search results
query = "panda"
num_results = 10

url = f"https://www.bing.com/search?q={query}&count={num_results}"

# Send an HTTP request to get the content of the search results page
response = requests.get(url)

# Parse the content of the search results page and extract the URL of each search result
soup = BeautifulSoup(response.text, "html.parser")
results = soup.select("li.b_algo h2 a")

# Iterate through the URLs of each search result, send an HTTP request to get the content of each web page
for result in results:
    title = result.get_text()
    url = result["href"]
    print(f"Title: {title}")
    print(f"URL: {url}")
    print("Content:")

    response = requests.get(url)
    page_content = response.text

    # Parse the content of each web page and extract the text content
    soup = BeautifulSoup(page_content, "html.parser")
    page_text = soup.get_text()
    print(page_text)
    print()