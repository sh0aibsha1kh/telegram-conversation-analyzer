import os
import datetime
from bs4 import BeautifulSoup

def calculate_overall_message_frequency():

    my_message_frequency = 0
    her_message_frequency = 0

    are_my_messages = False
    are_her_messages = False

    counter = 0

    for filename in os.listdir('data'):
        if 'messages' in filename:
            html = open('data/' + filename, 'r', encoding="utf8")
            soup = BeautifulSoup(html, 'html.parser')
            all_messages = soup.find_all(class_='message')

            for message in all_messages:
                message_soup = BeautifulSoup(str(message), 'html.parser')
                classes = message_soup.div['class']
                sender = message_soup.find_all(class_='from_name')
                
                if len(classes) == 3 and len(sender) != 0:
                    sender = sender[0].string
                    if 'S' in sender:
                        my_message_frequency += 1
                        are_my_messages = True
                        are_her_messages = False
                    elif 'Z' in sender:
                        her_message_frequency += 1
                        are_my_messages = False
                        are_her_messages = True
                if len(classes) == 4:
                    if are_my_messages:
                        my_message_frequency += 1
                    elif are_her_messages:
                        her_message_frequency += 1
            counter += 1
            print(counter)

    return my_message_frequency, her_message_frequency

def calculate_message_frequency_by_day_of_the_week():

    overall_message_frequency = {
        'MON': 0,
        'TUE': 0,
        'WED': 0,
        'THU': 0,
        'FRI': 0,
        'SAT': 0,
        'SUN': 0
    }

    my_message_frequency = {
        'MON': 0,
        'TUE': 0,
        'WED': 0,
        'THU': 0,
        'FRI': 0,
        'SAT': 0,
        'SUN': 0
    }

    her_message_frequency = {
        'MON': 0,
        'TUE': 0,
        'WED': 0,
        'THU': 0,
        'FRI': 0,
        'SAT': 0,
        'SUN': 0
    }

    are_my_messages = False
    are_her_messages = False

    for filename in os.listdir('data'):
        if 'messages' in filename:
            html = open('data/' + filename, 'r', encoding="utf8")
            soup = BeautifulSoup(html, 'html.parser')
            all_messages = soup.find_all(class_='message')

            for message in all_messages:
                message_soup = BeautifulSoup(str(message), 'html.parser')
                classes = message_soup.div['class']
                sender = message_soup.find_all(class_='from_name')
                date = message_soup.find_all(class_='date')

                if len(date) != 0:
                    date_soup = BeautifulSoup(str(date[0]), 'html.parser')
                    day, month, year = date_soup.div['title'].split(' ')[0].split('.')
                    day_of_week = datetime.date(int(year), int(month), int(day)).weekday()

                    if day_of_week == 0: 
                        overall_message_frequency['MON'] += 1
                    elif day_of_week == 1:
                        overall_message_frequency['TUE'] += 1
                    elif day_of_week == 2:
                        overall_message_frequency['WED'] += 1
                    elif day_of_week == 3:
                        overall_message_frequency['THU'] += 1
                    elif day_of_week == 4:
                        overall_message_frequency['FRI'] += 1
                    elif day_of_week == 5:
                        overall_message_frequency['SAT'] += 1
                    elif day_of_week == 6:
                        overall_message_frequency['SUN'] += 1

                    if len(classes) == 3 and len(sender) != 0:
                        sender = sender[0].string
                        if 'S' in sender:
                            if day_of_week == 0: 
                                my_message_frequency['MON'] += 1
                            elif day_of_week == 1:
                                my_message_frequency['TUE'] += 1
                            elif day_of_week == 2:
                                my_message_frequency['WED'] += 1
                            elif day_of_week == 3:
                                my_message_frequency['THU'] += 1
                            elif day_of_week == 4:
                                my_message_frequency['FRI'] += 1
                            elif day_of_week == 5:
                                my_message_frequency['SAT'] += 1
                            elif day_of_week == 6:
                                my_message_frequency['SUN'] += 1
                            are_my_messages = True
                            are_her_messages = False
                        elif 'Z' in sender:
                            if day_of_week == 0: 
                                her_message_frequency['MON'] += 1
                            elif day_of_week == 1:
                                her_message_frequency['TUE'] += 1
                            elif day_of_week == 2:
                                her_message_frequency['WED'] += 1
                            elif day_of_week == 3:
                                her_message_frequency['THU'] += 1
                            elif day_of_week == 4:
                                her_message_frequency['FRI'] += 1
                            elif day_of_week == 5:
                                her_message_frequency['SAT'] += 1
                            elif day_of_week == 6:
                                her_message_frequency['SUN'] += 1
                            are_my_messages = False
                            are_her_messages = True
                    if len(classes) == 4:
                        if are_my_messages:
                            if day_of_week == 0: 
                                my_message_frequency['MON'] += 1
                            elif day_of_week == 1:
                                my_message_frequency['TUE'] += 1
                            elif day_of_week == 2:
                                my_message_frequency['WED'] += 1
                            elif day_of_week == 3:
                                my_message_frequency['THU'] += 1
                            elif day_of_week == 4:
                                my_message_frequency['FRI'] += 1
                            elif day_of_week == 5:
                                my_message_frequency['SAT'] += 1
                            elif day_of_week == 6:
                                my_message_frequency['SUN'] += 1
                        elif are_her_messages:
                            if day_of_week == 0: 
                                her_message_frequency['MON'] += 1
                            elif day_of_week == 1:
                                her_message_frequency['TUE'] += 1
                            elif day_of_week == 2:
                                her_message_frequency['WED'] += 1
                            elif day_of_week == 3:
                                her_message_frequency['THU'] += 1
                            elif day_of_week == 4:
                                her_message_frequency['FRI'] += 1
                            elif day_of_week == 5:
                                her_message_frequency['SAT'] += 1
                            elif day_of_week == 6:
                                her_message_frequency['SUN'] += 1
            print(overall_message_frequency)
    return '====================' + str(my_message_frequency) + '\n' + str(her_message_frequency) + '\n' + str(overall_message_frequency)


def calculate_message_frequency_by_month():

    overall_message_frequency = {}
    my_message_frequency = {}
    her_message_frequency = {}

    are_my_messages = False
    are_her_messages = False

    for filename in os.listdir('data'):
        if 'messages' in filename:
            html = open('data/' + filename, 'r', encoding="utf8")
            soup = BeautifulSoup(html, 'html.parser')
            all_messages = soup.find_all(class_='message')

            for message in all_messages:
                message_soup = BeautifulSoup(str(message), 'html.parser')
                classes = message_soup.div['class']
                sender = message_soup.find_all(class_='from_name')
                date = message_soup.find_all(class_='date')

                if len(date) != 0:
                    date_soup = BeautifulSoup(str(date[0]), 'html.parser')
                    day, month, year = date_soup.div['title'].split(' ')[0].split('.')
                    if (month, year) not in overall_message_frequency:
                        overall_message_frequency[(month, year)] = 0
                    overall_message_frequency[(month, year)] += 1

                    if len(classes) == 3 and len(sender) != 0:
                        sender = sender[0].string
                        if 'S' in sender:
                            if (month, year) not in my_message_frequency:
                                my_message_frequency[(month, year)] = 0
                            my_message_frequency[(month, year)] += 1
                            are_my_messages = True
                            are_her_messages = False
                        elif 'Z' in sender:
                            if (month, year) not in her_message_frequency:
                                her_message_frequency[(month, year)] = 0
                            her_message_frequency[(month, year)] += 1
                            are_my_messages = False
                            are_her_messages = True
                    if len(classes) == 4:
                        if are_my_messages:
                            if (month, year) not in my_message_frequency:
                                my_message_frequency[(month, year)] = 0
                            my_message_frequency[(month, year)] += 1
                        elif are_her_messages:
                            if (month, year) not in her_message_frequency:
                                her_message_frequency[(month, year)] = 0
                            her_message_frequency[(month, year)] += 1
            print(overall_message_frequency)
        
    with open('test.csv', 'w') as f:
        for key in overall_message_frequency.keys():
            f.write("%s,%s,%s,%s\n"%(key,overall_message_frequency[key], my_message_frequency[key], her_message_frequency[key]))
            
    return '====================\n' + str(my_message_frequency) + '\n' + str(her_message_frequency) + '\n' + str(overall_message_frequency)
print(calculate_message_frequency_by_month())