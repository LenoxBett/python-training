# # import pyautogui
# import time

# # Function to paste and send a message
# def send_message(message):
#     # pyautogui.hotkey('ctrl', 'v')  # Paste message
#     # pyautogui.press('enter')  # Sending message
#     time.sleep(2)  # Wait for a moment before sending the next message

# # Main function
# def main():
#     # Message to be sent
#     message = "✅💰GUYS THIS PERSON IS LEGIT ON AVIATOR DM HIM NOW +2️⃣5️⃣4️⃣0️⃣1️⃣0️⃣4️⃣5️⃣2️⃣0️⃣3️⃣3️⃣7️⃣,💯HE HELPED ME WIN 900$ JUST FROM A STAKE OF 18$ AND PAYMENT IS AFTER WIN✅"

#     # Send the message 10 times (you can adjust the number of repetitions as needed)
#     for _ in range(10):
#         send_message(message)

# # Run the main function
# if __name__ == "__main__":
#     main()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def send_message_to_user(user_id, message, username, password):
    driver = webdriver.Chrome()

    try:
        driver.get("https://betting.co.zw/virtual/fast-games/aviator")
        time.sleep(3)  # Adding a delay to ensure page loading

        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Login')]"))
        )
        login_button.click()

        username_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='username']"))
        )
        username_input.send_keys(username)

        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='password']"))
        )
        password_input.send_keys(password)

        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        )
        login_button.click()

        time.sleep(3)  # Adding a delay after login to ensure page loading

        chat_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Chat')]"))
        )
        chat_button.click()

        user_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='user_id']"))
        )
        user_input.send_keys(user_id)

        message_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//textarea[@id='message']"))
        )
        message_input.send_keys(message)

        send_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Send')]"))
        )
        send_button.click()

        print("Message sent successfully.")

    except Exception as e:
        print("An error occurred:", e)

    finally:
        driver.dont_quit()

# User ID and message
user_id = "480951"
message = "💰✅ HERE WE GO TOGETHER WHATSAPP 2️⃣5️⃣4️⃣1️⃣0️⃣4️⃣5️⃣2️⃣0️⃣3️⃣3️⃣7️⃣ LET'S KEEP ON WINNING IF YOU HAVE BEING LOSING/share_bet:3655967717💰"


# Send the message to the user
send_message_to_user(user_id, message, username, password)