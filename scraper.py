from bs4 import BeautifulSoup
import requests as r
import csv

print("hello")


def get_fighter_matchups(fighter_id):
    page = r.get("http://www.sherdog.com/fighter/index?id={}".format(fighter_id), timeout=3).text
    soup = BeautifulSoup(page, 'html.parser')
    table = soup.find('div', {"class": "module fight_history"})
    fighter_name = soup.find('h1', {'itemprop': 'name'}).span.contents[0]
    fighter_table_prep = fighter_id, fighter_name
    cells = []

    event_date = 'NO FIGHTS FOUND'

    for row in table.findAll('tr')[1:]:
        result_cell, fighter_cell, event_cell, *blah = row.findAll('td')
        result = result_cell.span.contents[0]
        opponent_id_url = fighter_cell.contents[0]['href']
        opponent_id = int(opponent_id_url[opponent_id_url.rfind("-") + 1:])
        event_link = event_cell.contents[0]['href']
        event_date = event_cell.findAll('span')[-1].contents[0]
        fighter_out = (fighter_id, opponent_id, result, event_date, event_link)
        cells += [fighter_out]
    return fighter_table_prep, cells, event_date


def scrape():
    with open('text_num.txt', 'r') as f:
        contents = f.read()
        n = int(contents) - 1
        print('Start num = {}'.format(n))

    with open('match_csv3.csv', 'a') as match_table, \
            open('fighter_csv3.csv', 'a') as fighters_table, \
            open('errors_csv3.csv', 'a') as errors_table, \
            open('text_num.txt', 'w') as num_file:
        match_writer = csv.writer(match_table)
        fighter_writer = csv.writer(fighters_table)
        error_writer = csv.writer(errors_table)
        while True:
            try:
                fighter_table_prep, fight_results, first_fight = get_fighter_matchups(n)
                print(fighter_table_prep, first_fight)
                match_writer.writerows(fight_results)
                fighter_writer.writerow(fighter_table_prep)
            except AttributeError:
                error_writer.writerow([n, 'm'])

                if n % 1 == 0:
                    print('Failed to find fighter ID: {}'.format(n))
            except ValueError:
                print('Error seen on Fighter ID: {}'.format(n))
                error_writer.writerow([n, 'e'])
            except r.exceptions.Timeout:
                print('###### Requests Timeout!!', n)
                n -= 1
            except:
                print('unhandled exception')
                break
            n += 1
            num_file.seek(0)
            num_file.write(str(n))



scrape()