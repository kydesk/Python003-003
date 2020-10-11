
from abc import ABCMeta, abstractmethod

# 不允许被实例化
# 动物类要求定义“类型”、“体型”、“性格”、“是否属于凶猛动物”四个属性，是否属于凶猛动物的判断标准是：“体型 >= 中等”并且是“食肉类型”同时“性格凶猛”。
class Animal(metaclass=ABCMeta):

    def __init__(self, name, ani_type, size, character):
        self.name = name
        self.ani_type = ani_type
        self.size = size
        self.character = character
    
    @property
    def is_fierce(self):
        if (self.size == '中等' or self.size == '大') and self.ani_type == '食肉' and self.character == '凶猛':
            return True
        else:
            return False

    @property
    def is_pet(self):
        if self.character == "凶猛":
            return False
        else:
            return True

# 猫类要求有“叫声”、“是否适合作为宠物”以及“名字”三个属性，其中“叫声”作为类属性，除凶猛动物外都适合作为宠物，猫类继承自动物类。
class Cat(Animal):
    ani_sound = 'meow'
    def __init__(self, name, ani_type, size, character):
        super().__init__(name, ani_type, size, character)
    

# 狗类属性与猫类相同，继承自动物类。
class Dog(Animal):
    ani_sound = 'bow-wow'
    def __init__(self, name, ani_type, size, character):
        super().__init__(name, ani_type, size, character)

# 动物园类要求有“名字”属性和“添加动物”的方法，“添加动物”方法要实现同一只动物（同一个动物实例）不能被重复添加的功能。
class Zoo():
    def __init__(self, name):
        self.name = name
        self.animals = []

    def add_animal(self, animal):
        if animal not in self.animals:
            self.animals.append(animal)
            setattr(self, animal.__class__.__name__, 'yes')
        else:
            print(f'{animal.name}已经有了，不能重复添加！')

if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    # 增加一只猫到动物园
    z.add_animal(cat1)
    # 动物园是否有猫这种动物
    have_cat = hasattr(z, 'Cat')

    if have_cat:
        print("动物园有猫")



