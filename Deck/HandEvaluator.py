from Cards.Card import Card, Rank

# TODO (TASK 3): Implement a function that evaluates a player's poker hand.
#   Loop through all cards in the given 'hand' list and collect their ranks and suits.
#   Use a dictionary to count how many times each rank appears to detect pairs, three of a kind, or four of a kind.
#   Sort these counts from largest to smallest. Use another dictionary to count how many times each suit appears to check
#   for a flush (5 or more cards of the same suit). Remove duplicate ranks and sort them to detect a
#   straight (5 cards in a row). Remember that the Ace (rank 14) can also count as 1 when checking for a straight.
#   If both a straight and a flush occur in the same suit, return "Straight Flush". Otherwise, use the rank counts
#   and flags to determine if the hand is: "Four of a Kind", "Full House", "Flush", "Straight", "Three of a Kind",
#   "Two Pair", "One Pair", or "High Card". Return a string with the correct hand type at the end.
def evaluate_hand(hand: list[Card]):

    ranks = []
    suits = []
    
    #Collect ranks and suits from the hand
    for card in hand:
        ranks.append(card.rank.value)
        suits.append(card.suit)

    #Count occurrences of each rank
    rank_counts = {}
    for rank in ranks:
        rank_counts[rank] = rank_counts.get(rank, 0) + 1

    counts = []
    for rank, count in rank_counts.items():
        counts.append(count)

    #Sort counts in descending order
    for i in range(len(counts)):
        for j in range(i + 1, len(counts)):
            if counts[i] < counts[j]:
                counts[i], counts[j] = counts[j], counts[i]

    #Check for flush
    suit_counts = {}
    for suit in suits:
        suit_counts[suit] = suit_counts.get(suit, 0) + 1

    is_flush = False 
    for suit,count in suit_counts.items():
        if count >= 5:
            is_flush = True
            break

    #Get unique ranks and sort them
    unique_ranks = list(set(ranks))

    #Sort unique ranks in ascending order
    for i in range(len(unique_ranks)):
        for j in range(i + 1, len(unique_ranks)):
            if unique_ranks[i] > unique_ranks[j]:
                unique_ranks[i], unique_ranks[j] = unique_ranks[j], unique_ranks[i]

    is_straight = False
    
    #Check for straight 
    for i in range(len(unique_ranks) - 4):
        if (unique_ranks[i] + 1 == unique_ranks[i + 1] and
            unique_ranks[i] + 2 == unique_ranks[i + 2] and
            unique_ranks[i] + 3 == unique_ranks[i + 3] and
            unique_ranks[i] + 4 == unique_ranks[i + 4]):
            is_straight = True
            break

    #Check Ace-low straight (A,2,3,4,5)
    if not is_straight and 14 in unique_ranks:
        if 2 in unique_ranks and 3 in unique_ranks and 4 in unique_ranks and 5 in unique_ranks:
            is_straight = True


    #Determine hand type
    if is_straight and is_flush:
        return "Straight Flush"
    elif len(counts) > 0 and counts[0] == 4:
        return "Four of a Kind"
    elif len(counts) > 1 and counts[0] == 3 and counts[1] >= 2:
        return "Full House"
    elif is_flush:
        return "Flush"
    elif is_straight:
        return "Straight"
    elif len(counts) > 0 and counts[0] == 3:
        return "Three of a Kind"
    elif len(counts) > 1 and counts[0] == 2 and counts[1] == 2:
        return "Two Pair"
    elif len(counts) > 0 and counts[0] == 2:
        return "One Pair"
    else:
        return "High Card"
    
    

