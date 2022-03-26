from os import getenv
from leetcode_trello import LeetcodeTrello

client = LeetcodeTrello(
    api_key=getenv("TRELLO_API_KEY"),
    api_secret=getenv("TRELLO_API_SECRET"),
    token=getenv("TRELLO_API_TOKEN")
    # token_secret=''
)



# all_boards = client.list_boards()[1]


# question_list = all_boards[1].all_lists()

# for i in question_list:
#     print(i.list_cards())

# client.clear_board(all_boards[1].id)
