'''
Атрибут класса
1. Публичный
2. Приватный
3. Защищенный

Атрибут экземпляра
1. Публичный
2. Приватный
3. Защищенный

Методы экземпляров

Класс метод

Статический метод
'''

class A:
    public_class_attr_A = 'public_class_attr_A'
    _protected_class_attr_A = '_protected_class_attr_A'
    __private_class_attr_A = '__private_class_attr_A'

    def __init__(self):
        self.public_object_attr_A = "public_object_attr_A"
        self.__private_object_attr_A = "__public_object_attr_A"
        self._protect_object_attr_A = "_protect_object_attr_A"

    def public_object_method(self):
        print("public_object_method")

    def _protect_object_method(self):
        print('_protect_object_method')

    def __private_object_method(self):
        print('__private_object_method')

    @staticmethod
    def static_method_class_A():
        print('This is static method class A')

    @classmethodmethod
    def class_method_class_A(cls):
        print('This is class method class A')



if __name__ == '__main__':
    a = A()
    print(a.public_class_attr_A)
    print(a.__private_class_attr_A)