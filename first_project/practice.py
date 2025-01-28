simple_list=["bmw","benz","audi","subaru","maserati","volvo","ferrari","lambo"]
simple_list1=["dodge","bentley","kia","apple","roll","demn"]
con_list=list(("1",2,False))
print(simple_list[0])
print(type(simple_list))
print(con_list)
print(simple_list[-2:-1])
print(simple_list[:-1])
if "benzz" in simple_list:
	print("benz is in the list")
else:
	print("not in list")
    
simple_list[3]="skoda"
print(simple_list)
simple_list[3:5]=["chevorlet","suzuki","VW"]
print(simple_list)
simple_list.insert(0,"mahindra")
print(simple_list)
print(len(simple_list))
simple_list.append("RR")
print(simple_list)
simple_list.extend(simple_list1)
print(simple_list)
simple_list1.remove("roll")
print(simple_list1)
simple_list1.pop(1)
print(simple_list1)
del simple_list1[0]
print(simple_list1)
simple_list1.clear()
print(simple_list1)
