# define the 'EXPECTED_BAKE_TIME' constant
EXPECTED_BAKE_TIME = 40

# consider defining the 'PREPARATION_TIME' constant
#       equal to the time it takes to prepare a single layer
PREPARATION_TIME = 2

# define the 'bake_time_remaining()' function
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int baking time already elapsed.
    :return: int remaining bake time derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


# define the 'preparation_time_in_minutes()' function
#       and consider using 'PREPARATION_TIME' here
def preparation_time_in_minutes(number_of_layers):
    """
    :param number_of_layers: int number of layers in the lasagna
    :return: int minutes it will take to prepare lasagna
    """
    return number_of_layers * PREPARATION_TIME


# define the 'elapsed_time_in_minutes()' function
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    :param number_of_layers: int number of layers the lasagna has
    :param elapsed_bake_time: int elapsed time the lasagna has been baking
    :return: int returns the current known elapsed time and adds the prep time
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
