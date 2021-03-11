from time import sleep

def test_find_element_selenium(browser):
    browser.get("http://the-internet.herokuapp.com/")
    file_uplod_link = browser.find_element_by_link_text('File Upload')
    file_uplod_link.click()
    sleep(5)
    button_upload = browser.find_element_by_id('file-submit')
    assert 'Upload' == button_upload.get_attribute('value')