from services.basecard import *

class Cards(BaseCard):
    def __init__(self, name, description, strength, health, manna):
        super().__init__(name, description, strength, health, manna)
        self.skill_use = False
        self.skill = False

    def set_skill(self, skill_name, skill_strength, skill_health, skill_manna):
        self.skill_name = skill_name
        self.skill_strength = skill_strength
        self.skill_health = skill_health
        self.skill_manna = skill_manna
        self.skill = True

    def to_json(self):
        return {
            "name": self.name,
            "description": self.description,
            "strength": self.strength,
            "health": self.health,
            "manna": self.manna,
            "skill": {
                "name":self.skill_name,
                "strength": self.skill_strength,
                "health": self.skill_health,
                "manna": self.skill_manna,
            }
        }