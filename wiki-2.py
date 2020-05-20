import re
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("headless")
options.add_experimental_option('excludeSwitches', ['enable-logging'])

inputtext = input("What do you want to know more about?\n")

driver = webdriver.Chrome(options=options)
driver.get(f"https://en.wikipedia.org/wiki/{inputtext}")

try:
    disambig_check = driver.find_element_by_css_selector(
        "[title*='Category:Disambiguation']")
    ids = driver.find_elements_by_class_name("mw-headline")

    print("\n")

    j = 1
    for header in ids:
        print(str(j) + ". " + header.text)
        j += 1

    choice = input(
        "\nThere is too much information! Sorry. Pick a category.\n")

    print("\nYou chose option " + str(choice) +
          ". Nice! \n" + "Almost there. Pick a subject... \n")

    category = driver.find_elements_by_xpath(
        f'//*[@id="mw-content-text"]/div/ul[{choice}]')

    k = 1
    for cat in category:
        for line in cat.text.split('\n'):
            print(str(k) + ". " + line)
            k += 1

    page = input(
        "\nSo, what's it gonna be?\n")

    url_elem = driver.find_element_by_xpath(
        f'//*[@id="mw-content-text"]/div/ul[{choice}]/li[{page}]//a[@href]')

    url = url_elem.get_attribute("href")

    driver.get(f"{url}")

    html_source2 = driver.find_elements_by_xpath(
        f"//*[@id='mw-content-text']/div/p")

    i = 0
    for part in html_source2:
        for line in part.text.split('\n'):
            if 'disambiguation' not in line and line != '':
                while i < 1:
                    line = re.sub("[\(\[].*?[\)\]]", "", line)
                    print(
                        f"Here is some information about {inputtext}: \n" + line)
                    i += 1
    driver.quit()

except:
    html_source = driver.find_elements_by_xpath(
        f"//*[@id='mw-content-text']/div/p")

    i = 0
    for part in html_source:
        for line in part.text.split('\n'):
            if 'disambiguation' not in line and line != '':
                while i < 1:
                    line = re.sub("[\(\[].*?[\)\]]", "", line)
                    print(
                        f"Here is some information about {inputtext}: \n" + line)
                    i += 1
    driver.quit()


# TODO: sublists count - xpath different for sublists
# TODO: Wikipedia does not have an article with this exact name exception
# TODO: Then search bar?
