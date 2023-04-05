import pandas as pd
import numpy as np


chat_id = 1105105523 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    array=x
    x_func=array-963
    x_func=np.log2(x_func)
    mu=np.mean(x_func)
    sigma=np.std(x_func)
    result = np.exp(mu + sigma**2 / 2.0)
    return result # Ваш ответ
