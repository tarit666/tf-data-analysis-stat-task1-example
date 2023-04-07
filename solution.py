import pandas as pd
import numpy as np


chat_id = 681730925 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы 
    for element in x:
      element = element/np.power(51, 2)
    grade = len(x)/sum(x)
    return grade # Ваш ответ
