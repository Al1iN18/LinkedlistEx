from linkedlist import LinkedList

stu1 = {"name": "alice"}
stu2 = {"name":"bob"}
        
stu3  = {"name":"3"}

my_class_list = LinkedList()

my_class_list.append(stu1)
my_class_list.append(stu2)
my_class_list.prepend(stu3)

print(my_class_list)

my_class_list.remove(stu2)

print(my_class_list)