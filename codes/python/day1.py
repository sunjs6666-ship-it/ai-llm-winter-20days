# 导入必要的库
import pandas as pd
import os


def read_and_print_top10_csv(file_path):
    """
    读取 CSV 文件并打印前 10 行数据
    :param file_path: CSV 文件路径
    :return: 无返回值，直接打印结果
    """
    # 第一步：检查文件是否存在
    if not os.path.exists(file_path):
        print(f"错误：找不到 CSV 文件，请检查路径是否正确 -> {file_path}")
        return

    # 第二步：读取 CSV 文件
    try:
        df = pd.read_csv(file_path, encoding='utf-8')
    except Exception as e:
        print(f"错误：读取 CSV 文件失败 -> {e}")
        return

    # 第三步：打印结果
    print(f"✅ CSV 文件读取成功，共包含 {len(df)} 行数据（含表头）")
    print("=" * 50)
    print("📄 CSV 文件前 10 行数据如下：")
    print("=" * 50)
    print(df.head(10))  # 打印前 10 行数据


if __name__ == "__main__":
    # 配置 CSV 文件路径（相对路径，适配仓库目录结构）
    csv_file_path = "../../data/sample.csv"

    # 调用函数执行任务
    read_and_print_top10_csv(csv_file_path)