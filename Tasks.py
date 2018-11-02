class Task(object):

    """Class for containing a boss, classification and number of points"""

    def __init__(self, name, classification, points):
        """ Assigns the name, boss classification, and number of reaper points

        Parameters
        ----------
        name: string
            Boss name
        classification: {'Solo', 'Group'}
            Whether the boss is a solo or group boss
        points: vector
            Reward points for each number of options

        """
        self._name = name.lower()
        self._classification = classification.lower()
        self._points = points

    def get_points(self, num_options):
        """ Return the number of points awarded for completion of the task

        Parameters
        ----------
        num_options: int
            Number of options used when determining tasks

        Returns
        -------
        int: Number of points awarded

        """
        return(self._points[num_options])

    def is_available(self, group_option):
        """ Determine whether the task can be given to the player

        Parameters
        ----------
        group_options: boolean
            True is the group option is enabled, false otherwise

        Returns
        -------
        boolean: true if the task can be given, false otherwise

        """
        if (self._classification is 'solo'):
            return(True)
        elif (group_option):
            return(True)
        else:
            return(False)
