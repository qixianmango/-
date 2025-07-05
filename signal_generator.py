import numpy as np

def generate_sine_signal(duration, sampling_rate, frequency):
    """
    生成标准正弦信号 sin(100t)
    :param duration: 信号持续时间（秒）
    :param sampling_rate: 采样率（Hz）
    :param frequency: 信号频率（Hz）
    :return: 正弦信号
    """
    t = np.arange(0, duration, 1 / sampling_rate)
    signal = np.sin(2 * np.pi * frequency * t)
    return signal