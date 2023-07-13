# Importing required libraries

# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the Amazon.ca homepage
driver.get("https://music.youtube.com/")
time.sleep(3)

# Finding the search bar and entering text
# search_bar = driver.find_element_by_id("id","twotabsearchtextbox") old syntax
# search_bar = driver.find_element("id","gh-ac")
# search_bar.send_keys("earphones")
#
# # Submitting the search query
# search_bar.send_keys(Keys.RETURN)
#
# # Waiting for the search results page to load
# time.sleep(5)
#
# # Verifying that the search results page has loaded
# assert "earphones" in driver.title

# Selecting a laptop from the search results
earphones_link = driver.find_element("xpath","/html/body/ytmusic-app/ytmusic-app-layout/ytmusic-nav-bar/div[2]/ytmusic-pivot-bar-renderer/ytmusic-pivot-bar-item-renderer[2]/yt-formatted-string");
# laptop_link = driver.find_element("By.CSS_SELECTOR","span[data-component-type='s-product-image'] a")
earphones_link.click();
time.sleep(5);

# Adding the laptop to the cart

earphones_link1 = driver.find_element("xpath","/html/body/ytmusic-app/ytmusic-app-layout/div[4]/ytmusic-browse-response/div[2]/div[4]/ytmusic-section-list-renderer/div[2]/ytmusic-grid-renderer/div[2]/ytmusic-navigation-button-renderer[3]/button/yt-formatted-string");
# laptop_link = driver.find_element("By.CSS_SELECTOR","span[data-component-type='s-product-image'] a")
earphones_link1.click();
time.sleep(5);

# driver.find_element("id","x-buybox-cta").click()
add_to_watchlist_button = driver.find_element("xpath","/html/body/ytmusic-app/ytmusic-app-layout/div[4]/ytmusic-browse-response/div[2]/div[4]/ytmusic-section-list-renderer/div[2]/ytmusic-grid-renderer[1]/div[2]/ytmusic-navigation-button-renderer[2]/button");
add_to_watchlist_button.click();
time.sleep(5);
# Waiting for the cart to update




#proceed_to_checkout= driver.find_element("xpath","/html/body/div[9]/div[3]/div[3]/div/div[1]/div[3]/div[1]/div[2]/div[3]/span/span/input")
#proceed_to_checkout.click()
#time.sleep(2)

# Verifying that the laptop has been added to the cart
# cart_count = driver.find_element("id","nav-cart-count")
# assert cart_count.text == "1"
# cart_count.click()

# Closing the webdriver
driver.close()
