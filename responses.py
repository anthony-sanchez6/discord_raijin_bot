from event import Event

def handle_response(message) -> str:
    p_message = message.lower().split(' ')
    if p_message[0] == 'hello':
        return 'Hey There Bitch!'
    if p_message[0] == '!create':
        if len(p_message) > 1:
            event = Event(name_of_event=p_message[1])
            return event.as_String()
        else:
            print(len(p_message))
            return "Can not create event missing title"

