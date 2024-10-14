class Device:
    def __init__(self):
        self.name = ""
        self.cost = 0
        self.tier = 0
        self.image = None

        self.description = ""
        self.extended_description = ""
        self.summary = ""

        # Bools related to filtering
        self.is_active_item = False
        self.is_consumable = False
        self.is_relic = False

        self.related_roles = {}  # Contains roles that might be suggested item

        self.id_number = 0
        self.child_id_number_list = []


class Item(Device):
    def __init__(self):
        super().__init__()

        self.is_glyph_upgrade = False
        self.is_starting_item = False
        self.stats = {}


class Relic(Device):
    def __init__(self):
        super().__init__()
        self.is_active_item = False
        self.is_relic = True


class ActiveItem(Device):
    def __init__(self):
        super().__init__()
        self.is_active_item = False

        self.active_effect = None
        self.active_description = None


class Consumable(ActiveItem):
    def __init__(self):
        super().__init__()
        self.is_consumable = True


class EffectComponent():
    def __init__(self) -> None:
        self.effect_components = []
        

class Description():
    def __init__(self) -> None:
        self.text = None


class Effect():
    def __init__(self) -> None:
        self.description = None
        self.effect = None
