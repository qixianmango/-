import numpy as np
from collections import Counter
from dahuffman import HuffmanCodec


def non_uniform_quantization(signal, levels):
    """
    非均匀量化
    :param signal: 输入信号
    :param levels: 量化级别
    :return: 量化后的信号
    """
    quantized_signal = np.digitize(signal, bins=np.linspace(signal.min(), signal.max(), levels))
    return quantized_signal

def huffman_encode(signal):
    """
    霍夫曼编码
    :param signal: 输入信号
    :return: 编码后的信号和编码器
    """
    freq = Counter(signal)
    codec = HuffmanCodec.from_data(signal)  # 创建霍夫曼编码器
    encoded_signal = codec.encode(signal)  # 编码信号
    # 将bytes对象转换为numpy数组
    encoded_array = np.frombuffer(encoded_signal, dtype=np.uint8)
    return encoded_array, codec  # 返回编码后的信号和编码器

def huffman_decode(encoded_signal, codec):
    """
    霍夫曼解码
    :param encoded_signal: 编码后的信号
    :param codec: 霍夫曼编码器
    :return: 解码后的信号
    """
    # 将numpy数组转换回bytes对象
    encoded_bytes = encoded_signal.tobytes()
    decoded_signal = codec.decode(encoded_bytes)  # 解码信号
    return decoded_signal