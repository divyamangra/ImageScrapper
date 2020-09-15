import mechanize, os
from bs4 import BeautifulSoup as Soup
url=input("enter url:")
browser = mechanize.Browser()
browser.set_handle_equiv(True)
browser.set_handle_redirect(True)
browser.set_handle_referer(True)
browser.set_handle_robots(False)
browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
html = browser.open(url)
browser.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
print(browser.geturl())
soup = Soup(html,"html.parser")

image_tags = soup.findAll('img')
i=0
for image in image_tags:
    i=i+1
    filename = image['src']
    print(filename)
    filename = os.path.join(os.getcwd(), str(i))
    data = browser.open(image['src']).read()
    savename=(str(i)+'.jpg')
    save = open(savename, 'wb')
    save.write(data)
    save.close()
