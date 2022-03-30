from trello import TrelloClient

class LeetcodeTrello(TrelloClient):

  BOARD_NAME = "Leetcode"
  LABEL_COLORS = ['green', 'yellow', 'orange', 'red', 'purple', 'blue', 'sky', 'lime', 'pink', 'black']
  COVER_COLORS = {
    "EASY": "green",
    "MEDIUM": "yellow",
    "HARD": "red"
  }


  def __init__(self, api_key, api_secret=None, token=None, token_secret=None):
    super().__init__(api_key, api_secret, token, token_secret)
    self.board, self.question_list = self.create_or_get_board()





  def create_or_get_board(self):
    """
    create or get board
    """
    print("Creating or getting board")
    boards = self.list_boards()

    for board in boards:
      if board.name == LeetcodeTrello.BOARD_NAME:
        print("Found board")
        question_lists = list(filter(lambda x:x.name, board.open_lists()))
        print(question_lists)
        if len(question_lists) == 0:
          question_lists.append(board.add_list('Questions', pos=0))

        return board, question_lists[0]

    print("Creating new Board")
    board = self.add_board(LeetcodeTrello.BOARD_NAME)
    self.clear_board(board.id)
    question_list = board.add_list("Questions", pos=0)

    return board, question_list





  def clear_board(self, board_id):
    """
    Clears all cards from a board.
    """
    board = self.get_board(board_id)
    labels = board.get_labels()
    for label in labels:
      board.delete_label(label.id)


    lists = board.open_lists()
    for list_ in lists:
      list_.close()


  def add_question(self, question, email):
    self.question_list.add_card(question, label = self.create_or_get_label(email))

  def mark_question_as_done(self,card_id, email):
    label = self.create_or_get_label(email)
    card = filter(lambda card: card.id == card_id, self.question_list.list_cards())[0]
    card.add_label(label)

  def get_all_questions(self, email):
    label = self.create_or_get_label(email)
    return self.question_list.list_cards()


  def get_all_member_mails(self):
    return [i.fetch().email for i in self.board.all_members()]


  def create_or_get_label(self, mail):
    label_list = filter(lambda x: x.name == mail, self.board.get_labels())
    if len(label_list) == 0:
      return self.board.add_label(mail, LeetcodeTrello.LABEL_COLORS[len(label_list)])

    return label_list[0]