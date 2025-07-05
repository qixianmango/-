import numpy as np

def modulate(signal, carrier_frequency, sampling_rate):
    """
    调制信号
    :param signal: 输入信号
    :param carrier_frequency: 载波频率
    :param sampling_rate: 采样率
    :return: 调制后的信号
    """
    t = np.arange(len(signal)) / sampling_rate
    modulated_signal = signal * np.cos(2 * np.pi * carrier_frequency * t)
    return modulated_signal