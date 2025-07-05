import numpy as np

from scipy.signal import butter, filtfilt

def bandpass_filter(signal, cutoff_freq, sampling_rate):
    """
    带通滤波器
    :param signal: 输入信号
    :param cutoff_freq: 截止频率（[低频, 高频]）
    :param sampling_rate: 采样率
    :return: 滤波后的信号
    """
    nyq = 0.5 * sampling_rate
    low = cutoff_freq[0] / nyq
    high = cutoff_freq[1] / nyq
    b, a = butter(5, [low, high], btype='band')
    filtered_signal = filtfilt(b, a, signal)
    return filtered_signal