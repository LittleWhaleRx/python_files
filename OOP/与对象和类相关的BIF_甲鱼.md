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
# 一些相关的BIF
- issubclass(calss,classinfo)
    - 如果class是classinfo的子类返回True
    - 一个类被认为是自身的子类
    - classinfo可以是一个类对象组成的元祖，只要class是其中任何一个候选类的子类，则返回True
    - 其他情况会返回类型错误Type error
    - 如果第一个对象不是class类型则永远返回Fales
    - 如果第二个参数不是类或者由类对象组成的远足，会抛出一个TypeError异常
- attr = attribute: 属性
    - hasattr(object,name)
        - 测试一个对象object里是否有指定的属性name
    - getattr(object,name[,default])
        - 返回对象指定的属性值name，如果没有这个属性而且设置了default的内容则会返回default
    - setattr(object,name,value)
        - 返回对象指定的属性值name，如果没有这个属性则会新建一个属性name并给他复制value
    - delattr(object,name)
        - 删除对象object中的属性name,如果没有会返回异常
- property(fget（获得属性） = None,fset（设置属性） = None,fdel（删除属性） = None,doc = None)
    - 通过属性来设置属性
