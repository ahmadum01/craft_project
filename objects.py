from items import Ingredient, Slot, Inventory
from shapes import Rectangle
from tools import rel_x, rel_y

ingredient_a_1 = Ingredient(
    type_='A',
    level='1',
    x=100,
    y=100,
)

ingredient_b_2 = Ingredient(
    type_='B',
    level='2',
    x=100,
    y=250,
)

ingredient_c_3 = Ingredient(
    type_='C',
    level='3',
    x=100,
    y=400,
)

ingredient_d_4 = Ingredient(
    type_='D',
    level='4',
    x=100,
    y=550,
)

ingredient_e_1 = Ingredient(
    type_='E',
    level='1',
    x=100,
    y=700,
)

inventory = Inventory(
    x=25,
    y=50,
    w=rel_x(25),
    h=rel_y(90),
    fill=255,
)
crafting_frame = Rectangle(
    x=inventory.x + inventory.w + 20,
    y=inventory.y,
    w=rel_x(70),
    h=rel_y(90),
)
print(rel_x(50))

result_slot = Slot(
    x=crafting_frame.x + float(crafting_frame.w) / 2, 
    y=crafting_frame.y + float(crafting_frame.h) / 2 - 50, 
    r=120,
)

slot_left = Slot(
    x=crafting_frame.x + float(crafting_frame.w) / 2 - 300, 
    y=result_slot.y, 
)

slot_right = Slot(
    x=crafting_frame.x + float(crafting_frame.w) / 2 + 300, 
    y=result_slot.y, 

)

slot_bottom = Slot(
    x=crafting_frame.x + float(crafting_frame.w) / 2, 
    y=result_slot.y + 300, 
)


craft_button = Rectangle(
    x=rel_x(90), 
    y=rel_y(90), 
    w=100, 
    h=40,
)


SLOTS = [
    slot_left,
    slot_right,
    slot_bottom,
]

INGREDIENTS = [
    ingredient_a_1,
    ingredient_b_2,
    ingredient_c_3,
    ingredient_d_4,
    ingredient_e_1,
]

ELEMENTS_FOR_RENDER = [
    inventory,
    crafting_frame,
    craft_button,
    result_slot,
] + SLOTS + INGREDIENTS
