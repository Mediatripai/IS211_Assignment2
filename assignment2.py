import argparse
import urllib.request
import logging
import datetime

logging.basicConfig(filename='errors.log', level=logging.ERROR,
                    format='Error processing line #%(linenum)s for ID #%(personId)')
logger = logging.getLogger('assignment2')


def downloadData(url):
    
    with urllib.request.urlopen(url) as response:
        response = response.read()

         
    return response


def processData(fileContent):
    personData = {}

      
    lines = fileContent.split("\n")

    
    lineNum = 0
    header = True

    for line in lines:
      
        if header:
            header = False
            continue

      
        if len(line) == 0:
            continue


        elements = line.split(",")
        personId = int(elements[0])
        name = elements[1]
        date_str = elements[2]

        try:
            birthday = datetime.datetime.strptime(date_str, '%d/%m/%Y')
            personData[personId] = (name, birthday)

        except ValueError:
            
            logger.error("Error processing line #{} for ID #{}".format(lineNum, personId))

        lineNum += 1

    return personData


def displayPerson(personId, personData):
    if personId in personData:
        name, birthday = personData[personId]
        print("Person #{} is {} with a birthday of {}".format(personId, name, birthday.strftime("%Y %m %d")))

    else:
        print("No user found with that ID")


def main(url):
    print(f"Running main with URL = {url}...")

    fileContent = downloadData(url)
    personData = processData(fileContent)

    while True:
        user_input = int(input("Enter an ID number to search for person or type 0 to exit: "))

        if user_input <= 0:
            break

        displayPerson(user_input, personData)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
    args = parser.parse_args()
    main(args.url)
