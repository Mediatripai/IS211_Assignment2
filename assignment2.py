import argparse
import urllib.request
import logging
import datetime

def downloadData(url):
   

    with urllib.request.urlopen(url) as response:
        csvData = response.read()
    return csvData

def error_logger(count, id_num):
    
    LOG_FILENAME = 'errors.log'
    logging.basicConfig(filename=LOG_FILENAME, level=logging.ERROR)
    assignment2 = logging.getLogger('assignment2')
    assignment2.error(f'Error processing line #{count} for ID #{id_num}.')

def processData(file_content):
    
    person_list = file_content.decode('ascii').split('\n')
    personData = {}
    count = 0
    header = True
    for person in person_list:
        if header:
            header = False
            continue
        if len(person) == 0:
            continue
        line = person.split(',')
        id_num = int(line[0])
        name = line[1]

        birth_date = line[2]
        count += 1
        try:
            format = '%d/%m/%Y'
            bd = datetime.datetime.strptime(birth_date, format)
        except Exception as err:
            error_logger(count, id_num)
        personData[id_num] = (name, bd)
    return personData

def displayPerson(id, personData):
  
    id_num = id
    personData = personData

    if id_num not in personData:
        print("No user found with that id")
        main(args.url)
    else:
        values = personData[id_num]
        name = values[0]
        date = values[1].strftime('%d/%m/%Y')

    print(f"Person #{id_num} is {name} with a birthday of {date}.")
    main(args.url)

def main(url):
    
    id_num = ''
    while id_num == '':
        try:
            id_num = int(input("Enter the ID number to search for a person or type 0 to exit: "))

        except Exception as err:
            print(err, "\nID number must be an integer.")
    if id_num <= 0:
        print("Goodbye.")

    else:
        displayPerson(id_num, processData(downloadData(url)))

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
    args = parser.parse_args()
    main(args.url)
