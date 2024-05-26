import requests
from bs4 import BeautifulSoup
from text_gen import gpt_summarize

def scrapeRedditPostByURL(url):
    # Step 1: Fetch the webpage content
    res = requests.get(url)

    if res.status_code == 200:
        content = res.text
    else:
        print(f"Failed to retrieve the webpage. Status code: {res.status_code}")
        return None

    # Step 2: Parse the HTML content
    soup = BeautifulSoup(content, 'html.parser')

    # Step 3: Extract specific data
    # Extract the title from elements with id containing/starting with 'post-title'
    title_element = soup.find(lambda tag: tag.name and tag.has_attr('id') and tag['id'].startswith('post-title'))
    title = title_element.get_text() if title_element else 'No Title Found'

    # Function to extract paragraphs within specific tags
    def extract_paragraphs(tag_name):
        paragraphs = []
        for tag in soup.find_all(tag_name):
            for p in tag.find_all('p'):
                paragraphs.append(p.get_text())
        return paragraphs

    # Extract paragraphs from <shreddit-post> and <shreddit-comment>
    post_paragraphs = extract_paragraphs('shreddit-post')

    # Return the data as a dictionary
    return {
        'title': title,
        'post_paragraphs': post_paragraphs,
    }


def polish(data):
    print(data)
