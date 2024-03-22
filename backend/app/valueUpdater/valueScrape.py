from bs4 import BeautifulSoup
import requests

def crape_data():
    print("herer--->")
    url = 'https://snowtrace.io'  # Replace with the actual URL
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
    
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the div with class 'text-right'
    div = soup.findAll('div', class_='text-right')
    print(div)