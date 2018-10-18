from bs4 import BeautifulSoup

html_doc = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>My Webpage</title>
</head>
<body>
    <div id="section-1">
        <h3 data-hello="hi">Hello</h3>
        <img src="https://source.unsplash.com/200x200/?nature,water
        " alt="">
        <p>
            Lorem ipsum dolor sit, amet consectetur adipisicing elit. Ullam explicabo minima suscipit natus illum illo quidem placeat quis nihil, omnis labore consectetur nisi esse voluptatum sapiente nostrum ab accusantium neque dolore qui, repellendus consequuntur? Vero, porro. Alias adipisci suscipit reiciendis.
        </p>
    </div>
    <div id="section-2">
        <ul class="items">
            <li class="item"><a href="#">Item 1</a></li>
            <li class="item"><a href="#">Item 2</a></li>
            <li class="item"><a href="#">Item 3</a></li>
            <li class="item"><a href="#">Item 4</a></li>
            <li class="item"><a href="#">Item 5</a></li>
        </ul>
    </div>
</body>
</html>
"""
#create a variable called beautiful and set it to Beautiful Soup, the first parameter will be what to scraped (what to scrape=local variable, second parameter)
soup = BeautifulSoup(html_doc, 'html.parser')

# Direct
# below prints everything between the body tags, head tags, and the title
#print({soup.body, soup.head, soup.head.title})

#will just print the first div found

#find one or findAll (can use camelCase or underscore_method)
el = soup.find('div')
#the below gives us a list with the content in []'s
el2 = soup.findAll('div')
#lists function just as array's in javaScript, subsequently the below would give us the second div
el3 = soup.findAll('div')[1]

#can;'t use class, have to use class_
# el4 = soup.find({id='section-1',class_='items'})
el4 = soup.find(id='section-1')
el5 = soup.find(class_='items')
# attrs indicates the attribute that refers to the h3 as specified, set the key pair to what is expressed in the html portion of the document
el6 = soup.find(attrs={"data-hello": "hi"})


#select
#will always return the data inside of a list(aka a jS array)
el7 = soup.select('#section-1')
# to get the data outside of a list, use bracket notation
el8 = soup.select('#section-1')[0]

el9 = soup.select('.item')[0]


#get_text
# to just gt the text without thte html

el10 = soup.find(class_='item').get_text()
# OR loop through
#for item in soup.select('.item'):
 #   print(item.get_text())

# print(el10)


#NAVIGATION
# will preface the output with a "new-line"
#elem = soup.body.contents
#will get the image
el = soup.body.contents[1].contents[1].next_sibling.next_sibling
#will bypass the new line and get the actual eleent
elem = soup.body.contents[1].contents[1].find_next_sibling()

elem2 = soup.find(id='section-2').find_previous_sibling()

elem3 = soup.find(class_='item').find_parent()

elem4 = soup.find('h3').find_next_sibling('p')
print(elem4)
