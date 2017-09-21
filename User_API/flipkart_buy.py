__author__ = 'Ankit'
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import argparse
from selenium import webdriver



class webelements:

    name ="/html/body/div[2]/div/div/div/div/div[2]/div/form/div[1]/input"
    password ="/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/input"
    search_bar = '//*[@placeholder="Search for Products, Brands and More"]'
    cart_text = "//span[@id ='productRating_LSTMOBEMK62PN2HU7EEINTGNU_MOBEMK62PN2HU7EE_']"
    add_to_cart="#container > div > div:nth-child(2) > div > div > div > div._1GRhLX._3N5d1n > div > div._3S6yHr > div._1k1QCg > ul > li:nth-child(1) > button"
    logout_assert = "My Account"
    loout_verify = "Log In"

    fk_Cart ='// *[ @ id = "container"] / div / div[1] / div / div / div[1] / div[1] / span'


class flipkart_login(webelements) :
    browser = webdriver.Chrome("./utils/chromedriver")


    def __init__(self):
        url = "https://www.flipkart.com/"
        print "\nOpeaning Flipkart.com"
        self.browser.get(url)

    """ Login method """

    def login(self,user_id,user_password):
        try:
            self.id = user_id
            self.user_password=user_password
            print "Performing Login to flipkart.com"
            login_link2 =self.browser.find_element_by_link_text( "Log In")
            login_link2.click()
            name = self.browser.find_element_by_xpath(self.name)

            password = self.browser.find_element_by_xpath(self.password)
            name.send_keys(user_id)
            password.send_keys(user_password,Keys.ENTER)
            time.sleep(2)
            account_info =self.browser.find_element_by_link_text(self.logout_assert).text

            assert  account_info != 'My Account',"Fail"
            print "Login Pass"
        except:
           print "Something Went wrong "


class home_page(flipkart_login):


    def search(self):

        print "Serarching for Iphone 7"
        search_bar = self.browser.find_element_by_xpath(self.search_bar)
        search_bar.send_keys("Iphone 7",Keys.ENTER)
        time.sleep(2)
        self.browser.find_element_by_xpath(self.add_to_cart).click()
        print "Adding to cart "
        time.sleep(2)
        print self.browser.current_url
        #cont = "#container > div > div:nth-child(2) > div > div > div > div._1GRhLX._3N5d1n > div > div._3S6yHr > div._1k1QCg > ul > li:nth-child(1) > button"
        time.sleep(4)


class cart(home_page):


    def addto_cart_and_verify(self):
        self.browser.find_element_by_css_selector(self.add_to_cart).click()
        print self.browser.current_url
        print "verifying cart"

        fk_vart= self.browser.find_element_by_xpath(self.fk_Cart).text
        print fk_vart
        cart_val = 'MY CART (1)'
        assert cart_val!=self.fk_Cart,"Not addedd"
        print "Item Added to cart"


    def logout(self):
        print "Performing Logout"
        account_info = self.browser.find_element_by_link_text('My Account')
        hover = ActionChains(self.browser).move_to_element(account_info)
        hover.perform()
        logout =self.browser.find_element_by_link_text('Log Out')
        logout.click()
        print "Checking if its logged out "
        time.sleep(1)
        login_link2 = self.browser.find_element_by_link_text("Log In").text
        print login_link2
        login_text = 'Log In'
        assert login_text!=login_link2,"Logout failed"
        print "Logput successfull"




'''Argparser to take comand line arguments!!! '''

parser = argparse.ArgumentParser()
parser.add_argument('email', help='email or phone  ',type=str)
parser.add_argument('password', help='password',type=str)
args = parser.parse_args()



email = args.email
password = args.password
obj = cart()

obj.login(email,password)
obj.search()
obj.addto_cart_and_verify()
obj.logout()
