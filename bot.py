import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from tkinter import messagebox

url = "https://www.instagram.com/accounts/login/"
chrome_driver_path = r"C:\Users\hp\Desktop\PROGRAMS\Chrome Driver\chromedriver.exe"


class Bot:
    def __init__(self, uname, password):
        self.uname = uname
        self.password = password
        self.driver = webdriver.Chrome(service=Service(chrome_driver_path))
        self.driver.maximize_window()
        self.target = ""
        self.comment = ''
        self.number = ''
        self.login()

    def login(self):
        self.driver.get(url)
        time.sleep(3)
        username = self.driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/div[1]/div['
                                                      '2]/form/div/div[1]/div/label/input')
        username.send_keys(self.uname)
        passwd = self.driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/div[1]/div['
                                                    '2]/form/div/div[2]/div/label/input')
        time.sleep(3)
        passwd.send_keys(self.password)
        passwd.send_keys(Keys.ENTER)
        time.sleep(3)
        not_now = self.driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/div/div/button')
        not_now.click()
        time.sleep(3)
        notification_not_now = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div['
                                                                  '1]/div/div[2]/div/div/div/div/div/div/div/div['
                                                                  '3]/button[2]')
        time.sleep(2)
        notification_not_now.click()
        messagebox.showinfo('SUCCESS!', 'LOGIN SUCCESSFUL!')

    def search(self):
        time.sleep(2)
        search = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div['
                                                    '1]/section/nav/div[2]/div/div/div[2]/input')
        time.sleep(3)
        search.send_keys(self.target)
        time.sleep(3)
        search.send_keys(Keys.ARROW_DOWN)
        time.sleep(2)
        search.send_keys(Keys.ENTER)
        time.sleep(3)
        try:
            id_name = self.driver.find_element(By.CSS_SELECTOR, 'span._aacl._aacp._aacw._aacx._aad7._aade')
            print(f'ID {id_name.text} is valid')
        except NoSuchElementException:
            messagebox.showerror('ERROR', 'INVALID ID')
            self.home()

    def follow(self):
        self.search()
        time.sleep(3)
        try:
            follow_button = self.driver.find_element(By.CSS_SELECTOR, 'button._acan._acap._acas')
            follow_button.click()
            messagebox.showinfo('SUCCESS', f'SUCCESSFULLY FOLLOWED {self.target}')
            self.home()
        except NoSuchElementException:
            messagebox.showerror('ERROR', f'You Already Follow {self.target}')
            self.home()

    def unfollow(self):
        self.search()
        time.sleep(3)
        try:
            drop_down = self.driver.find_element(By.CSS_SELECTOR, 'div._ab8w._ab94._ab99._ab9f._ab9m._ab9p._abb0._abcm button')
            drop_down.click()
            time.sleep(2)
            unfollow_button = self.driver.find_element(By.CSS_SELECTOR, 'button._a9--._a9-_')
            unfollow_button.click()
            messagebox.showinfo('UNFOLLOWED!', f'SUCCESSFULLY UNFOLLOWED {self.target}')
        except NoSuchElementException:
            messagebox.showerror('ERROR', f'YOU DO NOT FOLLOW {self.target} ')
            self.home()
            return

    def private_account(self):
        try:
            private_account = self.driver.find_element(By.CSS_SELECTOR, 'h2._aa_u')
        except NoSuchElementException:
            print('Account is Not Private to You.. Continue...')
            return False
        else:
            return True

    def like_comment(self):
        time.sleep(2)
        if len(self.target) == 0:
            messagebox.showerror('ERROR', 'NO TARGET ID SPECIFIED!')
            return
        if len(self.comment) == 0:
            messagebox.showerror('ERROR', 'NO COMMENT SPECIFIED!')
            return
        if int(self.number) <= 0:
            messagebox.showerror('ERROR', 'NUMBER OF POSTS NOT SPECIFIED!')
            return
        self.search()
        time.sleep(3)
        if self.private_account():
            messagebox.showerror('ERROR', 'ACCOUNT IS PRIVATE!')
            self.home()
            return
        else:
            time.sleep(4)
            try:
                latest_post = self.driver.find_element(By.CSS_SELECTOR, 'div._aabd._aa8k._aanf a')
                latest_post.click()
            except NoSuchElementException:
                print('User has no Post')
            time.sleep(3)
            for i in range(int(self.number)):
                time.sleep(3)
                try:
                    like = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div['
                                                              '1]/div/div[3]/div/div/div/div/div['
                                                              '2]/div/article/div/div[ '
                                                              '2]/div/div/div[2]/section[1]/span[1]/button')

                    like.click()
                except NoSuchElementException:
                    print('Unable to find Like Button at iteration')
                time.sleep(3)
                # WE HOLD TWO COMMENT SELENIUM OBJECTS SINCE AFTER CLICKING THE COMMENT TEXT AREA , XPATH CHANGES
                try:
                    before_comment = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div['
                                                                        '2]/div/div/div[1]/div/div['
                                                                        '3]/div/div/div/div/div[2]/div/article/div/div['
                                                                        '2]/div/div/div[2]/section[3]/div/form/'
                                                                        'textarea')
                    before_comment.click()
                    time.sleep(2)
                    comment = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div['
                                                                 '1]/div/div[3]/div/div/div/div/div['
                                                                 '2]/div/article/div/div[2]/div/div/div[2]/section['
                                                                 '3]/div/form/textarea')

                    comment.send_keys(self.comment)
                    comment.send_keys(Keys.ENTER)
                except NoSuchElementException:
                    print('Comment Box Not Found at iteration')
                try:
                    time.sleep(3)
                    go_forward = self.driver.find_element(By.CSS_SELECTOR, "div._aaqg._aaqh button")
                    time.sleep(3)
                    go_forward.click()
                except NoSuchElementException:
                    print('Last Post Reached! at iteration')
                    break
            time.sleep(3)
            try:

                close = self.driver.find_element(By.CSS_SELECTOR, 'div.o9tjht9c.jar9mtx6.mbzxb4f5.njoytozt div')
                close.click()
            except NoSuchElementException:
                print('Could Not Find CLOSE BUTTON')
            time.sleep(2)
            self.home()

    def home(self):
        home = self.driver.find_element(By.CSS_SELECTOR, 'div._acrd a.oajrlxb2')
        home.click()
