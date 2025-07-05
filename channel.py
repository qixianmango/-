import numpy as np

def add_awgn(signal, snr_db):
    """
    添加加性高斯白噪声
    :param signal: 输入信号
    :param snr_db: 信噪比（dB）
    :return: 加噪后的信号
    """
    snr_linear = 10 ** (snr_db / 10)
    noise_power = np.var(signal) / snr_linear
    noise = np.sqrt(noise_power) * np.random.randn(len(signal))
    return signal + noise