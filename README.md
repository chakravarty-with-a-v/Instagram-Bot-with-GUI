# Instagram-Bot-with-GUI
The Project uses Selenium and Chrome WebDriver to login to Instagram and do the following : <br />
  (1) Like and Comment on Target Account <br />
  (2) Follow Target Account <br />
  (3) Unfollow Target Account <br />
The Project uses tkinter for GUI
# TO RUN THIS PROJECT :

Download the files and store them in the same folder. <br />
Make sure to have Chrome Driver installed as per your Chrome VERSION :  link-> https://chromedriver.chromium.org/downloads <br />
chrome_driver_path should be : file path where you installed chromedriver + "\chromedriver.exe" for **WINDOWS** and simply "\chromedriver" for **Mac** <br />
EXAMPLE : In My case , Chrome Driver was installed in "C:\Users\hp\Desktop\PROGRAMS\Chrome Driver" <br />so I appended "\chromedriver" as I am Using **WINDOWS** to get "C:\Users\hp\Desktop\PROGRAMS\Chrome Driver\chromedriver.exe"

# USER INPUTS:

(1) In **FIRST WINDOW** User needs to provide **Target USER ID**

![Main Menu](https://user-images.githubusercontent.com/109027110/182222920-eadca033-1bb4-40b3-83ad-cef98bdc0fdc.png)

(2) If User selects *Like and Comment* Option a new Dialog Box Opens asking for **Comment Text** and **Number of Posts to like starting from recent post**

![comment](https://user-images.githubusercontent.com/109027110/182223329-fde63a6d-3371-4b9e-ae05-1c0981ed4b95.png)

(3) For Follow and Unfollow Buttons, The Bot automatically Follows and Unfollows The Target Account
# Bot CLASS
## SELENIUM AND CHROME DRIVER
Bot Class Members : <br />
(1) Using Selenium and Chrome Driver, a webdriver.Chrome Object is created. Using it I have made the driver to open to https://www.instagram.com/accounts/login/ <br />
(2) target : String to store User ID of Target Account <br />
(3) comment : To Store User Comment <br />
(4) number : To Store the number of new posts from latest post to like and comment <br />

## Bot Methods
(1) login() -> Logs into Bot's Instagram Account <br />
(2) search() -> Finds ID based on target ID input from USER. If ID is invalid , it generates an error message and returns to Home Page <br />
(3) follow() -> Employs Search method and then follows user. If User is already followed , generates an error message. Finally returns to Home Page <br />
(4) unfollow()-> Same as follow() method except that it unfollows target account <br />
(5) private()-> Checks if **target account** is **private with respect to the Bot account.** <br />
(6) like_comment() -> Searches Target Account , checks if it is Not Private with respect to Bot Account and then likes and comments Target Account Posts based on User Input <br />
(7) home() -> Returns to Home Page

# GUI

## Main Window
 This is created in the main python file Instagram_Bot.py using tkinter
 
 ## COMMENTS WINDOW
 
 This is created using LikeComment class in likecomment.py
 
  likecomment class objects take a Tk type object and a Bot type Object as parameters and the Window is Created using tkinter <br />
  ### likecomment members
  (1) Window Entries are class members  namely **comment entry** and **number entry** <br />
  (2) An Object of TK class <br />
  (3) An Object of Bot class
  
 ### likecomment methods
 comment_input() -> to take input from Entries and store them in methods of likecomment.Bot accordingly.
  
  # MESSAGEBOX from tkinter
  Used for Generating Error or Information Messages
  
 
  
