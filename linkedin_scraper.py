from selenium import webdriver
from bs4 import BeautifulSoup
import time, re

# Creating a webdriver instance
driver = webdriver.Chrome()
# Location of local webdriver
# This instance will be used to log into LinkedIn

# Opening linkedIn's login page
driver.get("https://linkedin.com/uas/login")

# waiting for the page to load
time.sleep(6)

# entering username
username = driver.find_element_by_id("username")

# In case of an error, try changing the element
# tag used here.

# Enter Your Email Address
username.send_keys("ivanivic@gmail.com")

# entering password
pword = driver.find_element_by_id("password")
# In case of an error, try changing the element
# tag used here.

# Enter Your Password
pword.send_keys("lozinka1234")		

# Clicking on the log in button
# Format (syntax) of writing XPath -->
# //tagname[@attribute='value']
driver.find_element_by_xpath("//button[@type='submit']").click()
# In case of an error, try changing the
# XPath used here.


# Opening Bill's Profile
# paste the URL of Bill's profile here
profile_url = "https://www.linkedin.com/in/williamhgates"
  
driver.get(profile_url) 

start = time.time()
  
# will be used in the while loop
initialScroll = 0
finalScroll = 3000
  
while True:
    driver.execute_script(f"window.scrollTo({initialScroll}, {finalScroll})")
    # this command scrolls the window starting from
    # the pixel value stored in the initialScroll 
    # variable to the pixel value stored at the
    # finalScroll variable
    initialScroll = finalScroll
    finalScroll += 3000
  
    # we will stop the script for 6 seconds so that 
    # the data can load
    time.sleep(6)
    # You can change it as per your needs and internet speed
  
    end = time.time()
  
    # We will scroll for 40 seconds.
    # You can change it as per your needs and internet speed
    if round(end - start) > 40:
        break

    src = driver.page_source
  
# Now using beautiful soup
soup = BeautifulSoup(src, 'lxml')

# Extracting the HTML of the complete introduction box
# that contains the name, company name, and the location
intro = soup.find('div', {'class': 'pv-text-details__left-panel'})
  
print(intro)

# In case of an error, try changing the tags used here.

name_loc = intro.find("h1")

# Extracting the Name
name = name_loc.get_text().strip()
# strip() is used to remove any extra blank spaces

works_at_loc = intro.find("div", {'class': 'text-body-medium'})

# this gives us the HTML of the tag in which the Company Name is present
# Extracting the Company Name
works_at = works_at_loc.get_text().strip()


location_loc = intro.find_all("span", {'class': 'text-body-small'})

# Getting the HTML of the Experience section in the profile
experience = soup.find("section", {"id": "experience-section"}).find('ul')
  
print(experience)

# In case of an error, try changing the tags used here.

li_tags = experience.find('div')
a_tags = li_tags.find("a")
job_title = a_tags.find("h3").get_text().strip()

print(job_title)

company_name = a_tags.find_all("p")[1].get_text().strip()
print(company_name)

joining_date = a_tags.find_all("h4")[0].find_all("span")[1].get_text().strip()

employment_duration = a_tags.find_all("h4")[1].find_all(
	"span")[1].get_text().strip()

print(joining_date + ", " + employment_duration)

############################################ company info #####################################################################


url=['https://www.linkedin.com/company/meta/about/']

driver.get(url)
    for i in range(max(0,10)): # here you will need to tune to see exactly how many scrolls you need
        driver.execute_script('window.scrollBy(0, 500)')
        sleep(3)
	

data={
    "overview": [],
    "website": [],
    "company_size": [],
    "headquarters": [],
    #"locations":[]
}


src=driver.page_source
soup=BeautifulSoup(src, 'html.parser')

overview = driver.find_elements_by_xpath('//div[@class="ember-view"]')
  


        overview = soup.find('div',{'class':'break-words white-space-pre-wrap mb5 text-body-small t-black--light'}).get_text().strip()
   	website = soup.find('div',{'class':'link-without-visited-state ember-view'}).get_text().strip()
	company_size = soup.find('div',{'class':'text-body-small t-black--light mb1'}).get_text().strip()

	headquarters = soup.find('div',{'class':'mb4 text-body-small t-black--light'}).get_text().strip()
	
print(overview)

driver.close()
