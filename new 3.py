class Stu:
	name = "None"
	age = None
	xingbei = "None"	
	
print Stu.name
print Stu.age
print Stu.xingbei

Person = Stu

print Person.name
print Person.age
print Person.xingbei

Person.name = "XiaoMing"
Person.age = 15
Person.xingbei = "Man"

print Person.name
print Person.age
print Person.xingbei