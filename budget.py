class Category:

    def __init__(self, category_name):
        self.category_name = category_name
        self.ledger = []

    def deposit(self, amount, description=''):
        self.ledger.append({'amount':amount, 'description':description})

    def withdraw(self, amount, description=''):
        if(self.check_funds(amount)):
            self.ledger.append({'amount':-amount, 'description':description})
            return True
        else:
            return False
            
    def get_balance(self):
        balance = 0.0
        for entry in self.ledger:
            balance += entry['amount']
        return balance

    def transfer(self, amount, destination):
        description_source = "Transfer to {}".format(destination.category_name)
        description_transfer = "Transfer from {}".format(self.category_name)
        if(self.withdraw(amount,description_source)):
            destination.deposit(amount, description_transfer)
            return True
        else:
            return False
        

    def check_funds(self, amount):
        balance = self.get_balance()
        if(amount>balance):
            return False
        else:
            return True

    def __str__(self):
        display = "{:*^30s}\n".format(self.category_name)
        for entry in self.ledger:
            display+="{:<23}{:>7.2f}\n".format(entry['description'][:23], entry['amount'])
        display+="Total: {:.2f}".format(self.get_balance())
        return display


def ledger_calculations(ledger):
    sum = 0.0
    for entry in ledger:
        if entry['amount']<0:
            sum+=-1*entry['amount']
    return round(sum, 2)


def percentage(spendings):
    percent = []
    for i in range(len(spendings)):
        percent.append(round((spendings[i]/sum(spendings)*100)//10)*10)
    return percent


def create_spend_chart(categories):
    spendings = [0.0]*len(categories)
    
    for i in range(len(categories)):
        spendings[i] = ledger_calculations(categories[i].ledger)
    spendings = percentage(spendings)
    graph = 'Percentage spent by category\n'
    
    for row in range(11):
        row_no = (11-1-row)*10
        graph+="{:>3}| ".format(row_no)
        for per in spendings:
            out =' '
            if per >= row_no:
                out = 'o'
            graph+="{}  ".format(out)
        graph+='\n'
    graph += ' '*4 + '-'*3*len(spendings)+'-'+'\n'
    long_len = len(max([category.category_name for category in categories ],key=len))
    format = [cat.category_name+' '*(long_len-len(cat.category_name)) for cat in categories]
    
    for row in range(long_len):
        graph+=" "*5
        for name in format:
            graph+="{}  ".format(name[row])
        graph+='\n'
    return graph[:-1]