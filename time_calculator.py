def add_time(start, duration, day=''):
    week_day_map = {'monday': 1, 'tuesday': 2, 'wednesday': 3,
                    'thursday': 4, 'friday': 5, 'saturday': 6, 'sunday': 7}
    week_days = ['monday', 'tuesday', 'wednesday',
                 'thursday', 'friday', 'saturday', 'sunday']

    start_split = start.split()
    am_pm = start_split[1].lower()
    start_list = start_split[0].split(':')
    duration_list = duration.split(':')

    minute = int(start_list[1]) + int(duration_list[1])

    hour = int(start_list[0]) + int(duration_list[0]) + minute // 60
    hour += 12 if am_pm == 'pm' else 0

    extra_days = hour // 24
    new_day = (week_day_map.get(day.lower(), 0) + extra_days - 1) % 7
    am_pm = 'PM' if(hour % 24 > 11) else 'AM'

    minute %= 60
    hour = (hour % 24) % 12
    hour = 12 if(hour == 0) else hour

    new_time = str(hour) + ':' + ('0' + str(minute) if minute <
                                10 else str(minute)) + ' ' + am_pm

    if(len(day) > 3):
        new_time += ', ' + week_days[new_day].capitalize()

    if(extra_days == 1):
        new_time += ' (next day)'
    elif(extra_days > 1):
        new_time += ' (' + str(extra_days) + ' days later)'

    return new_time


print(add_time("2:59 AM", "24:00", "saturDay"))
