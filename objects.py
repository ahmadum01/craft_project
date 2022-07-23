from items import Ingredient, Slot
from shapes import Rectangle

ingredient_A_1 = Ingredient(
    type_='A',
    level='1',
    x=100,
    y=100,
)

ingredient_A_2 = Ingredient(
    type_='A',
    level='2',
    x=100,
    y=250,
)

ingredient_b_3 = Ingredient(
    type_='b',
    level='3',
    x=100,
    y=400,
)


slot_left = Slot(600, 400)
slot_right = Slot(1200, 400)
slot_bottom = Slot(900, 700)
result_slot = Slot(900, 400, 120)

craft_button = Rectangle(
    x=1350, 
    y=800, 
    w=100, 
    h=40,
)


SLOTS = [
    slot_left,
    slot_right,
    slot_bottom,
]

INGREDIENTS = [
    ingredient_A_1,
    ingredient_A_2,
    ingredient_b_3,
]

ELEMENTS_FOR_RENDER = [
    craft_button,
    result_slot,
] + SLOTS + INGREDIENTS
