from lxml import html
import requests

def printResults(results, total):
    print('total: {}'.format(total))

    for opp, result in sorted(sorted(results.items(), key=lambda rec:rec[1], reverse=True), key=lambda rec: rec[1][0] + rec[1][1] + rec[1][2], reverse=True):
        print(opp, result)

def parseData(records):
    ## Set up variables
    rec_dict = {}
    total = (0,0,0)

    ## Loop through the records,
    ## first parsing the result
    ## and combining them with pre-existing results of the same opponent
    for record in records:
        w_l_d = (0,0,0)
        if record[0] == 'Win' or record[0] == 'Bye':
            w_l_d = (1,0,0)
        elif record[0] == 'Loss':
            w_l_d = (0,1,0)
        elif record[0] == 'Draw':
            w_l_d = (0,0,1)

        total = tuple(sum(t) for t in zip(total, w_l_d))

        opp = ' '.join(record[1:])
        if opp in rec_dict:
            rec_dict[opp] = tuple(sum(t) for t in zip(rec_dict[opp], w_l_d))
        else:
            rec_dict[opp] = w_l_d

    return rec_dict, total

def getTxtData(URI):
    file_object = open(URI, "r")

    str = file_object.read()
    records = [x.split(' ') for x in str.split('\n')]

    return records

def getWebData(URL):
    page = requests.get(URL)
    tree = html.fromstring(page.content)

    print(page.content)

    resultsArray = []

    results = tree.xpath('//div[@class="MatchResult"]/text()')
    opps = tree.xpath('//div[@class="MatchOpponent"]/text()')

    for opp, result in zip(opps, results):
        resultsArray.append([result, opp])

    return resultsArray

def main():
    URI = input("Data path: ")
    records = getTxtData(URI)

    records = getWebData('http://www.wizards.com/Magic/PlaneswalkerPoints/History')

    results, total = parseData(records)
    printResults(results, total)

## Running the script
if __name__ == "__main__":
    main()