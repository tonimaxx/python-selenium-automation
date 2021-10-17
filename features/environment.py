from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from app.application import Application


def browser_init(context):
    """
    :param context: Behave context
    """
    context.driver = webdriver.Chrome(executable_path='./chromedriver')

    """
    ##-- Edited for Chrome Profile
    options = Options()

    options.add_argument("user-data-dir=/Users/tonimaxx/Library/Application Support/Google/Chrome/Profile 31")
    context.driver = webdriver.Chrome(executable_path = './chromedriver', chrome_options=options)
    ##-- End Chrome Profile
    """

    # context.browser = webdriver.Safari()
    # context.browser = webdriver.Firefox()

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
