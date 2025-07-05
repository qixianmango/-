import numpy as np

def hvpc_encode(data_matrix):
    """
    水平垂直奇偶校验码编码
    :param data_matrix: 输入数据矩阵
    :return: 编码后的数据矩阵
    """
    rows, cols = data_matrix.shape
    encoded_matrix = np.zeros((rows + 1, cols + 1), dtype=int)

    # 填充原始数据
    encoded_matrix[:rows, :cols] = data_matrix

    # 计算水平奇偶校验位
    for i in range(rows):
        encoded_matrix[i, cols] = np.sum(encoded_matrix[i, :cols]) % 2

    # 计算垂直奇偶校验位
    for j in range(cols):
        encoded_matrix[rows, j] = np.sum(encoded_matrix[:rows, j]) % 2

    # 计算总奇偶校验位
    encoded_matrix[rows, cols] = np.sum(encoded_matrix[:rows, :cols]) % 2

    return encoded_matrix