from re import match
from bot.event import Event

def reaction_handler(reaction,user):
    p_message = reaction.message.content.lower()
    test_string = p_message
    if p_message.split(':')[0] == '# event':
        bad_chars = ['#', '-', "*", " ","————————————————————","\n"]
        for char in bad_chars:
            test_string = test_string.replace(char, '')
        pattern = r'event:(.*)when:(.*)roles:tank:(.*)heal:(.*)dps:(.*)reacttojoin.*'
        regex = match(pattern=pattern,string=test_string)
        if regex:
            event = Event(name_of_event=regex.group(1),date=regex.group(2))
            
            tanks=(regex.group(3).split('@') if regex.group(3) is not '' else [])
            for user in tanks:
                event.roster.append(
                    {
                        'name':user,
                        'role':'tank'
                    }
                )
            heals=(regex.group(4).split('@') if regex.group(3) is not '' else [])
            for user in heals:
                event.roster.append(
                    {
                        'name':user,
                        'role':'heal'
                    }
                )
            dps=(regex.group(5).split('@') if regex.group(3) is not '' else [])
            for user in dps:
                event.roster.append(
                    {
                        'name':user,
                        'role':'dps'
                    }
                )
            
            if reaction.emoji == '🛡️':
                event.roster.append({'name':user,
                                     'role':'tank'})
            if reaction.emoji == '⚔️':
                event.roster.append({'name':user,
                        'role':'dps'})
            if reaction.emoji == '⛑️':
                event.roster.append({'name':user,
                        'role':'heal'})
            # event.roster.append({'name':'whyraijin','role':'tank'})
        return event.as_String()
            

