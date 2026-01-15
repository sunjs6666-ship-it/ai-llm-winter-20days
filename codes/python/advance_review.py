# 类与对象 + 异常处理
class User:
    def __init__(self, name, age):
        # 初始化用户属性
        self.name = name
        # 年龄合法性校验
        try:
            self.age = int(age)
            if self.age < 0 or self.age > 150:
                raise ValueError("年龄必须在 0-150 之间")
        except ValueError as e:
            print(f"用户 {name} 年龄初始化失败：{e}")
            self.age = None

    def get_user_info(self):
        """返回用户格式化信息"""
        if self.age:
            return f"姓名：{self.name}，年龄：{self.age} 岁"
        else:
            return f"姓名：{self.name}，年龄：无效"

# 实例化类并测试
if __name__ == "__main__":
    users = [("Alice", "20"), ("Bob", "200"), ("Charlie", "abc")]
    for name, age in users:
        user = User(name, age)
        print(user.get_user_info())