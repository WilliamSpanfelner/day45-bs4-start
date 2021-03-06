from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

#get the title of each article listed
articles = soup.find_all(name="a", class_="titlelink")

article_titles = []
article_links = []

for article_title in articles:
    title = article_title.getText()
    article_titles.append(title)
    link = article_title.get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

print(article_titles)
print(article_links)
print(article_upvotes)

#Get the maximum value from the article_upvotes list and use it to determine its index value,
# which can be use to retrieve the corresponding elements in the other lists.
max_vote_count = max(article_upvotes)
max_vote_count_index = article_upvotes.index(max_vote_count)

print(article_titles[max_vote_count_index])
print(article_links[max_vote_count_index])

# max_votes = 0
# for index in range(0, len(article_upvotes)):
#     if article_upvotes[index] > max_votes:
#         max_votes = article_upvotes[index]
#         i = index
#
# print(max_votes, i)
# print(article_titles[i], article_links[i])



# article_titles = soup.find_all(name="a", class_="titlelink")
# for title in article_titles:
#     print(title.getText())










# with open("website.html", "r") as file:
#     contents = file.read()
#
# # After creating an instance of BeautifulSoup using the html.parser,
# soup = BeautifulSoup(contents, "html.parser")
#
# # HTML tags can be accessed and the content they contain with dot notation:
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
#
# # The first anchor element in the html document can be accessed like so:
# print(soup.a)
#
# # The entire document can be printed plain or prettified
# print(soup)
# print(soup.prettify())
#
# # If all the instances of a particular type of element is required, the find_all method can help.
# all_a_elements = soup.find_all(name="a")
# print(all_a_elements)
#
# all_paragraph_tags = soup.find_all(name="p")
# print(all_paragraph_tags)
#
# # Use the getText() method to return the content text (e.g. for anchor tags)
# for tag in all_a_elements:
#     print(tag.getText())
#
# # Use the get() method to return the value of any attribute (e.g. href)
# for tag in all_a_elements:
#     print(tag.get("href"))
#     # prints all the target http links
#
# # Use the find method to return the first item that matches specified criteria
# # e.g. element name and id values
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# # Similarly, finding elements with a specific class name is done like so.
# # The class keyword requires an underscore suffix since its normal HTML use is for assigning a name.
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)
# print(section_heading.name)
# print(section_heading.getText())
# print(section_heading.get("class"))
#
# # Use CSS selectors to get specific information like a company url
# company_url = soup.select_one(selector="p a")
# print(company_url)
# print(company_url.get("href"))
#
# # CSS selectors can also be use to retrieve id values -
# # the id key must be prefixed with #
# name = soup.select_one(selector="#name")
# print(name)
# print(name.getText("id"))
#
# # CSS selectors can be use to create a list of items with a common class name for instance.
# headings = soup.select(".heading")
# print(headings)
