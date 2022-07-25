from objects import SLOTS



def check_move_to_back(element):
    for slot in SLOTS:            
        if element.intersects(slot):
            return True
    return False
