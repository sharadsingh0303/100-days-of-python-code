links = [
    "www.b001.io",
    "www.youtube",
    "www.google.com",
    "www.wikipedia.org"
]


for link in links:
    #print(link.lstrip("w."))
    print(link.removeprefix("www."))