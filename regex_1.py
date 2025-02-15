"""
Author: Emanuele Bossi
Class: DS 244
Assignment 4: RegEx
Description: complete the provided code.
"""

""" 
For this homework, you will need to write a Python program 
that reads the HTML content of a web page and extracts the 
headlines and summaries of the articles on that page.
"""
import re
from urllib.request import Request, urlopen


def get_headlines(html: str) -> list[str]:
    """Extracts the headlines from the HTML content"""
    h3_pattern = re.compile(r"<h3.*?>\s*<a.*?>(.*?)<\/a>\s*<\/h3>", re.DOTALL)
    return h3_pattern.findall(html)


def get_summaries(html: str) -> list[str]:
    """Extracts the summaries from the HTML content"""
    h3_pattern = re.compile(r"<p>([^<]+)</p>", re.DOTALL)
    return h3_pattern.findall(html)


if __name__ == '__main__':
    url = "https://wolfpaulus.com/posts"
    try:
        request = Request(url)
        request.add_header("User-Agent", "Mozilla/5.0")
        with urlopen(request) as page:
            text = page.read().decode('utf-8')
    except OSError as e:
        print(f"Failed to open {url}", e)
    else:
        for i, headline in enumerate(get_headlines(text), start=1):
            print(f"{i}. {headline}")
        print("\n"+"-"*50+"\n")
        for i, summary in enumerate(get_summaries(text), start=1):
            print(f"{i}. {summary}")
