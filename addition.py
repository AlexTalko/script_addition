import os
import time
import pyautogui

# Открытие калькулятора
# os.system('calc')  # Для Windows
os.system('open -a Calculator')  # Для macOS
# os.system('gnome-calculator &')  # Для Linux

time.sleep(4)  # Ждем, пока калькулятор откроется

# Функция для нажатия кнопки
def click_button(image_name):
    button_location = pyautogui.locateOnScreen(f'images/{image_name}', confidence=0.9)
    if button_location is not None:
        pyautogui.click(button_location)
    else:
        raise pyautogui.ImageNotFoundException(f"Image '{image_name}' not found on the screen.")

# Нажимаем кнопки для 12 + 7
click_button('button_1.png')  # Нажимаем '1'
click_button('button_2.png')  # Нажимаем '2'
click_button('button_plus.png')  # Нажимаем '+'
click_button('button_7.png')  # Нажимаем '7'
click_button('button_equals.png')  # Нажимаем '='
