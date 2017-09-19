__author__ = 'Ankit'
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import argparse
from selenium import webdriver

class flipkart_action:
    url = "https://www.flipkart.com/"
    browser = webdriver.Chrome("./utils/chromedriver")
    print "\nOpeaning Flipkart.com"
    browser.get(url)

    """ constructure """
    def __init__(self,user_id,user_password):
        try:

            self.id = user_id
            self.user_password=user_password
            print "Performing Login to flipkart.com"
            login_link2 =self.browser.find_element_by_link_text( "Log In")
            login_link2.click()
            name = self.browser.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div/form/div[1]/input")
            password = self.browser.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/input")
            name.send_keys(user_id)
            password.send_keys(user_password,Keys.ENTER)
            time.sleep(2)
            account_info =self.browser.find_element_by_link_text('My Account').text

            if  account_info == 'My Account':
                print "Login Pass"
            else:
                 print "Login Fail"
        except:
           print "Something Went wrong "


    def add_to_cart(self):
        print "Serarching for Iphone 7"
        search_bar = self.browser.find_element_by_xpath('//*[@placeholder="Search for Products, Brands and More"]')
        search_bar.send_keys("Iphone 7",Keys.ENTER)
        time.sleep(2)
        self.browser.find_element_by_xpath("//span[@id ='productRating_LSTMOBEMK62PN2HU7EEINTGNU_MOBEMK62PN2HU7EE_']").click()
        print "Adding to cart "
        time.sleep(2)
        print self.browser.current_url
        cont = "#container > div > div:nth-child(2) > div > div > div > div._1GRhLX._3N5d1n > div > div._3S6yHr > div._1k1QCg > ul > li:nth-child(1) > button"
        self.browser.find_element_by_css_selector(cont).click()
        time.sleep(4)
        print self.browser.current_url
        print "verifying cart"
        cart_val = 'MY CART (1)'
        fk_vart= self.browser.find_element_by_xpath('// *[ @ id = "container"] / div / div[1] / div / div / div[1] / div[1] / span').text
        print fk_vart
        if cart_val==fk_vart:
            print "Item Added to cart"
        else:
            print "Item not added to cart "


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
        if login_text==login_link2:
            print "Logput successfull"


'''Argparser to take comand line arguments!!! '''
parser = argparse.ArgumentParser()
parser.add_argument('email', help='email or phone  ',type=str)
parser.add_argument('password', help='password',type=str)
args = parser.parse_args()

email = args.email
password = args.password
obj = flipkart_action(email,password)
obj.add_to_cart()
obj.logout()
