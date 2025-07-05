import numpy as np
from signal_generator import generate_sine_signal
from decimation import decimate
from quantization_and_encoding import non_uniform_quantization, huffman_encode, huffman_decode
from hvpc_encoding import hvpc_encode
from modulation import modulate
from channel import add_awgn
from demodulation import demodulate
from demultiplexing import bandpass_filter
from hvpc_decoding import hvpc_decode
from decoding_and_dequantization import dequantize
from interpolation import interpolate
from ber_calculation import calculate_ber

def main():
    # 参数设置
    duration = 1  # 信号持续时间（秒）
    sampling_rate = 10000  # 采样率（Hz）
    signal_frequency = 100  # 信号频率（Hz）
    decimation_factor = 2
    quantization_levels = 8
    carrier_frequencies = [1000, 2000]  # 两路载波频率
    snr_db = 10  # 信噪比（dB）

    # 生成原始信号
    original_signal = generate_sine_signal(duration, sampling_rate, signal_frequency)

    # 抽取
    decimated_signal = decimate(original_signal, decimation_factor)

    # 量化与信源编码
    quantized_signal = non_uniform_quantization(decimated_signal, quantization_levels)
    encoded_signal, codec = huffman_encode(quantized_signal)  # 获取编码器

    # 动态计算目标形状的第一个维度
    target_rows = int(np.sqrt(len(encoded_signal)))
    while len(encoded_signal) % target_rows != 0:
        target_rows -= 1

    # 计算目标形状的第二个维度
    target_cols = len(encoded_signal) // target_rows

    # 重塑数组
    data_matrix = np.reshape(encoded_signal, (target_rows, target_cols))

    # 水平垂直奇偶校验码编码
    encoded_matrix = hvpc_encode(data_matrix)

    # 分路调制
    modulated_signals = []
    for freq in carrier_frequencies:
        modulated_signals.append(modulate(encoded_matrix.flatten(), freq, sampling_rate))

    # 合成多路信号
    combined_signal = np.sum(modulated_signals, axis=0)

    # 信道传输
    noisy_signal = add_awgn(combined_signal, snr_db)

    # 解复用与解调
    demodulated_signals = []
    for freq in carrier_frequencies:
        filtered_signal = bandpass_filter(noisy_signal, [freq - 100, freq + 100], sampling_rate)
        demodulated_signals.append(demodulate(filtered_signal, freq, sampling_rate))

    # 合并解调后的信号
    combined_demodulated_signal = np.sum(demodulated_signals, axis=0)

    # 确保combined_demodulated_signal是整数类型
    combined_demodulated_signal = np.round(combined_demodulated_signal).astype(int)

    # 水平垂直奇偶校验码解码
    decoded_matrix = hvpc_decode(np.reshape(combined_demodulated_signal, encoded_matrix.shape))

    # 信源解码与解量化
    decoded_signal = huffman_decode(decoded_matrix.flatten(), codec)  # 使用编码器解码

    # 确保decoded_signal中的值不会超出索引范围
    decoded_signal = np.mod(decoded_signal, quantization_levels)

    dequantized_signal = dequantize(decoded_signal, quantization_levels)

    # 内插
    interpolated_signal = interpolate(dequantized_signal, decimation_factor)

    # 计算误码率
    ber = calculate_ber(original_signal, interpolated_signal)

    print(f"误码率 (BER): {ber}")

if __name__ == "__main__":
    main()