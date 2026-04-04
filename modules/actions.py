from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
import os
import webbrowser


def play_youtube(query):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    driver.get("https://www.youtube.com")
    time.sleep(2)

    search_box = driver.find_element(By.NAME, "search_query")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)

    time.sleep(3)

    videos = driver.find_elements(By.ID, "video-title")
    videos[0].click()


def search_google(query):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    driver.get("https://www.google.com")
    time.sleep(2)

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)

    time.sleep(2)

    results = driver.find_elements(By.CSS_SELECTOR, "h3")
    results[0].click()


def perform_action(command, original_command):

    command = command.lower()

    # 🎬 Play music
    if "play" in command or "song" in command or "music" in command:
        query = original_command

        for word in ["play", "song", "songs", "on youtube", "youtube"]:
            query = query.replace(word, "")

        query = query.strip()

        if query == "":
            query = "top songs"

        play_youtube(query)

    # 🔍 Google search
    elif "search" in command or "google" in command:
        query = original_command

        for word in ["search", "google"]:
            query = query.replace(word, "")

        query = query.strip()

        if query == "":
            query = "latest news"

        search_google(query)

    # 🖥️ Open apps
    elif "open" in command:
        app = command.replace("open", "").strip()
        os.system(f"start {app}")

    # 🌐 fallback
    else:
        webbrowser.open("https://www.google.com")