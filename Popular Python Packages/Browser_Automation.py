from selenium import webdriver


browser = webdriver.Chrome()
browser.get("https://github.com")

# username = browser.find_element_by_id("identifierId")
# username.send_keys("ayushvanpariya07@gmail.com")
# next_btn = browser.find_element_by_class_name("VfPpkd-vQzf8d")
# next_btn.click()
Signin_link = browser.find_element_by_link_text("Sign in")
Signin_link.click()
username = browser.find_element_by_id("login_field")
username.send_keys("ayushvanparia@gmail.com")
password = browser.find_element_by_id("password")
password.send_keys("qwe456yuioP")
password.submit()


# assert "AyushVanparia" in browser.page_source

# pflink = browser.find_element_by_class_name(".user-profile-link")
# linklabel = pflink.get_attribute("innerHTML")
# assert "AyushVanparia" in linklabel

browser.quit()
