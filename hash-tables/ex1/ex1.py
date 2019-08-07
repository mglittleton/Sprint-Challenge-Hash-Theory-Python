#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    # make sure hash table is big enouogh for all weights, if necessary
    while length > ht.capacity * 0.7:
        ht = hash_table_resize(ht)
    
    # loop through weights
    for i in range(len(weights)):
        # take off current weight from limit
        balance = limit - weights[i]
        balance_index = hash_table_retrieve(ht, balance)
        # if the balance does not exist, add that weight as a future possibility for the next check
        if balance_index is None:
            hash_table_insert(ht, weights[i], i)
        # if there is a pair, return it in the correct format 
        elif balance > weights[i]:
            print ("balance",balance, "weight", weights[i])
            return (balance_index, i)
        else:
            print ("balance",balance, "weight", weights[i])
            return (i, balance_index)
    
    # return None if no pair is ever found
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0]) + " " + str(answer[1]))
    else:
        print("None")


print_answer(get_indices_of_item_weights([12, 6, 7, 14, 19, 3, 0, 25, 40], 9, 7))