class Quote():
    def __init__(self,person,words):
        self.person = person
        self.words = words

    def who(self):
        return (self.person)

    def says(self):
        return (self.words) + '.'

class QuestionQuote(Quote):
    def says(self):
        return (self.words) + '?'

class ExclamationQuote(Quote):
    def says(self):
        return (self.words) + '!'

class BabblingBrook():
    def who(self):
        return 'Brook'
    
    def says(self):
        return 'Babble'


def who_says(obj):
    print(obj.who(),'says',obj.says())


hunter = Quote('Elmer Fudd',"I'm hunting wabbits")
who_says(hunter)
#print(hunter.who(),'says:',hunter.says())

hunted1 = QuestionQuote('Bugs Bunny',"What's up, doc")
who_says(hunted1)
#print(hunted1.who(),'Says:',hunted1.says())

hunted2 = ExclamationQuote('Daffy Duck',"It's a rabbit season")
who_says(hunted2)
#print(hunted2.who(),'Says:',hunted2.says())


brook = BabblingBrook()
who_says(brook)