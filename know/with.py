class MyContextManager:
    def __enter__(self):
        print("Entering the context...")
        return "Resource"  # 返回值会赋给 as 后的变量

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context...")
        if exc_type is not None:
            print(f"An exception occurred: {exc_value}")
        # 可以选择返回 True 来抑制异常传播
        return True

with MyContextManager() as resource:
    print(f"Using {resource}")
    # 可以在这里测试抛出异常，比如：raise ValueError("An error")
    # raise ValueError("error")
