from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unidecode
import time


Problems = {}
driver = webdriver.Chrome()

Username = input("Username: ")
Password = input("Password: ")

driver.get(
    "http://laptrinhonline.club/accounts/login/?next=/submissions/user/NGUYENVANHOANG_K64_SFIT/?status=AC"
)

usernameElement = driver.find_element("id", "id_username")
usernameElement.send_keys(Username)
passwordElement = driver.find_element("id", "id_password")
passwordElement.send_keys(Password)
passwordElement.send_keys(Keys.RETURN)

print("Runing...")

for i in range(1, 12):
    driver.get(
        "http://laptrinhonline.club/submissions/user/NGUYENVANHOANG_K64_SFIT/"
        + str(i)
        + "?status=AC"
    )
    elems = driver.find_elements(By.CLASS_NAME, "submission-row")
    for elem in elems:
        idProblem = elem.get_attribute("id")
        divSub = elem.find_element(By.CLASS_NAME, "name")
        nameProblem = divSub.find_element(By.TAG_NAME, "a").text
        if idProblem not in Problems:
            Problems[idProblem] = nameProblem
            driver.get("http://laptrinhonline.club/src/" + str(idProblem) + "/raw")
            dataCode = driver.find_element(By.TAG_NAME, "pre").text
            driver.execute_script("window.history.go(-1)")
            for x in [" ", ":", "?", "/", "*", "<", ">", "|", '"', "."]:
                nameProblem = nameProblem.replace(x, "_")
            nameProblemFile = unidecode.unidecode(nameProblem)
            # print("./src/" + str(nameProblemFile) + ".cpp")
            with open(
                "./src/" + str(nameProblemFile) + ".cpp", "w", encoding="utf-8"
            ) as file:
                file.write(dataCode)

print("Done")

driver.quit()
