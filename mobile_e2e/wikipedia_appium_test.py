from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Desired capabilities
desired_caps = {
    "platformName": "Android",
    "platformVersion": "11", 
    "deviceName": "emulator256", 
    "app": "/wikipedia_app.apk",
    "appPackage": "org.wikipedia",
    "appActivity": "org.wikipedia.main.MainActivity",
    "automationName": "UiAutomator2",
}

# Initialize the Appium driver
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
wait = WebDriverWait(driver, 10)

try:
    # Step 1: Launch app and scroll down to the end
    driver.implicitly_wait(10)
    for _ in range(10):  # Scroll down multiple times until the end
        driver.swipe(500, 1500, 500, 300, 800)

    # Step 2: Click on the "My lists" icon
    my_lists_button = wait.until(
        EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "My lists"))
    )
    my_lists_button.click()
    driver.implicitly_wait(3)

    # Step 3: Click on the "History" icon
    history_button = wait.until(
        EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "History"))
    )
    history_button.click()
    driver.implicitly_wait(3)

    # Step 4: Click on the "Nearby" icon
    nearby_button = wait.until(
        EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Nearby"))
    )
    nearby_button.click()
    driver.implicitly_wait(3)

    # Step 5: Go back to the home page by clicking on "Explore"
    explore_button = wait.until(
        EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Explore"))
    )
    explore_button.click()

    # Step 6: Scroll up to the first topic
    for _ in range(10):  # Scroll up multiple times until the first topic
        driver.swipe(500, 300, 500, 1500, 800)

    # Task 2: Launch app, search for "New York" and assert results
    # Step 1: Locate and click on the search bar
    search_bar = wait.until(
        EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia"))
    )
    search_bar.click()

    # Step 2: Enter "New York" in the search bar
    search_input = wait.until(
        EC.presence_of_element_located((AppiumBy.ID, "org.wikipedia:id/search_src_text"))
    )
    search_input.send_keys("New York")

    # Step 3: Assert that search results are displayed
    search_results = wait.until(
        EC.presence_of_all_elements_located((AppiumBy.ID, "org.wikipedia:id/page_list_item_title"))
    )
    assert len(search_results) > 0, "Search results were not displayed."

    # Step 4: Double click on the close search button
    close_button = wait.until(
        EC.presence_of_element_located((AppiumBy.ID, "org.wikipedia:id/search_close_btn"))
    )
    close_button.click()  # First click to clear the search
    close_button.click()  # Second click to return to the home page

    # Task 3: Disable all options in Settings and return to home page
    settings_button = wait.until(
        EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "More options"))
    )
    settings_button.click()

    settings_option = wait.until(
        EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Settings']"))
    )
    settings_option.click()

    toggle_options = wait.until(
        EC.presence_of_all_elements_located((AppiumBy.CLASS_NAME, "android.widget.Switch"))
    )
    for toggle in toggle_options:
        if toggle.get_attribute("checked") == "true":
            toggle.click()

    # Go back to the home page
    driver.back()
    driver.back()

    print("Test completed successfully!")


finally:
    # Quit the driver
    driver.quit()
