class Item:
    def __init__(self, **kwargs):
        self.name = ""
        self.cost = 0
        self.total_cost = 0
        
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
        self.parent_id_number_list = []
        self.child_id_number_list = []

        self.__dict__.update(kwargs)

    def debug_print(self):
        import pprint
        pprint.pprint(self.__dict__)

class Relic(Item):
    def __init__(self):
        super().__init__()
        self.is_active_item = False
        self.is_relic = True


class ActiveItem(Item):
    def __init__(self):
        super().__init__()
        self.is_active_item = False


class Consumable(ActiveItem):
    def __init__(self):
        super().__init__()
        self.is_consumable = True


class EffectComponent():
    def __init__(self) -> None:
        self.effect_components = []  # This would cover anything from damage, buff, debuff, healing
        

class Description():
    def __init__(self) -> None:
        self.text = None


class Effect():
    def __init__(self) -> None:
        self.description = None
        self.effect = None
