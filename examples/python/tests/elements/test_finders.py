from selenium import webdriver
from selenium.webdriver.common.by import By


def test_basic_finders():
    driver = webdriver.Chrome()
    driver.get('https://www.selenium.dev/')

    body_on_page = driver.find_element(By.CLASS_NAME, 'td-home')
    container_on_page = body_on_page.find_element(By.CLASS_NAME, 'container-fluid')

    assert container_on_page.is_displayed()

    driver.quit()

def test_evaluating_shadow_DOM():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get('https://www.selenium.dev/selenium/web/shadowRootPage.html')

    # div_el = driver.find_element(By.TAG_NAME, 'body')
    custom_element = driver.find_element(By.TAG_NAME, 'custom-checkbox-element')
    assert custom_element.is_displayed()
    print(custom_element.shadow_root)
    assert custom_element.shadow_root
    div_children = custom_element.shadow_root.find_element(By.CSS_SELECTOR, 'input[type=checkbox]')
    print(div_children)
    assert div_children.is_displayed()

    driver.quit()

def test_optimized_locator():
    driver = webdriver.Chrome()
    driver.get('https://www.selenium.dev/')

    nested_element = driver.find_element(By.CSS_SELECTOR, '.td-home #announcement-banner')

    assert nested_element.is_displayed()

    driver.quit()

def test_all_matching_elements():
    driver = webdriver.Chrome()
    driver.get('https://www.selenium.dev/')

    header_two_elements = driver.find_elements(By.TAG_NAME, 'h2')
    
    assert len(header_two_elements) > 1

    for header_element in header_two_elements:
        print(header_element.text)

    driver.quit()

def test_find_elements_from_element():
    driver = webdriver.Chrome()
    driver.get('https://www.selenium.dev/')

    main_element = driver.find_element(By.TAG_NAME, 'main')
    svg_elements = main_element.find_elements(By.TAG_NAME, 'svg')

    assert len(svg_elements) > 1

    for svg_element in svg_elements:
        print(svg_element.is_displayed())


    ## get elements from parent element using XPATH
    ## NOTE: in order to utilize XPATH from current element, you must add "." to beginning of path

    header_tag = driver.find_element(By.TAG_NAME, 'header')
    # Get first element of tag 'ul'
    ul_tag = header_tag.find_element(By.XPATH, '//ul')

    # get children of tag 'ul' with tag 'li'
    elements  = ul_tag.find_elements(By.XPATH, './/li')
    assert len(elements) > 0

    for element in elements:
        print(element.text)

    driver.quit()

def test_get_active_element():
    driver = webdriver.Chrome()
    driver.get('https://www.selenium.dev/')

    dropdown = driver.find_element(By.CSS_SELECTOR, '.nav-item.dropdown')
    dropdown.click()

    active_element = driver.switch_to.active_element

    assert active_element.get_attribute('href').endswith('#')

    driver.quit()

