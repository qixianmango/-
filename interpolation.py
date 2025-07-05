import numpy as np

def interpolate(signal, L):
    """
    内插信号
    :param signal: 输入信号
    :param L: 内插因子
    :return: 内插后的信号
    """
    interpolated_signal = np.zeros(len(signal) * L)
    interpolated_signal[::L] = signal
    return interpolated_signal