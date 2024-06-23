import os
import json
import logging
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from urllib.parse import urlparse, parse_qs, urlencode
import dotenv
# Set up logging
def get_auth_code_and_state():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    client_id = os.getenv('CLIENT_ID')
    state = os.getenv('STATE')
    # Define parameters for the authorization request
    params = {
        'client_id': client_id,
        'response_type': 'code',
        #'redirect_uri': 'http://localhost:8888/callback',
        'redirect_uri': 'https://apple.com',
        'scope': 'user-read-private user-read-email user-read-playback-state user-modify-playback-state user-read-currently-playing',
        'state': state
    }

    # Setup Edge options
    edge_options = Options()

    # Setup WebDriver
    webdriver_service = Service(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service=webdriver_service, options=edge_options)

    # Open the login page on the same domain
    login_url = 'https://accounts.spotify.com/login'
    logger.info("Opening login URL: %s", login_url)
    driver.get(login_url)

    # Load cookies if they exist
    cookies_file = 'cookies.json'
    if os.path.exists(cookies_file):
        with open(cookies_file, 'r') as file:
            cookies = json.load(file)
            for cookie in cookies:
                if 'domain' in cookie and cookie['domain'] in driver.current_url:
                    driver.add_cookie(cookie)
                    logger.info("Loaded cookie: %s", cookie['name'])

    # Define the authorization URL
    auth_url = 'https://accounts.spotify.com/authorize?' + urlencode(params)
    logger.info("Authorization URL: %s", auth_url)

    try:
        # Open the authorization URL in the browser
        driver.get(auth_url)
        logger.info("Opened authorization URL")


        # Wait for the redirect to occur (you can adjust the timeout as needed)
        WebDriverWait(driver, 65).until(EC.url_contains('code='))
        logger.info("URL has changed")

        final_redirected_url = driver.current_url
        logger.info("Final redirected URL: %s", final_redirected_url)

        # Parse the URL to get the code and state
        parsed_url = urlparse(final_redirected_url)
        params = parse_qs(parsed_url.query)
        code = params.get('code', [None])[0]
        state = params.get('state', [None])[0]

        logger.info("Authorization code: %s", code)
        logger.info("State: %s", state)

    except Exception as e:
        logger.error("An error occurred: %s", e)

    finally:
        driver.quit()
    code = params.get('code', [None])[0]
    state = params.get('state', [None])[0]

    print(f"Code: {code}\nState: {state}")

    return code, state