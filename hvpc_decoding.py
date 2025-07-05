import numpy as np


def hvpc_decode(encoded_matrix):
    """
    水平垂直奇偶校验码解码
    :param encoded_matrix: 编码后的数据矩阵
    :return: 解码后的数据矩阵
    """
    rows, cols = encoded_matrix.shape
    decoded_matrix = encoded_matrix[:rows - 1, :cols - 1].astype(int)  # 确保是整数类型

    # 检查水平奇偶校验位
    for i in range(rows - 1):
        if np.sum(decoded_matrix[i, :]) % 2 != encoded_matrix[i, cols - 1]:
            decoded_matrix[i, :] ^= 1

    # 检查垂直奇偶校验位
    for j in range(cols - 1):
        if np.sum(decoded_matrix[:, j]) % 2 != encoded_matrix[rows - 1, j]:
            decoded_matrix[:, j] ^= 1

    return decoded_matrix