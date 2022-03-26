from os import getenv
from trello import TrelloClient

client = TrelloClient(
    api_key=getenv("TRELLO_API_KEY"),
    api_secret=getenv("TRELLO_API_SECRET"),
    token=getenv("TRELLO_API_TOKEN"),
    # token_secret=''
)

all_boards = client.list_boards()
last_board = all_boards
print(last_board.name)
