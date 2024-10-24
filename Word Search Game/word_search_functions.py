'''A board is a list of list """A board is a list of list of str. For example, the board
    ANTT
    XSOB
is represented as the list
    [['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']]

A word list is a list of str. For example, the list of words
    ANT
    BOX
    SOB
    TO
is represented as the list
    ['ANT', 'BOX', 'SOB', 'TO']
'''

list_of_words = ['ANT', 'BOX', 'SOB','TO']
char_list_separated = [['A', 'N', 'T'], ['B', 'O', 'X'], ['S', 'O', 'B'], ['T', 'O']]

def is_valid_word(wordlist, word):
    """ (list of str, str) -> bool
    Return True if and only if word is an element of wordlist.
    >>> is_valid_word(['ANT', 'BOX', 'SOB', 'TO'], 'TO')
    True
    """
    return word in wordlist

def make_str_from_row(board, row_index):
    """ (list of list of str, int) -> str
    Return the characters from the row of the board with index row_index
    as a single string.
    >>> make_str_from_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 0)
    'ANTT'
    """
    concatenated_char = ''
    for chars in board[row_index]:
        concatenated_char += chars
    return concatenated_char

def make_str_from_column(board, column_index):
    """ (list of list of str, int) -> str
    Return the characters from the column of the board with index column_index
    as a single string.
    >>> make_str_from_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 1)
    'NS'
    """
    column_chars = ''
    for chars in board:
        column_chars += chars[column_index]
    return column_chars

def board_contains_word_in_row(board, word):
    """ (list of list of str, str) -> bool
    Return True if and only if one or more of the rows of the board contains
    word.
    Precondition: board has at least one row and one column, and word is a
    valid word.
    >>> board_contains_word_in_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'SOB')
    True
    """
    for row_index in range(len(board)):
        if word in make_str_from_row(board, row_index):
            return True
    return False

def board_contains_word_in_column(board, word):
    """ (list of list of str, str) -> bool
    Return True if and only if one or more of the columns of the board
    contains word.
    Precondition: board has at least one row and one column, and word is a
    valid word.
    >>> board_contains_word_in_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'NO')
    False
    """
    for column_index in range(len(board[0])):
        if word in make_str_from_column(board, column_index):
            return True
    return False

def board_contains_word(board, word):
    """ (list of list of str, str) -> bool
    Return True if and only if word appears in board.
    Precondition: board has at least one row and one column.
    >>> board_contains_word([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'ANT')
    True
    """
    if board_contains_word_in_row(board, word) or board_contains_word_in_column(board, word):
        return True
    return False

def word_score(word):
    """ (str) -> int
    Return the point value the word earns.
    Word length: < 3: 0 points
                 3-6: 1 point per character for all characters in word
                 7-9: 2 points per character for all characters in word
                 10+: 3 points per character for all characters in word
    >>> word_score('DRUDGERY')
    16
    """
    if len(word) < 3:
        return 0
    elif len(word) <= 6:
        return len(word)
    elif len(word) <= 9:
        return 2 * len(word)
    else:
        return 3 * len(word)

def update_score(player_info, word):
    """ ([str, int] list, str) -> NoneType
    player_info is a list with the player's name and score. Update player_info
    by adding the point value word earns to the player's score.
    >>> update_score(['Jonathan', 4], 'ANT')
    """
    points = word_score(word)
    player_info[1] += points

def num_words_on_board(board, words):
    """ (list of list of str, list of str) -> int
    Return how many words appear on board.
    >>> num_words_on_board([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], ['ANT', 'BOX', 'SOB', 'TO'])
    3
    """
    count = 0
    for word in words:
        if board_contains_word(board, word):
            count += 1
    return count

def read_words(file_path):
    """ (str) -> list of str
    Return a list of all words (with newlines removed) from the file specified by file_path.
    Precondition: Each line of the file contains a word in uppercase characters
    from the standard English alphabet.
    """
    words = []
    with open(file_path, 'r') as words_file:
        for line in words_file:
            words.append(line.strip())
    return words

def read_board(file_path):
    """ (str) -> list of list of str
    Return a board read from the file specified by file_path. The board file will contain
    one row of the board per line. Newlines are not included in the board.
    """
    board = []
    with open(file_path, 'r') as board_file:
        for line in board_file:
            row = list(line.strip())
            board.append(row)
    return board
