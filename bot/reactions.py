from re import match
from bot.event import Event

def reaction_add_handler(reaction,user):
    event = Event.parse_message_to_event(reaction.message.content)
    if reaction.emoji == '🛡️':
        event.roster.append({'name':user,'role':'tank'})
    elif reaction.emoji == '⚔️':
        event.roster.append({'name':user,'role':'dps'})
    elif reaction.emoji == '⛑️':
        event.roster.append({'name':user,'role':'heal'})
    return event.as_String()
    
def reaction_remove_handler(reaction,user):
    event = Event.parse_message_to_event(reaction.message.content)
    event.remove_user(reaction.emoji,user)
    return event.as_String()


