from objects import SLOTS

def check_affiliation_ingredient(element, slot):
    if len(slot.items) == 5 and element.slot is None:
        return False
    
    for s in slot.items:
        if element.level != s.level:
            return False
        
    return True


def check_move_to_back(element):
    for slot in SLOTS:            
        if element.intersects(slot):
            return True
    return False
