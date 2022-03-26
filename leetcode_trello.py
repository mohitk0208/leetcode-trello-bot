from trello import TrelloClient

class LeetcodeTrello(TrelloClient):

  board_name = "Leetcode"

  def __init__(self, api_key, api_secret=None, token=None, token_secret=None):
    super().__init__(api_key, api_secret, token, token_secret)
    self.board = self.create_or_get_board()




  def create_or_get_board(self):
    """
    create or get board
    """
    print("Creating or getting board")
    boards = self.list_boards()
    for board in boards:
      if board.name == LeetcodeTrello.board_name:
        question_list = list(map(lambda x:x.name, board.open_lists()))
        print(question_list)
        if "Questions" not in question_list:
          question_list = board.add_list('Questions')
        return board



    board = self.add_board(LeetcodeTrello.board_name)
    self.clear_board(board.id)
    board.add_list("Questions", pos=0)

    return board





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


  def add_question(self, question):

    question_list = self.board.all_lists()
    question_list.add_card(question)

  def mark_question(self,card_id, label):
    question_list = self.board.all_lists()[-1]

    question_list.list_cards(query={label: [label]})
    pass

  def get_all_questions(self, label):

    self.board.list_cards()
    pass

  def get_all_member_mails(self):
    return [i.email for i in self.board.all_members().fetch()]

  def add_label(self, mail):
    self.board.add_label(mail)