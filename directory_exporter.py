import csv
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

# To set the appropriate webdriver Chrome option.
def no_headless_option(enabled=True):
    if enabled == True:
        return webdriver.Chrome('./chromedriver')
    else:
        chrome_option = webdriver.ChromeOptions()
        chrome_option.add_argument("--headless")
        return webdriver.Chrome(executable_path='./chromedriver', options=chrome_option)

# Be sure to set the (last) 'Name' column to descending order
def set_list_to_descending_order_by_last_name():
    try:
        name_ascending_element = driver.find_element_by_css_selector(".fa.fa-caret-up")
        name_ascending_element.click()
    except NoSuchElementException:
        pass

def primary_number(contact_element):
    # expect contact_element in parameter
    primary_contact_list = []
    for i in contact_element:
        each_contact_list = i.text.splitlines()
        if len(each_contact_list) >= 2:
            primary_contact_list.append(each_contact_list[0])
        elif len(each_contact_list) < 2:
            primary_contact_list.append('')
    if len(primary_contact_list) == len(contact_element):
        return primary_contact_list
    else:
        raise ValueError('Something is not quite right with primary_number function')

def secondary_number(contact_element):
    # expect contact_element in parameter
    secondary_contact_list = []
    for i in contact_element:
        each_contact_list = i.text.splitlines()
        if len(each_contact_list) > 2:
            secondary_contact_list.append(each_contact_list[1])
        elif len(each_contact_list) <= 2:
            secondary_contact_list.append('')
    if len(secondary_contact_list) == len(contact_element):
        return secondary_contact_list
    else:
        raise ValueError('Something is not quite right with secondary_number function')

if __name__ == "__main__":
    
    # set Selenium Webdriver
    driver = no_headless_option(False) # run in "background"
    driver.get('https://my.gallaudet.edu/Directory')

    # this is not optional as the default unsorted order appears to be broken
    set_list_to_descending_order_by_last_name()

    # create a new or overwrite existing CSV file with the title row in first one
    with open('gallaudet_directory.csv', mode='w') as directory_file:
        directory_writer = csv.writer(directory_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        directory_writer.writerow(['name','title','primary_number','secondary_number','email','department','location'])

    # loop through each page to extract each information
    while True:
        # create lists of elements per page
        name_list = driver.find_elements_by_xpath('//*[@id="IgxBody"]/div/div[2]/div[2]/div[2]/table/tbody/tr/td[2]/a')
        title_list = driver.find_elements_by_xpath('//*[@id="IgxBody"]/div/div[2]/div[2]/div[2]/table/tbody/tr/td[2]/span')
        contact_list = driver.find_elements_by_xpath('//*[@id="IgxBody"]/div/div[2]/div[2]/div[2]/table/tbody/tr/td[3]')
        primary_number_list = primary_number(contact_list)
        secondary_number_list = secondary_number(contact_list)
        email_list = driver.find_elements_by_xpath('//*[@id="IgxBody"]/div/div[2]/div[2]/div[2]/table/tbody/tr/td[3]/a')
        department_list = driver.find_elements_by_xpath('//*[@id="IgxBody"]/div/div[2]/div[2]/div[2]/table/tbody/tr/td[4]/a')
        location_list = driver.find_elements_by_xpath('//*[@id="IgxBody"]/div/div[2]/div[2]/div[2]/table/tbody/tr/td[5]/a')

        # # print the entries to stdout (this is a test for csv file output)
        # for i in range(len(name_list)):
        #     print(name_list[i].text,';', title_list[i].text,';', primary_number_list[i],';', secondary_number_list[i],';', \
        #         email_list[i].text,';', department_list[i].text,';', location_list[i].text)

        # append each contact data to CSV file
        with open('gallaudet_directory.csv', mode='a') as directory_file:
            directory_writer = csv.writer(directory_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for i in range(len(name_list)):
                directory_writer.writerow([name_list[i].text, title_list[i].text, primary_number_list[i], \
                    secondary_number_list[i], email_list[i].text, department_list[i].text, location_list[i].text])

        try:
            # go to the next page if there are remaining contacts
            driver.find_element_by_link_text('»').click()
        except NoSuchElementException:
            # else break out of while loop if there's no more page left
            break

    driver.quit()
