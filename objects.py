from items import Ingredient, Slot, Inventory, Text, Button
from shapes import Rectangle
from tools import rel_x, rel_y, group_ingredients

title = Text(
    x=20,
    y=15,
    w=100,
    h=100,
    text='Craft',
    text_size=40,
    fill='#ff1100'
)

inventory = Inventory(
    x=25,
    y=80,
    w=rel_x(23),
    h=rel_y(85),
    fill=255,
    r=20,
)

crafting_frame = Rectangle(
    x=inventory.x + inventory.w + 20,
    y=inventory.y,
    w=rel_x(70),
    h=inventory.h,
    r=20,
)
a = 0
def hello():
    global a
    print(a)
    a += 1
    
crafting_button = Button(
    x=crafting_frame.x + crafting_frame.w - 100, 
    y=crafting_frame.y + crafting_frame.h - 40, 
    w=100, 
    h=40,
    text="Craft",
    action=hello,
    r=20,
)

result_slot = Slot(
    x=crafting_frame.x + float(crafting_frame.w) / 2, 
    y=crafting_frame.y + float(crafting_frame.h) / 2 - 100, 
    r=120,
)

slot_left = Slot(
    x=crafting_frame.x + float(crafting_frame.w) / 2 - 280, 
    y=result_slot.y, 
)

slot_right = Slot(
    x=crafting_frame.x + float(crafting_frame.w) / 2 + 280, 
    y=result_slot.y, 

)

slot_bottom = Slot(
    x=crafting_frame.x + float(crafting_frame.w) / 2, 
    y=result_slot.y + 280, 
)


SLOTS = [
    slot_left,
    slot_right,
    slot_bottom,
]

ingredients = [
    ('A', 1), ('B', 2), ('C', 3),
    ('D', 4), ('E', 1), ('A', 1),
    ('B', 2)
]


INGREDIENTS = []

for i, group in enumerate(group_ingredients(ingredients)):
    for ing in group:
        ingredient = Ingredient(
                           type=ing[0],
                           level=ing[1],
                           x=100,
                           y=150 + i * 100,
                           r=40,
                    )
        INGREDIENTS.append(ingredient)


ELEMENTS_FOR_RENDER = [
    title,
    inventory,
    crafting_frame,
    crafting_button,
    result_slot,
] + SLOTS + INGREDIENTS
