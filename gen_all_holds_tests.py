def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.
    :param hand: full yahtzee hand
    Returns a set of tuples, where each tuple is dice to hold
    """

    answer_set = {()}
    for item in hand:
        temp = set()
        for seq in answer_set:
            new_seq = list(seq)
            new_seq.append(item)
            temp.add(tuple(new_seq))
            temp.add(seq)
        answer_set = temp
    return answer_set

TEST_CASES = [
              tuple([]),
              tuple([2, 4]),
              tuple([2, 2]),
              tuple((1, 2, 2)),
              tuple([2, 3, 6]),
              tuple([2, 2, 2, 2, 2, 2]),
              tuple([1, 2, 3, 4, 5, 6]),
              tuple([1, 2, 2, 4, 4, 6])
]
