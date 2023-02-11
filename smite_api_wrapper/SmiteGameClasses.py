class Device:
    def __init__(self):
        self.name = ""
        self.cost = 0
        self.tier = 0
        self.image = None
        self.is_active_item = True

        self.description = ""
        self.extended_description = ""
        self.summary = ""

        self.id_number = 0
        self.child_item_id_number = 0

        self.restricted_roles = {}


class Item(Device):
    def __init__(self):
        super().__init__()

        self.is_glyph_upgrade = False
        self.is_starting_item = False
        self.stats = {}


class Active(Device):
    def __init__(self):
        super().__init__()


class Consumable(Device):
    def __init__(self):
        super().__init__()
