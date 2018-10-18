
import requests
from bs4 import BeautifulSoup

#allow sus to write to csv files
from csv import writer

response = requests.get('https://www.brainyquote.com/topics/motivational')

#will get the webpage and put it in here
soup = BeautifulSoup(response.text, 'html.parser')

quoteBlocks = soup.findAll(class_="bqQt")


#pass in a name of a file and a w because we wan to write to the file
with open('quotes.csv', 'w') as csv_file:
    # writer is the writer we brought in
    csv_writer = writer(csv_file)
    #the variable is set to a list of strings 
    headers = ['Quote', 'Author', 'Link']
    #write a row using writer
    csv_writer.writerow(headers)



    count = 0
    for block in quoteBlocks:
        quote = block.find_all(class_="b-qt")
        qText = block.find(class_='b-qt')
        #if you're getting a heading or a space around the text, replace the new line with a space
        
        #the reason that we get an error at the end is because it is an AJAX request, the page has loaded all of the quotes, thus some returns are listed as NoneType has no attribute 'get_text()'
        qTextSpace = block.find(class_='b-qt').get_text().replace('.', '.\n')

        #get the links
        link = block.find('a')['href']
        count = count + 1
        #select returns a list, so get the list then the text
        author = block.select('.bq-aut')[0].get_text()
        ##life = block.findAll(attrs={'href': "/topics/life"}).get_text()
        # print(count, "Quote: " + qTextSpace, "\n ", link, "\n ", "Author: " + author)
        print(author)
        #for each post we want to write a row
        csv_writer.writerow([ author, link])
