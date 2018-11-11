from bs4 import BeautifulSoup
import urllib2
import re

url = "https://questionnaire-148920.appspot.com/swe/data.html"

content = urllib2.urlopen(url).read()

soup = BeautifulSoup(content)

#print soup.prettify()
#print soup.contents[0].name
dataset_salary = soup.findAll('td', "player-salary")
#print dataset_salary[0]

sum = 0
numberofsalaries = len(dataset_salary)
average = 0
for i in range(0,len(dataset_salary)):
    stringer = dataset_salary[i].renderContents().replace("$", "").replace(",", "")
    stringer = re.sub("\D", "", stringer)

    if not stringer:
        continue
    #if dataset_salary[i].renderContents()==" ":
    #    continue
    else:
        sum = sum+int(stringer)
    print sum

average = sum/numberofsalaries
print "This is the average salary of a player:"
print average
#print soup.findAll('td', "player-salary")[0].renderContents()
#print soup.findAll('td', "player-salary")[1].renderContents()
#print soup.findAll('td', "player-salary")[2].renderContents()
#print soup.findAll('td', "player-salary")[3].renderContents()

#print soup.title
#print soup.title.string
#print soup.p
