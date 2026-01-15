import pandas as pd
import os

class CSVDataProcessor:
    """CSV 数据处理工具类，实现读取、清洗、筛选、写入全流程"""

    def __init__(self, input_csv_path, output_csv_path):
        self.input_path = input_csv_path
        self.output_path = output_csv_path
        self.raw_data = None  # 原始数据
        self.cleaned_data = None  # 清洗后数据
        self.filtered_data = None  # 筛选后数据

    def read_csv(self):
        """读取 CSV 文件，捕获异常"""
        try:
            if not os.path.exists(self.input_path):
                raise FileNotFoundError(f"输入文件不存在：{self.input_path}")
            self.raw_data = pd.read_csv(self.input_path, encoding='utf-8')
            print(f"✅ 成功读取原始 CSV，共 {len(self.raw_data)} 行数据（含表头）")
            return True
        except Exception as e:
            print(f"❌ 读取 CSV 失败：{e}")
            return False

    def clean_data(self):
        """数据清洗：去除空值、去重"""
        try:
            if self.raw_data is None:
                raise ValueError("请先读取原始数据（调用 read_csv() 方法）")
            # 去除包含空值的行
            self.cleaned_data = self.raw_data.dropna()
            # 去除重复行（基于所有列）
            self.cleaned_data = self.cleaned_data.drop_duplicates()
            # 重置索引
            self.cleaned_data = self.cleaned_data.reset_index(drop=True)
            print(f"✅ 数据清洗完成，清洗后剩余 {len(self.cleaned_data)} 行数据")
            return True
        except Exception as e:
            print(f"❌ 数据清洗失败：{e}")
            return False

    def filter_data(self, age_threshold=20, target_cities=["Beijing", "Shanghai"]):
        """条件筛选：年龄 ≥ 阈值 且 城市在目标列表中"""
        try:
            if self.cleaned_data is None:
                raise ValueError("请先完成数据清洗（调用 clean_data() 方法）")
            # 条件筛选（确保 age 列为数值类型）
            self.cleaned_data['age'] = pd.to_numeric(self.cleaned_data['age'], errors='coerce')
            filter_condition = (self.cleaned_data['age'] >= age_threshold) & \
                               (self.cleaned_data['city'].isin(target_cities))
            self.filtered_data = self.cleaned_data[filter_condition].reset_index(drop=True)
            print(f"✅ 数据筛选完成，符合条件的数据共 {len(self.filtered_data)} 行")
            return True
        except Exception as e:
            print(f"❌ 数据筛选失败：{e}")
            return False

    def write_csv(self):
        """将筛选后的数据写入新 CSV 文件"""
        try:
            if self.filtered_data is None:
                raise ValueError("请先完成数据筛选（调用 filter_data() 方法）")
            # 写入 CSV，不包含索引列
            self.filtered_data.to_csv(self.output_path, index=False, encoding='utf-8')
            print(f"✅ 筛选后的数据已成功写入：{self.output_path}")
            return True
        except Exception as e:
            print(f"❌ 写入 CSV 失败：{e}")
            return False

    def run_full_process(self):
        """运行 CSV 处理全流程"""
        print("=" * 60)
        print("开始执行 CSV 数据全流程处理...")
        print("=" * 60)
        # 按顺序执行各步骤
        success = (self.read_csv() and
                   self.clean_data() and
                   self.filter_data() and
                   self.write_csv())
        print("=" * 60)
        if success:
            print("🎉 CSV 数据全流程处理完成！")
        else:
            print("❌ CSV 数据全流程处理失败，请检查日志！")
        print("=" * 60)

if __name__ == "__main__":
    # 配置文件路径（适配仓库目录结构）
    input_csv = "../../data/sample.csv"
    output_csv = "../../data/filtered_sample.csv"

    # 实例化处理器并运行全流程
    csv_processor = CSVDataProcessor(input_csv, output_csv)
    csv_processor.run_full_process()