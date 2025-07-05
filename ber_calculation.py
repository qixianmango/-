import numpy as np

def calculate_ber(original_signal, received_signal):
    """
    计算误码率
    :param original_signal: 原始信号
    :param received_signal: 接收信号
    :return: 误码率
    """
    errors = np.sum(original_signal != received_signal)
    ber = errors / len(original_signal)
    return ber