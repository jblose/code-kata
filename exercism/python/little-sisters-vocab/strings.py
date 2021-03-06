def add_prefix_un(word):
    """

    :param word: str of a root word
    :return:  str of root word with un prefix

    This function takes `word` as a parameter and
    returns a new word with an 'un' prefix.
    """
    return "un" + word


def make_word_groups(vocab_words):
    """

    :param vocab_words: list of vocabulary words with a prefix.
    :return: str of prefix followed by vocabulary words with
             prefix applied, separated by ' :: '.

    This function takes a `vocab_words` list and returns a string
    with the prefix  and the words with prefix applied, separated
     by ' :: '.
    """
    prefix = ""
    result = ""
    len_of_list = len(vocab_words)
    print(len_of_list)
    for x, word in enumerate(vocab_words):
        if x == 0:
            prefix = word
            result = word
        else:
            result = result + prefix + word
        if x < len_of_list - 1:
            result = result + " :: "

    return result


def remove_suffix_ness(word):
    """

    :param word: str of word to remove suffix from.
    :return: str of word with suffix removed & spelling adjusted.

    This function takes in a word and returns the base word with `ness` removed.
    """
    snipped_word = word[: word.find("ness")]
    if snipped_word.endswith("i"):
        return snipped_word[: snipped_word.find("ness")] + "y"

    return snipped_word


def noun_to_verb(sentence, index):
    """

    :param sentence: str that uses the word in sentence
    :param index:  index of the word to remove and transform
    :return:  str word that changes the extracted adjective to a verb.

    A function takes a `sentence` using the
    vocabulary word, and the `index` of the word once that sentence
    is split apart.  The function should return the extracted
    adjective as a verb.
    """
    sentence = sentence.strip(".")
    list_sentence = sentence.split(" ")
    indexedWord = list_sentence[index]

    return indexedWord + "en"
