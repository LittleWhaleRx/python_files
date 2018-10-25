# 拾遗
- 组合
    - 把类的实例化放到新类里面
            
            // 乌龟类
            class Turtle:
                def __init__(self, x):
                    self.num = x
            // 鱼类
            class Fish:
                def __init__(self, x):
                    self.num = x
            // 水池类
            class Pool:
                def __init__(self, x, y):
                    self.turtle = Turtle(x)        // 组合乌龟类进来
                    self.fish = Fish(y)        // 组合鱼类进来
                 
                def print_num(self):
                    print("水池里总共有乌龟 %d 只，小鱼 %d 条！" % (self.turtle.num, self.fish.num))
            
            pool = Pool(1, 10)
            pool.print_num()

- 类、类对象和实例对象
    - 如果属性的名字和方法相同，那么属性会覆盖方法
    - 不要试图在一个类里面定义出所有能想到的特性和方法，应该利用继承和组合机制来进行扩展。
    - 用不同的词性命名，如属性名用名词，方法名用动词
- 到底什么是绑定
    - Python严格要求方法需要有实例才能被调用，这种限制其实就是Python所谓的绑定概念
    - 编程中多使用实例属性，而不要使用类属性