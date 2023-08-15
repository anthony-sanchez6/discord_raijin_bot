from pprint import pprint
from re import match

class Event:

    def __init__(self,name_of_event, date='Not_Set') -> None:
        self.name_of_event = name_of_event
        self.date = date
        self.roster = []

    @staticmethod
    def parse_message_to_event(message_content:str):
        p_message = message_content.lower()
        if p_message.split(':')[0] == '# event':
                bad_chars = ['#', '-', "*", " ","————————————————————","\n"]
                for char in bad_chars:
                        p_message = p_message.replace(char,'')
                pattern = r'event:(.*)when:(.*)roles:tank:(.*)heal:(.*)dps:(.*)reacttojoin.*'
                regex = match(pattern=pattern,string=p_message)
                if regex:
                        event = Event(name_of_event=regex.group(1),date=regex.group(2))
                        tanks=(regex.group(3).split('@') if regex.group(3) != '' else [])
                        for user in tanks:
                                if user != '':
                                        event.roster.append({'name':user,'role':'tank'})
                        heals=(regex.group(4).split('@') if regex.group(4) != '' else [])
                        for user in heals:
                                if user != '':
                                        event.roster.append({'name':user,'role':'heal'})
                        dps=(regex.group(5).split('@') if regex.group(5) != '' else [])
                        for user in dps:
                                if user != '':
                                        event.roster.append({'name':user,'role':'dps'})
                        return event
                else:
                      print('Did not parser correctly!')
        else:
              print('String is not an event!')
                
    def as_String(self) -> str:

        string = f"""
# Event: **{self.name_of_event}**
————————————————————
## When: **{self.date}**
————————————————————
### **Roles**:
**Tank:**
"""
        for user in self.roster:
             if user.get("role") == 'tank':
                  string += f"- @{user.get('name')}\n"
        string += """
**HEAL:**
"""
        for user in self.roster:
             if user.get("role") == 'heal':
                  string += f"- @{user.get('name')}\n"
        string+="""
**DPS:**
"""

        for user in self.roster:
             if user.get("role") == 'dps':
                  string += f"- @{user.get('name')}\n"
        string+="""
————————————————————
### React to join:
**Roles**
- Tank = :shield:
- DPS = :crossed_swords:
- Heal = :helmet_with_cross:
"""
        return string
    
    def remove_user(self, reaction_emoji, user):
        if reaction_emoji == '🛡️':
                role = 'tank'
        elif reaction_emoji == '⚔️':
                role = 'dps'
        elif reaction_emoji == '⛑️':
                role = 'heal'
        for item in self.roster:
                print(item)
                print(user)
                if item.get('name') == user.name.lower() and item.get('role') == role:
                        self.roster.remove(item)
                        return self