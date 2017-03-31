# Below is a link to a 10-day weather forecast at weather.com
# Use urllib and BeautifulSoup to scrape data from the weather table.
# Print a brief synopsis of the weather for the next 10 days.
# Include the day, date, high temp, low temp, and chance of rain.
# You can customize the text as you like, but it should be readable
# for the user.  You will need to target specific classes or other
# attributes to pull some parts of the data.
# (e.g.  Wednesday, March 22: the high temp will be 48 with a low of 35, and a 20% chance of rain). (25pts)
import urllib.request
from bs4 import BeautifulSoup

url = "https://weather.com/weather/tenday/l/USIL0225:1:US"
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page.read(), "html.parser")

#print(soup.prettify())

weather_list = [[[z.text.strip() for z in y.findAll("span",{"class":"date-time"})] for y in x.findAll("td", {"class":"twc-sticky-col"})] for x in soup.findAll("table", {"class":"twc-table"})]
#print(weather_list)


better_list = []
for i in range(len(weather_list[0])):
    if (i+1)%2 == 0:
        better_list.append(weather_list[0][i])
better_list = [x[0] for x in better_list]
#print(better_list)

temp_list = [[[z.text.strip() for z in y.findAll("span")] for y in x.findAll("td", {"class":"temp"})] for x in soup.findAll("table", {"class":"twc-table"})]
#print(temp_list)

high_list = []
low_list = []
for i in range(len(temp_list[0])):
    high_list.append(temp_list[0][i][0])
    low_list.append(temp_list[0][i][2])
#print(high_list)
#print(low_list)

for i in range(len(better_list)):
    print("The forecast for", better_list[i], "is a high of", high_list[i], "and a low of", low_list[i])