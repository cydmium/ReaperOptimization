from Tasks import task
from Color import color


class task_list(object):

    """Contains the list of tasks to do and to skip"""

    def __init__(self, group, skip_tasks):
        """Initializes all the tasks, and removes the skip tasks

        Parameters
        ----------
        group : boolean
            true if group bosses are enabled, false otherwise
        skip_tasks : list of strings
            list of all tasks to remove
        """
        solo_bosses = [('Araxxi', [20, 25, 30]),
                       ('Barrows Brothers', [7, 8, 9]),
                       ('Black Stone Dragon', [15, 18, 21]),
                       ('Chaos Elemental', [10, 12, 14]),
                       ('Commander Zilyana', [12, 15, 18]),
                       ('Corporeal Beast', [12, 15, 18]),
                       ('Dagannoth Kings', [10, 12, 14]),
                       ('General Graardor', [12, 15, 18]),
                       ('Giant Mole', [7, 8, 9]),
                       ('Gregorovic', [18, 22, 26]),
                       ("Har'Aken", [15, 18, 21]),
                       ('Helwyr', [18, 22, 26]),
                       ('Kalphite Queen', [10, 12, 14]),
                       ('King Black Dragon', [7, 8, 9]),
                       ("Kree'Arra", [12, 15, 18]),
                       ("K'ril Tsutsaroth", [12, 15, 18]),
                       ('Legiones', [15, 18, 21]),
                       ('The Magister', [15, 18, 21]),
                       ('Queen Black Dragon', [10, 12, 14]),
                       ('Seiryu', [15, 18, 21]),
                       ('Telos', [23, 28, 33]),
                       ('Twin Furies', [18, 22, 26]),
                       ('TzTok-Jad', [10, 12, 14]),
                       ('Vindicta and Gorvek', [18, 22, 26])]

        group_bosses = [('Rise of the Six', [20, 25, 30]),
                        ('Kalphite King', [15, 18, 21]),
                        ('Nex', [17, 21, 25]),
                        ('Nex: Angel of Death', [25, 31, 37]),
                        ('Solak', [27, 33, 39]),
                        ('Vorago', [20, 25, 30])]

        self._group = group
        self._do_list = {}
        self._skip_list = {}

        for pair in solo_bosses:
            self._do_list.update({pair[0].lower(): task(pair[0], 'Solo',
                                  pair[1])})
        if(group):
            for pair in group_bosses:
                self._do_list.update({pair[0].lower(): task(pair[0], 'Group',
                                      pair[1])})

        for boss in skip_tasks:
            task_object = self._do_list.pop(boss.lower())
            self._skip_list.update({boss.lower(): task_object})

    def print_lists(self):
        """ Prints the list of tasks that should be done and should be skipped
        """
        print(color.BOLD + 'Bosses to Kill:' + color.END)
        for boss in self._do_list:
            print(boss)
        print('')
        print(color.BOLD + 'Bosses to Skip:' + color.END)
        for boss in self._skip_list:
                print(boss)
