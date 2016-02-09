"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""

# Used to increase the timeout, if necessary
# import codeskulptor
# codeskulptor.set_timeout(20)

import random


def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of outcomes of given length.
    """
    answer_set = {()}
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set


def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.
    :param hand: full yahtzee hand
    Returns an integer score
    """

    return max(hand.count(item)*item for item in hand)


def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """

    sequences = gen_all_sequences([_ for _ in range(1, num_die_sides+1)], num_free_dice)
    # print sequences
    # print "sum", sum(score(held_dice + seq) for seq in sequences)
    # print "count", len(sequences)

    return sum(score(held_dice + seq) for seq in sequences)/float(len(sequences))


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


def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the discarded dice are rolled.

    :param hand: full yahtzee hand
    :param num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    max_score = 0
    all_holds = gen_all_holds(hand)
    for hold in all_holds:
        exp_score = expected_value(hold, num_die_sides, len(hand) - len(hold))
        # print "hold:", hold, ", score: ", exp_score, ", num_free_dice", len(hand) - len(hold)
        if exp_score > max_score:
            max_score = exp_score
            hold_return = hold

    return (max_score, hold_return)


def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    # hand = (1, 1, 1, 5, 6)
    hand = tuple(random.randint(1, 6) for dummy in range(num_die_sides))
    # print hand
    hand_score, hold = strategy(hand, num_die_sides)
    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score
    # print score(hand)
    # print expected_value((2, 2), 6, 3)
    # print gen_all_holds(hand)


# run_example()

# import poc_holds_testsuite
# poc_holds_testsuite.run_suite(gen_all_holds)
