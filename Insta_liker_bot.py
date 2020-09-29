from tkinter import*
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

win = Tk()
win.resizable(width = False, height = False)
win.title("Insta_liker_bot")
win.iconbitmap("myicon.ico")

User_label = Label(win, text = "Username:")
User_label.grid(row = 0, column = 0, padx = 5, pady = 5)

Pass_label = Label(win, text = "Password:")
Pass_label.grid(row = 1, column = 0, padx = 5, pady = 5)

User_entry = Entry(win, width = 30)
User_entry.grid(row = 0, column = 1, padx = (0,5))

Pass_entry = Entry(win, width = 30)
Pass_entry.grid(row = 1, column = 1, padx = (0,5))

target_label = Label(win, text = "Target ID:")
target_label.grid(row = 2, column = 0, padx = 5, pady = 5)

target_entry = Entry(win , width = 30)
target_entry.grid(row = 2, column = 1, padx = (0,5))

time_label = Label(win, text = "Interval:")
time_label.grid(row = 3, column = 0, padx = 5, pady = 5)

time_entry = Entry(win , width = 30)
time_entry.grid(row = 3, column = 1, padx = (0,5))
time_entry.insert(0, '5')

def clicked():
	driver = webdriver.Chrome("chromedriver.exe")
	driver.get("https://www.instagram.com")

	try:
	    element = WebDriverWait(driver, 100).until(
	        EC.presence_of_element_located((By.NAME, "username"))
	    )
	    element.send_keys(User_entry.get())

	    element2 = WebDriverWait(driver, 100).until(
	        EC.presence_of_element_located((By.NAME, "password"))
	    )
	    element2.send_keys(Pass_entry.get())
	    element2.send_keys(Keys.RETURN)

	    notnow1 = WebDriverWait(driver, 100).until(
	        lambda x: x.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div/div/button")
	    )
	    notnow1.click()

	    notnow2 = WebDriverWait(driver, 100).until(
	        lambda x: x.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
	    )
	    notnow2.click()

	    instasearch = WebDriverWait(driver, 100).until(
	        lambda x: x.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/input")
	    )
	    instasearch.send_keys(target_entry.get())
	    instasearch.send_keys(Keys.RETURN)

	    searchresult = WebDriverWait(driver, 100).until(
	        lambda x: x.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a[1]")
	    )
	    searchresult.click()

	    target_xpath_here = WebDriverWait(driver, 100).until(
	        lambda x: x.find_element_by_css_selector("#react-root > section > main > div > div._2z6nI > article > div > div > div:nth-child(1) > div:nth-child(1)")
	    )
	    target_xpath_here.click()

	    time.sleep(int(time_entry.get()))

	    liking1 = WebDriverWait(driver, 1000).until(
	        lambda x: x.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]")
	    )
	    liking1.click()

	    nextbutton1 = WebDriverWait(driver, 1000).until(
	        lambda x: x.find_element_by_xpath("/html/body/div[4]/div[1]/div/div/a")
	    )
	    nextbutton1.click()

	    time.sleep(int(time_entry.get()))

	    for i in range(2,1000000000000000):

	        for j in range(1000000000000000):

	            liking1 = WebDriverWait(driver, 100).until(
	            lambda x: x.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]")
	            )
	            liking1.click()

	            nextbutton2 = WebDriverWait(driver, 100).until(
	            lambda x: x.find_element_by_xpath("/html/body/div[4]/div[1]/div/div/a" + str([i]))
	            )
	            nextbutton2.click()
	            time.sleep(int(time_entry.get()))

	finally:
	    driver.quit()

	User_entry.delete(0, END)
	Pass_entry.delete(0, END)
	target_entry.delete(0, END)

b1 = Button(win , text = "Activate", command = clicked)
b1.grid(row = 4, column = 0 , columnspan = 2, pady = 5)

win.mainloop()