from Task_List import task_list

class player(object):

    """Class for containing player information such as doable tasks and reaper
    options"""

    def __init__(self, extended, group, choice):
        """Set the bossing options for the player

        Parameters
        ----------
        extended : boolean
            true if extended option enabled, false otherwise
        group : boolean
            true if group bosses option enabled, false otherwise
        choice : boolean
            true if Reaper's Choice is unlocked, false otherwise
        """
        self.adjust_options(extended, group, choice)

    def adjust_options(self, extended, group, choice):
        """ Change the boss options for the player

        Parameters
        ----------
        extended : boolean
            true if extended option is enabled, false otherwise
        group : boolean
            true if group bosses option enabled, false otherwise
        choice : boolean
            true if Reaper's Choice is unlocked, false otherwise
        """
        self._extended = extended
        self._group = group
        self._choice = choice

    def print_options(self):
        """ Prints the current player options
        """
        if(self._extended):
            print("Extended tasks are enabled")
        if(self._group):
            print("Group tasks are enabled")
        if(not (self._extended or self._group)):
            print("No options are enabled")
        if(self._choice):
            print("Reaper's Choice is unlocked")
        else:
            print("Reaper's choice is not unlocked")

    def create_lists(self, skip_tasks):
        """ Creates the player's task list

        Parameters
        ----------
        skip_tasks : list of strings
            list of bosses the player does not wish to kill
        """
        self._tasks = task_list(self._group, skip_tasks)

    def optimize_lists(self):
        """ Optimize the players skip list based on their preferences
        """
        pass

    def print_expected_values(self):
        """ Print the expected value for some specific case
        """
        solo_list = task_list(False, [])._do_list
        group_list = task_list(True, [])._do_list
        i = 0
        sum = 0
        for boss, task in solo_list.items():
            sum += task.get_points(0)
            i += 1
        print("Expected Value for no options always accepting the first task "
              "is:")
        print(sum/i)

        i = 0
        sum = 0
        for boss, task in solo_list.items():
            sum += task.get_points(1)
            i += 1
        print("Expected Value for extended tasks always accepting the first "
              "task is:")
        print(sum/i)

        i = 0
        sum = 0
        for boss, task in group_list.items():
            sum += task.get_points(2)
            i += 1
        print("Expected Value with both options always accepting the first "
              "task is:")
        print(sum/i)
