# from linkedin_scraper import Person, actions
# from selenium import webdriver
# driver = webdriver.Chrome()
#
# # email = "some-email@email.address"
# # password = "password123"
# actions.login(driver) # if email and password isnt given, it'll prompt in terminal
# person = Person("https://www.linkedin.com/in/parthsh", driver=driver)


from linkedin_scraper import JobSearch, actions
from selenium import webdriver

driver = webdriver.Chrome()

actions.login(driver) # if email and password isnt given, it'll prompt in terminal
input("Press Enter")
job_search = JobSearch(driver=driver, close_on_complete=False, scrape=False)
# job_search contains jobs from your logged in front page:
# - job_search.recommended_jobs
# - job_search.still_hiring
# - job_search.more_jobs

job_listings = job_search.search("Data Engineer BFSI") # returns the list of `Job` from the first page