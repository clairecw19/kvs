
from otree.api import *
c = cu

doc = ''
class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = 2
    num_rounds = 1
    US = 100000
    ETH = 200
    pricesDay1_10 = (194.39, 197.78, 196.78, 196.86, 215.55, 206.27, 211.98, 214.15, 210.06, 206.94)
def creating_session(subsession):
    session = subsession.session
    subsession.group_randomly()
class Subsession(BaseSubsession):
    time1 = models.FloatField()
class Group(BaseGroup):
    pass
class Player(BasePlayer):
    US = models.FloatField(initial=100000)
    ETH = models.FloatField(initial=200)
    ROI = models.FloatField()
    ROI2 = models.FloatField()
    ROI3 = models.FloatField()
    US2 = models.FloatField(initial=100000)
    ETH2 = models.FloatField(initial=200)
    Asset_day1 = models.FloatField()
    Asset_day10 = models.FloatField()
    value_total_asset = models.FloatField(initial=0)
    Name = models.StringField(label='Your name')
    Sig = models.StringField(label='Your Signature')
    Email = models.StringField(label='Your Email Address')
    Date = models.StringField(label='Date')
    one = models.StringField(choices=[['T', 'T'], ['F', 'F']], label='1) I usually get what I want in life. ', widget=widgets.RadioSelect)
    two = models.StringField(choices=[['T', 'T'], ['F', 'F']], label='2) I need to be kept informed about news events.', widget=widgets.RadioSelect)
    three = models.StringField(choices=[['T', 'T'], ['F', 'F']], label='3) I never know where I stand with other people.', widget=widgets.RadioSelect)
    four = models.StringField(choices=[['T', 'T'], ['F', 'F']], label='4) I do not really believe in luck or chance.', widget=widgets.RadioSelect)
    five = models.StringField(choices=[['T', 'T'], ['F', 'F']], label='5) I think that I could easily win a lottery.', widget=widgets.RadioSelect)
    six = models.StringField(choices=[['T', 'T'], ['F', 'F']], label='6) If I do not succeed in a task, I tend to give up.', widget=widgets.RadioSelect)
    seven = models.StringField(choices=[['T', 'T'], ['F', 'F']], label='7) I usually convince others to do things my way.', widget=widgets.RadioSelect)
    eight = models.StringField(choices=[['T', 'T'], ['F', 'F']], label='8) People make a difference in controlling crime. ', widget=widgets.RadioSelect)
    nine = models.StringField(blank=True, choices=[['T', 'T'], ['F', 'F']], label='9) The success I have is largely a matter of chance.', widget=widgets.RadioSelect)
    ten = models.StringField(choices=[['T', 'T'], ['F', 'F']], label='10) Marriage is largely a gamble for most people.', widget=widgets.RadioSelect)
    eleven = models.StringField(choices=[['T', 'T'], ['F', 'F']], label='11) People must be the master of their own fate. ', widget=widgets.RadioSelect)
    twelve = models.StringField(choices=[['T', 'T'], ['F', 'F']], label='12) It is not important for me to vote.', widget=widgets.RadioSelect)
    thirteen = models.StringField(choices=[['T', 'T'], ['F', 'F']], label='13) My life seems like a series of random events. ', widget=widgets.RadioSelect)
    fourteen = models.StringField(choices=[['T', 'T'], ['F', 'F']], label='14) I never try anything that I am not sure of.', widget=widgets.RadioSelect)
    fifteen = models.StringField(choices=[['T', 'T'], ['F', 'F']], label='15) I earn the respect and honors I receive. ', widget=widgets.RadioSelect)
    sixteen = models.StringField(choices=[['T', 'T'], ['F', 'F']], label='16) A person can get rich by taking risks.', widget=widgets.RadioSelect)
    seventeen = models.StringField(choices=[['T', 'T'], ['F', 'F']], label='17) Leaders are successful when they work hard. ', widget=widgets.RadioSelect)
    eighteen = models.StringField(choices=[['T', 'T'], ['F', 'F']], label='18) Persistence and hard work usually lead to success.', widget=widgets.RadioSelect)
    nineteen = models.StringField(choices=[['T', 'T'], ['F', 'F']], label='19) It is difficult to know who my real friends are.', widget=widgets.RadioSelect)
    twenty = models.StringField(choices=[['T', 'T'], ['F', 'F']], label='20) Other people usually control my life.', widget=widgets.RadioSelect)
    Choice_2 = models.StringField(choices=[['1', 'Strategy A'], ['2', 'Strategy B'], ['3', 'Strategy C']], label='Choose the AI strategy', widget=widgets.RadioSelect)
    Choice_3 = models.StringField(choices=[['1', 'AI Strategy'], ['2', 'Believe yourself']], label='Choose the session 3 decision', widget=widgets.RadioSelect)
    time_choice1 = models.FloatField()
    time_choice2 = models.FloatField()
    time_choice3 = models.FloatField()
    time_choice4 = models.FloatField()
    time_choice5 = models.FloatField()
    time_choice6 = models.FloatField()
    time_choice7 = models.FloatField()
    time_choice8 = models.FloatField()
    time_choice9 = models.FloatField()
    time_choice10 = models.FloatField()
    Choice1 = models.FloatField(label='Enter the amount of ETH you want to buy/sell (- for sell): ')
    Choice2 = models.FloatField(label='Enter the amount of ETH you want to buy/sell (- for sell): ')
    Choice3 = models.FloatField(label='Enter the amount of ETH you want to buy/sell (- for sell): ')
    Choice4 = models.FloatField(label='Enter the amount of ETH you want to buy/sell (- for sell):')
    Choice5 = models.FloatField(label='Enter the amount of ETH you want to buy/sell (- for sell):')
    Choice6 = models.FloatField(label='Enter the amount of ETH you want to buy/sell (- for sell):')
    Choice7 = models.FloatField(label='Enter the amount of ETH you want to buy/sell (- for sell):')
    Choice8 = models.FloatField(label='Enter the amount of ETH you want to buy/sell (- for sell):')
    Choice9 = models.FloatField(label='Enter the amount of ETH you want to buy/sell (- for sell):')
    Choice10 = models.FloatField(label='Enter the amount of ETH you want to buy/sell (- for sell):')
    time1 = models.FloatField()
    time2 = models.FloatField()
    time3 = models.FloatField()
    time4 = models.FloatField()
    time5 = models.FloatField()
    my_field5 = models.FloatField()
    my_field6 = models.FloatField()
    my_field7 = models.FloatField()
    my_field8 = models.FloatField()
    my_field9 = models.FloatField()
class Consent(Page):
    form_model = 'player'
class PleaseRead(Page):
    form_model = 'player'
    form_fields = ['Name', 'Sig', 'Email', 'Date']
class Psycho(Page):
    form_model = 'player'
    form_fields = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty']
class Session2_Opening(Page):
    form_model = 'player'
    form_fields = ['Choice_2']
    @staticmethod
    def is_displayed(player):
        group = player.group
        return int(player.id_in_group) == 1
class Day1(Page):
    form_model = 'player'
    form_fields = ['Choice1']
    @staticmethod
    def vars_for_template(player):
        import time
        
        current_price =  Constants.pricesDay1_10[0]
        player.value_total_asset = player.US + player.ETH * float(current_price)
        player.Asset_day1 = player.value_total_asset
        player.time1 = float(time.time())
        
        return dict(current_price = current_price,
                    value_total_asset = player.value_total_asset,
                    US = player.US,
                    ETH = player.ETH,)
class Day2(Page):
    form_model = 'player'
    form_fields = ['Choice2']
    @staticmethod
    def vars_for_template(player):
        import time
        
        formal_price = float(Constants.pricesDay1_10[0])
        player.US = player.US - player.Choice1 * formal_price
        player.ETH = player.ETH + player.Choice1
        player.time2 = float(time.time())
        player.time_choice1 = player.time2 - player.time1
        
        current_price =  Constants.pricesDay1_10[1]
        player.value_total_asset = player.US + player.ETH * float(current_price)
        
        return dict(
                    current_price = current_price,
                    value_total_asset = player.value_total_asset,
                    US = player.US,
                    ETH = player.ETH,
                   )
class Day3(Page):
    form_model = 'player'
    form_fields = ['Choice3']
    @staticmethod
    def vars_for_template(player):
        import time
        
        formal_price = float(Constants.pricesDay1_10[1])
        player.US = player.US - player.Choice2 * formal_price
        player.ETH = player.ETH + player.Choice2
        player.time3 = float(time.time())
        player.time_choice2 = player.time3 - player.time2
        
        current_price =  Constants.pricesDay1_10[2]
        player.value_total_asset = player.US + player.ETH * float(current_price)
        
        return dict(
                    current_price = current_price,
                    value_total_asset = player.value_total_asset,
                    US = player.US,
                    ETH = player.ETH,
                   ) 
class Day4(Page):
    form_model = 'player'
    form_fields = ['Choice4']
    @staticmethod
    def vars_for_template(player):
        import time
        
        formal_price = float(Constants.pricesDay1_10[2])
        player.US = player.US - player.Choice3 * formal_price
        player.ETH = player.ETH + player.Choice3
        player.time4 = float(time.time())
        player.time_choice3 = player.time4 - player.time3
        
        current_price =  Constants.pricesDay1_10[3]
        player.value_total_asset = player.US + player.ETH * float(current_price)
        
        return dict(
                    current_price = current_price,
                    value_total_asset = player.value_total_asset,
                    US = player.US,
                    ETH = player.ETH,
                   )
page_sequence = [Consent, PleaseRead, Psycho, Session2_Opening, Day1, Day2, Day3, Day4]