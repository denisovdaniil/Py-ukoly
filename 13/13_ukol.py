# 13_ukol.py

# kompozice

# vlak - vůz
# stát - prezident
# fabrika - výrobní hala - linka

class Factory:
    def __init__(self,name):
        self.name = name

class Shop_Floor:
    def __init__(self, name, factory: Factory):
        self.name = name
        self.factory = factory
        self.lines = set()

    def __str__(self):
        return self.name
           
    def build_line(self, line: 'Line'):
        line.set_shop_floor(self)
        self.lines.add(line)

    def deconstruct_line(self, line: 'Line'):
        self.lines.remove(line)

class Line:
    def __init__(self,name):
        self.name = name
        self.shop_floor = None
    def __str__(self):
        
        return self.name

    def __repr__(self):
        
        return f"Line('{self.name}')"

    def set_shop_floor(self, new_shop_floor):
        if self.shop_floor:
            self.shop_floor.deconstruct_line(self) 
        
        self.shop_floor = new_shop_floor


asc = Factory('Ascorium s.r.o.')
shop_floor_A = Shop_Floor('Shop Floor A', asc)
shop_floor_B = Shop_Floor('Shop Floor B', asc)

line1 = Line('Line 1')
line2 = Line('Line 2')

print(line1.shop_floor)
print(shop_floor_A.lines)

shop_floor_A.build_line(line1)

print(line1.shop_floor)
print(shop_floor_A.lines)


# dědičnost

# sporák (parent) - indukční sporák (child)
# žárovka (parent) - LED žárovka (child)
# operátor (parent) - floater (child) - master (child)
"""
class Operator:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        

    def demould(self):
        print("I am carrying panels")

class Floater(Operator):
    def __init__(self, first_name, last_name, line):
        super().__init__(first_name, last_name)

        self.line = line

    def serve_line(self):
        print("I am preparing the line")
        


class Master(Floater):
    def __init__(self, first_name, last_name, line, shop_floor):
        super().__init__(first_name, last_name, line)
        self.shop_floor = shop_floor
    def assign_staff(self):
        print("I am assigning staff on the lines")

"""
