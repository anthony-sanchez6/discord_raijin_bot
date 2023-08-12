
class Event:

    def __init__(self,name_of_event, date='not set') -> None:
        self.name_of_event = name_of_event
        self.date = date
        self.roster = [{}]
    
    def as_String(self) -> str:
        string = f"""
## {self.name_of_event}:
————————————————————
# When:
- {self.date}
————————————————————
# **Roles**:
**Tank:**
"""
        for user in self.roster:
             if user.get("role") == 'tank':
                  string += f"- {user.get('name')}"
        string += """
**HEAL:**
"""
        for user in self.roster:
             if user.get("role") == 'heal':
                  string += f"- {user.get('name')}"
        string+="""
**DPS:**
"""

        for user in self.roster:
             if user.get("role") == 'dps':
                  string += f"- {user.get('name')}"
        string+="""
————————————————————
# React to join:
**Roles**
- Tank = :shield:
- DPS = :crossed_swords:
- Heal = :helmet_with_cross:
"""
        return string