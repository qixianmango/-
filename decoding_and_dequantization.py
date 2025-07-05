import numpy as np

def huffman_decode(encoded_signal, freq):
    """
    霍夫曼解码
    :param encoded_signal: 编码后的信号
    :param freq: 符号频率
    :return: 解码后的信号
    """
    huffman = HuffmanCoding()
    decoded_signal = huffman.decode(encoded_signal, freq)
    return decoded_signal

def dequantize(quantized_signal, levels):
    """
    解量化
    :param quantized_signal: 量化后的信号
    :param levels: 量化级别
    :return: 解量化后的信号
    """
    dequantized_signal = np.linspace(0, 1, levels)[quantized_signal]
    return dequantized_signal