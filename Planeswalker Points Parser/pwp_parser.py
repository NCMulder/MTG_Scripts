import re

class PlaneswalkerPointsParser():
    def get_points_array(self, points_string):
        pattern = re.compile(r'(\d\d\d\d-\d\d-\d\d)(.*)', re.MULTILINE)
        points_array = pattern.split(points_string)

        return points_array
    
    def parse_points_array(self, points_array):
        tupelized_array = zip(points_array[1::2], points_array[2::2])

        hilko = []
        for date, data in tupelized_array:
            fields = data.split('\n')
            print(f'At date {date}, fields are {fields}')

    def read_points_from_file(self, path):
        with open(path) as points_file:
            return points_file.read()

if __name__ == '__main__':
    pwp_parser = PlaneswalkerPointsParser()
    data = pwp_parser.read_points_from_file('pwp_all.txt')
    array = pwp_parser.get_points_array(data)
    pwp_parser.parse_points_array(array)
