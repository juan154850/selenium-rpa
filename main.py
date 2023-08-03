from selenium import webdriver
import pandas as pd #Library for file management.
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select #Library for the management of select html


def get_text_from_table(table, tag_name):
    """
    Extracts text data from a table element.

    Parameters:
        table (WebElement): The table element from which to extract data.
        tag_name (str): The tag name of the cells (e.g., 'td' for table data cells, 'th' for table header cells).

    Returns:
        list: A list of lists containing the text data of the table. Each inner list represents a row of the table.
    """
    data = []
    for row in table:
        cells = row.find_elements(By.TAG_NAME, tag_name)
        row_data = [cell.text for cell in cells]
        data.append(row_data)
    return data

def get_nobel_winners():
    """
    Scrapes Nobel Prize winners' information from a Wikipedia page and saves it to a CSV file.

    The function uses Selenium WebDriver to interact with the Wikipedia page and extract data from the table
    containing Nobel Prize winners. The extracted data is then stored in a pandas DataFrame and saved as a CSV file.

    Raises:
        Exception: If any error occurs during the scraping process, it will be raised with an error message.

    Note:
        - The WebDriver runs in headless mode (no visible browser window) by default to improve performance.
        - The Wikipedia page URL used in this function may be subject to change. Make sure to update the URL
            if necessary to match the current Wikipedia page.
    """
    # Set up options for the WebDriver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode (no visible window)
    try:
        # Create the WebDriver with options and a context manager (using 'with' statement)
        with webdriver.Chrome(options=chrome_options) as driver:
            # We entered the wikipedia page that contains the nobel prize winners.
            driver.get("https://www.wikipedia.org/")

            # We perform the corresponding navigation to search from the main source for Nobel Prize winners.
            select_language = WebDriverWait(driver,10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '[id="searchLanguage"]'))
            )
            select_language = Select(select_language)
            select_language.select_by_value('es')

            search_input = WebDriverWait(driver,10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '[id="searchInput"]'))
            )

            search_input.send_keys("Anexo: Ganadores del premio Nobel")
            search_input.submit()

            # Wait for the data table to be present on the page
            data_table = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '[id="mw-content-text"] table'))
            )

            # We get the headers and store them in an array.
            table_headers = data_table.find_elements(By.TAG_NAME, "thead")
            headers = get_text_from_table(table_headers, "th")

            # We get the winners' information and store it in an array.
            table_winners = data_table.find_elements(By.TAG_NAME, "tr")
            winners = get_text_from_table(table_winners, "td")

        # We create a DataFrame of pandas with the extracted data.
        df = pd.DataFrame(data=winners, columns=headers).dropna(how='all')
        # Create the CSV file and save the data in it.
        df.to_csv("nobel_winners.csv", index=False, encoding='utf-8-sig')

    except Exception as e:
        raise Exception("An error occurred:", e)


get_nobel_winners()
