import numpy as np

def decimate(signal, M):
    """
    对信号进行降采样
    :param signal: 输入信号
    :param M: 抽取因子
    :return: 抽取后的信号
    """
    return signal[::M]