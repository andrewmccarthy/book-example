from selenium import webdriver

def test_server_is_running():
    browser = webdriver.Firefox()
    browser.get('http://localhost:8000')

    assert 'Django' in browser.title
