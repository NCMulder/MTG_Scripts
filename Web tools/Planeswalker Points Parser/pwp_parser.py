import re
import sqlite3
import matplotlib.pyplot as plt
import pandas as pd


class PlaneswalkerPointsParser():
    def get_points_array(self, points_string):
        pattern = re.compile(r'(\d\d\d\d-\d\d-\d\d.*\n)', re.MULTILINE)
        points_array = pattern.split(points_string)

        return points_array

    def setup_db(self, path):
        cs = self.get_db_cursor(path)

        has_events = cs.execute(
            'SELECT name FROM sqlite_master '
            'WHERE type="table" AND name="events"'
        )

        if not has_events.fetchall():
            cs.execute(
                'CREATE TABLE events (sanctioning_number text PRIMARY KEY, '
                'date text, type text, multiplier int, player_count int, '
                'participation_points int, format text, location text, '
                'place int)'
            )

        has_matches = cs.execute(
            'SELECT name FROM sqlite_master '
            'WHERE type="table" AND name="matches"'
        )

        if not has_matches.fetchall():
            cs.execute(
                'CREATE TABLE matches (round int, result text, '
                'opponent text, event_number text, '
                'FOREIGN KEY(event_number) REFERENCES '
                'events(sanctioning_number))'
            )

        cs.commit()
        return cs

    def get_db_cursor(self, path):
        return sqlite3.connect(path)

    def get_regex_from_string(self, string, pattern_string):
        pattern = re.compile(pattern_string)
        result = pattern.search(string)
        if result:
            return result.group(1).strip()
        else:
            return None

    def parse_points_array(self, points_array):
        tupelized_array = zip(points_array[1::2], points_array[2::2])

        cs = self.get_db_cursor('niels_points.db')

        # Get the already handled events
        sns_cs = cs.execute('SELECT sanctioning_number FROM events')
        sns = [sn[0] for sn in sns_cs.fetchall()]

        count = 0
        for date_title, data in tupelized_array:
            date = date_title[0:10].strip()
            title = date_title[10:].strip()

            sn = self.get_regex_from_string(data, r'Sanctioning Number:(.*)')

            if not sn:
                # Achievement entry
                continue

            # Check if this event has been recorded already
            if sn in sns:
                continue

            et = self.get_regex_from_string(data, r'Event Type:(.*)')
            mp = self.get_regex_from_string(data, r'Event Multiplier:(.*)')
            pc = self.get_regex_from_string(data, r'Players:(.*)')
            pp = self.get_regex_from_string(data, r'Participation Points:(.*)')
            fm = self.get_regex_from_string(data, r'Format:(.*)')
            lc = self.get_regex_from_string(data, r'Location:(.*)')
            pl = self.get_regex_from_string(data, r'Place:(.*)')
            yp = self.get_regex_from_string(data, r'Yearly:(.*)')
            lp = self.get_regex_from_string(data, r'Lifetime:(.*)')

            cs.execute(
                'INSERT INTO events VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
                [sn, date, et, mp, pc, pp, fm, lc, pl]
            )
            count += 1

            mh_pattern = re.compile(
                r'Match History:\n((?:\d|.*\n)*)Planes', re.MULTILINE
            )
            mh_result = mh_pattern.search(data)
            if mh_result:
                mh = mh_result.group(1)
                mhg_pattern = re.compile(r'(\d.*\n[^\d]*)')
                mhg = mhg_pattern.findall(mh)
                for single_match in mhg:
                    mhg_array = single_match.split('\t')
                    rnd = mhg_array[0]
                    result = mhg_array[1]
                    points = mhg_array[2]
                    if len(mhg_array) > 3:
                        opponent = mhg_array[3].strip()
                    if not opponent:
                        opponent = 'Unknown'
                    if result == 'Bye':
                        continue
                    cs.execute(
                        'INSERT INTO matches VALUES (?, ?, ?, ?)',
                        [rnd, result, opponent, sn]
                    )
            else:
                mh = None

        cs.commit()

        if count > 0:
            print(f'Imported {count} new events!')
        else:
            print('No new events found')

    def read_points_from_file(self, path):
        with open(path) as points_file:
            return points_file.read()

    def write_all_results(self, path):
        base_query = 'SELECT result, COUNT(result) AS Total FROM matches WHERE opponent=="{0}" GROUP BY result'

        cs = self.get_db_cursor(path)

        opps = cs.execute('SELECT DISTINCT opponent FROM matches')

        table = []
        rowlabels = []

        for opponent_row in opps.fetchall():
            opponent = opponent_row[0].replace('\n', ', ')
            results = cs.execute(base_query.format(opponent)).fetchall()

            if not results:
                continue

            losses = 0
            wins = 0
            draws = 0

            for result_type, result_count in results:
                if result_type == 'Loss':
                    losses = result_count
                elif result_type == 'Win':
                    wins = result_count
                elif result_type == 'Draw':
                    draws = result_count
            table.append([wins, losses, draws])
            rowlabels.append(opponent)
            
            print(f'{opponent}: {results}')
        
        fig, ax = plt.subplots()
        fig.patch.set_visible(False)
        ax.axis('off')
        ax.axis('tight')

        df = pd.DataFrame(table, columns=['Wins', 'Losses', 'Draws'])

        ax.table(cellText=df.values, rowLabels=rowlabels, colLabels=df.columns, loc='center')
        plt.show()


if __name__ == '__main__':
    pwp_parser = PlaneswalkerPointsParser()
    data = pwp_parser.read_points_from_file('20200205.txt')
    array = pwp_parser.get_points_array(data)

    pwp_parser.setup_db('niels_points.db')

    pwp_parser.parse_points_array(array)
    pwp_parser.write_all_results('niels_points.db')
