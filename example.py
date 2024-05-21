import os
import time

from selenium import webdriver
import selenium.common.exceptions


server = "http://testuser:password@localhost:4444"

options = webdriver.ChromeOptions()

# Uncomment to use a web proxy
# proxy = "http://proxy-host:port"  # Does NOT support auth
# options.add_argument(f"--proxy-server={proxy}")
# options.add_argument('--ignore-certificate-errors')

chrome_prefs = {}
# Do not load images. Makes the request faster and uses less bandwidth
chrome_prefs["profile.default_content_settings"] = {"images": 2}
chrome_prefs["profile.managed_default_content_settings"] = {"images": 2}
options.experimental_options["prefs"] = chrome_prefs


driver = webdriver.Remote(command_executor=server, options=options)

try:
    # Make sure to set to some value that makes sense for your use case
    driver.set_page_load_timeout(60)

    driver.get("https://httpbin.org/headers")

except selenium.common.exceptions.TimeoutException:
    print("timeout")

except Exception as e:
    raise

else:
    print(driver.page_source)

finally:
    # Always make sure you quit the web driver
    driver.quit()


