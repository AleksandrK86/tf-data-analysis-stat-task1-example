import pandas as pd
import numpy as np


chat_id = 1105105523 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    return np.log(x-963).mean()
