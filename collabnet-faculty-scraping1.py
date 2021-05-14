import bs4
from urllib.request import Request, urlopen as uReq
from bs4 import BeautifulSoup as soup

# https://www.youtube.com/watch?v=XQgXKtPSzUI

my_url = 'https://csc.calpoly.edu/faculty/'
# print(my_url)

# opening up connection, grabbing up page
req = Request(my_url, headers={'User-Agent': 'Chrome/51.0.2704.103'})
u_client = uReq(req)
page_html = u_client.read()
u_client.close()

page_soup = soup(page_html, "html.parser")
# print(page_soup.h1)

#which is the name of the box that contains all the info we need
#grabs each product
containers = page_soup.findAll("div", {"class" :"elementor-element elementor-element-ad8beb3 elementor-widget elementor-widget-text-editor"})
# print(len(containers))
# print(containers[0])

container = containers[0]
all_info = container.div.div.table.tbody
# print(len(all_info))
# print(all_info.tr.findAll("td"))
# # print(container.div.div.table.tbody.tr)
# tag = container.div.div.table.tbody.tr.findAll("td")
# print("\n")
# print(tag[0].text)
# print(tag[1].text)
# print(tag[2].text)
# print("\n")

# #to csv
filename = "faculty_info_cp.csv"
f = open(filename, "w")
headers = "Name, Email\n"
f.write(headers)

for i in all_info:
    infos = i.findAll("td")
    name_faculty_member = infos[0].text
    email_faculty_member = infos[1].text
    # office_faculty_member = infos[2].text
    f.write(name_faculty_member + ", " + email_faculty_member + "\n")

f.close()