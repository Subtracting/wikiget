import re
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("headless")
options.add_experimental_option('excludeSwitches', ['enable-logging'])

inputtext = input("What do you want to know more about?\n")

driver = webdriver.Chrome(options=options)
driver.get(f"https://en.wikipedia.org/wiki/{inputtext}")

try:

    html_source = driver.find_element_by_xpath(
        '//*[@id="mw-content-text"]/div/p[3]').text
    html_source = re.sub("[\(\[].*?[\)\]]", "", html_source)
    print(f"Here is some information about {inputtext}: \n" + html_source)
    driver.quit()
except:
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
        # page_list = cat.text.split('\n')
        for line in cat.text.split('\n'):
            print(str(k) + ". " + line)
            k += 1

    page = input(
        "\nSo, what's it gonna be?\n")

    url_elem = driver.find_element_by_xpath(
        f'//*[@id="mw-content-text"]/div/ul[{choice}]/li[{page}]//a[@href]')

    url = url_elem.get_attribute("href")

    driver.get(f"{url}")

    html_source2 = driver.find_element_by_xpath(
        '//*[@id="mw-content-text"]/div/p[1]').text
    html_source2 = re.sub("[\(\[].*?[\)\]]", "", html_source2)
    print(f"Here is some information about {inputtext}: \n" + html_source2)
    driver.quit()


# //*[@id = "mw-content-text"]/div/ul[2]/li[1]
# //*[@id = "mw-content-text"]/div/ul[2]/li[2]
# //*[@id = "mw-content-text"]/div/ul[2]/li[2]/ul/li
# //*[@id = "mw-content-text"]/div/ul[2]/li[3]


# TODO: is niet altijd p[3]. Kan ook p[2] zijn, bijv. 'duck'
# TODO: sublists juist tellen
# TODO: eerste paar zinnen per pagina met de inputtext

# //*[@id="mw-content-text"]/div/ul[2]/li[3]
