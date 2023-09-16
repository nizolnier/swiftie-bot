import requests
from bs4 import BeautifulSoup
import re


def getSongContent(url, album):
    try:
        output = []
        # get the html code from the given url
        # for this implementation make the url the link to a given album
        # url = 'https://genius.com/albums/Migos/Culture-ii'
        response = requests.get(url)
        html = response.content
        # make use of the BeautifulSoup library for scraping through lxml
        soup = BeautifulSoup(html, 'lxml')
        souper = BeautifulSoup(html, 'html.parser')
        title = souper.find('title').contents[0]
        counter = 0

        # from inspection of html I know the lyrics are in 'Lyrics__Contaier', so find these div classes and extract the lyrics
        for tag in soup.select('div[class^="Lyrics__Container"], .song_body-lyrics p'):
            t = tag.get_text("\n", strip=True)
            t = re.sub('\[.*\]', '', t)
            print(counter)
            print(t)
            counter += 1

        return html
    except Exception as e:
        print(e)


def albumGetSongLinks(url):
    try:
        output = []
        # get the html code from the given url
        # for this implementation make the url the link to a given album
        # url = 'https://genius.com/albums/Migos/Culture-ii'
        response = requests.get(url)
        html = response.content
        # make use of the BeautifulSoup library for scraping through html
        soup = BeautifulSoup(html, features="html.parser")
        souper = BeautifulSoup(html, 'html.parser')
        album = souper.find('title').contents[0]

        # this list will hold the links to all songs in the given album
        songLinks = []
        # from inspection of html I know links to songs are in div with class
        # 'chart_row-content', so find these div classes and extract the links in them
        data = soup.findAll('div', attrs={'class': 'chart_row-content'})
        for div in data:
            # get the link in the div class
            links = div.findAll('a')
            # save the link into a data structure
            for a in links:
                songLinks.append(a['href'])

        for link in songLinks:
            o = getSongContent(link, album)
            output.append(o)

        print(output)
        return output
    except Exception as e:
        print(e)


def getAlbums(url):
    output = []

    # standard method of using BeautifulSoup class
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html, features="html.parser")

    # from inspection the album links are all in <a> with class = "album_link"
    data = soup.findAll('a', {'class': 'album_link'})

    eras = ["/albums/Taylor-swift/Speak-now-taylors-version",
            "/albums/Taylor-swift/Red-taylors-version",
            "/albums/Taylor-swift/1989-deluxe",
            "/albums/Taylor-swift/Reputation",
            "/albums/Taylor-swift/Folklore-deluxe-version",
            "/albums/Taylor-swift/Fearless-taylor-s-version",
            "/albums/Taylor-swift/Taylor-swift",
            "/albums/Taylor-swift/Midnights-3am-edition",
            "/albums/Taylor-swift/Lover",
            "/albums/Taylor-swift/Evermore-deluxe-version"
            ]

    # fromat each href and add it to list of links
    for link in data:
        if link['href'] in eras:
            output.append("https://genius.com" + link['href'])

    return output

    # Purpose - this method will search all songs by a given artist to determine the list of
    # songs on which the keyword appears in
    # Param - url - the link to the artist page on Genius
    # Param - word - the keyword to search for


def getSongs(url):
    output = []

    # first find the list of albums for the artist
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html, features="html.parser")

    link = None
    # from inspection of artist page the link to page with all albums in div
    # with class of 'u-quarter_top_margin. Retrieve the link in this div
    divs = soup.findAll('div', attrs={'class': 'u-quarter_top_margin'})
    for div in divs:
        links = div.findAll('a')
        for a in links:
            link = "https://genius.com" + a['href']
            print(link)

        # pass link to helper method to get the list of album links
    albumLinks = getAlbums(link)

    # then pass each album url
    for link in albumLinks:
        output.extend(albumGetSongLinks(link))

    return output
