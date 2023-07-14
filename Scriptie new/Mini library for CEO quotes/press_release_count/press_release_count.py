class Word_count:
    def __init__(self):
        self.word_list_count = [('year', 0.9402985074626866),
 ('growth', 0.6952380952380952),
 ('strong', 0.6911764705882353),
 ('customers', 1.3333333333333333),
 ('fiscal', 1.3142857142857143),
 ('record', 3.2142857142857144),
 ('billion', 1.2571428571428571),
 ('revenue', 0.88),
 ('performance', 0.6349206349206349),
 ('business', 0.6190476190476191),
 ('cash', 2.125),
 ('results', 1.6111111111111112),
 ('cloud', 0.7272727272727273),
 ('delivered', 0.8518518518518519),
 ('continued', 5.25),
 ('sales', 0.5757575757575758)]

        self.word_dict_count = {'year': 0.9402985074626866,
 'growth': 0.6952380952380952,
 'strong': 0.6911764705882353,
 'customers': 1.3333333333333333,
 'fiscal': 1.3142857142857143,
 'record': 3.2142857142857144,
 'billion': 1.2571428571428571,
 'revenue': 0.88,
 'performance': 0.6349206349206349,
 'business': 0.6190476190476191,
 'cash': 2.125,
 'results': 1.6111111111111112,
 'cloud': 0.7272727272727273,
 'delivered': 0.8518518518518519,
 'continued': 5.25,
 'sales': 0.5757575757575758}

    def list_count(self):
        """
  Provide a list that shows the probability of a word and its occurence in a rising stock price


  :return: List of tuples. Each tuple has a word and its given probability of occurence of rising stock price
  :rtype: List
  """

        return self.word_list_count

    def dict_count(self):
        """
  Provide a dictionary that shows the probability of a word and its occurence in a rising stock price


  :return: Dictionary. Each key has a word and its value gives a probability of occurence of rising stock price
  :rtype: Dictionary
  """

        return self.word_dict_count


    def word_calculation(self, text):
         import spacy
         nlp = spacy.load("en_core_web_sm")
         count = 1
         doc = nlp(text)
         for word in doc:
              for j in self.word_list_count:
                   if str(word) == j[0]:
                        count = count * j[1]
         return count

    """
   Provide a value that shows the chance that a sequence of words occur in CEO quotes that have a rising stock price after a year
   Returns 1 if the sequence of words have no indication

   :return: Score
   :rtype: float
   """
