from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unidecode
import time


Problems = {}
driver = webdriver.Chrome()


driver.get("http://laptrinhonline.club/accounts/login/?next=/user")

# Username = input("Username: ")
# Password = input("Password: ")

# usernameElement = driver.find_element("id", "id_username")
# usernameElement.send_keys(Username)
# passwordElement = driver.find_element("id", "id_password")
# passwordElement.send_keys(Password)
# passwordElement.send_keys(Keys.RETURN)

while 1:
    if driver.current_url == "http://laptrinhonline.club/user":
        break

print("Login Success")

user_sidebar = driver.find_element(By.CLASS_NAME, "user-sidebar")
UsernameLink = user_sidebar.find_element(By.TAG_NAME, "a").get_attribute("href")

print(UsernameLink)

for i in range(1, 12):
    driver.get(UsernameLink + str(i) + "?status=AC")
    elems = driver.find_elements(By.CLASS_NAME, "submission-row")
    for elem in elems:
        idProblem = elem.get_attribute("id")
        divSub = elem.find_element(By.CLASS_NAME, "name")
        nameProblem = divSub.find_element(By.TAG_NAME, "a").text
        Problems[idProblem] = nameProblem
        
for problem in Problems:
    idProblem = problem
    nameProblem = Problems[problem]
    driver.get("http://laptrinhonline.club/src/" + str(idProblem) + "/raw")
    dataCode = driver.find_element(By.TAG_NAME, "pre").text
    driver.execute_script("window.history.go(-1)")
    nameProblem = unidecode.unidecode(nameProblem)
    tempName = ""
    for x in nameProblem:
        if (
            (x >= "a" and x <= "z")
            or (x >= "A" and x <= "Z")
            or (x >= "0" and x <= "9")
        ):
            tempName += x
    nameProblem = tempName
    with open("./src/" + str(nameProblem) + ".cpp", "w", encoding="utf-8") as file:
        file.write(dataCode)
    time.sleep(0.5)

print("Done")

time.sleep(5)

driver.quit()
