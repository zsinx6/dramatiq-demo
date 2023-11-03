import httpx


def count_words(url):
    response = httpx.get(url)
    count = len(response.text.split(" "))
    print(f"There are {count} words at {url!r}.")
