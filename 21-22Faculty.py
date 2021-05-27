import bs4
from urllib.request import Request, urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://catalog.calpoly.edu/facultyandstaff/#facultystaffemeritustext'

# opening up connection, grabbing up page
req = Request(my_url, headers={'User-Agent': 'Chrome/51.0.2704.103'})
u_client = uReq(req)
page_html = u_client.read()
u_client.close()

page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("table", {
    "class":"tbl_facdir"
})

container = containers[0]
all_info = container.findAll("tr")

#to csv without position
filename = "all_faculty_info_cp_without_position.csv"
f = open(filename, "w")
headers = "LastName, FirstName, Course\n"
f.write(headers)

name_course = all_info[1].td.text
name_course_split = name_course.split(")")
name_faculty = name_course_split[1].split("(")
f.write(name_faculty[0].lstrip() + "," + name_course_split[2] + "\n")
for i in all_info[2:]:
    name_course = i.td.text
    name_course_split = name_course.split(")")
    name_faculty = name_course_split[0].split("(")
    f.write(name_faculty[0].lstrip() + "," + name_course_split[1] + "\n")

f.close()

# to csv with position
filename2 = "all_faculty_info_cp_with_position.csv"
f2 = open(filename2, "w")
headers2 = "LastName, FirstName, Course, Position\n"
f2.write(headers2)

for i in all_info[2:]:
    name_course = i.td.text
    name_course_split = name_course.split(")")
    name_faculty = name_course_split[0].split("(")
   
    get_stuff = i.findAll("td")
    f2.write(name_faculty[0] + ", " + name_course_split[1] + ", " + get_stuff[1].text + "\n")

f2.close()
