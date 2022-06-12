
class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []
        self.balance = 0.0

    def deposit(self, amount, description=''):
        self.balance += amount
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=''):
        if(not self.check_funds(amount)):
            return False

        self.balance -= amount
        self.ledger.append({'amount': -amount, 'description': description})

        return True

    def get_balance(self):
        return self.balance

    def transfer(self, amount, recipient):
        if(self.check_funds(amount)):
            self.withdraw(amount, "Transfer to {category}".format(
                category=recipient.category))

            recipient.deposit(amount, "Transfer from {category}".format(
                category=self.category))

            return True

        return False

    def check_funds(self, amount):
        if(self.balance < amount):
            return False

        return True

    def __repr__(self):
        output = self.category.center(30, '*') + '\n'

        for item in self.ledger:
            desc = item['description'][:23]
            amount = '{amount:.2f}'.format(amount=item['amount'])[:7]
            spaces = ' ' * (30 - (len(desc) + len(amount)))

            output += '{desc}{spaces}{amount}\n'.format(
                desc=desc, spaces=spaces, amount=amount)

        output += 'Total: {balance:.2f}'.format(balance=self.balance)

        return output


def create_spend_chart(categories):
    num_categories = len(categories)
    cat_percent_spent = {}

    for cat in categories:
        withdrawals = 0

        for item in cat.ledger:
            if(item['amount'] < 0):
                withdrawals += -item['amount']

        cat_percent_spent[cat.category] = withdrawals

    total = sum(cat_percent_spent.values())
    cat_percent_spent.update((x, int(((y / total) * 100)))
                             for x, y in cat_percent_spent.items())

    chart_marks = ['100|', ' 90|', ' 80|', ' 70|', ' 60|',
                   ' 50|', ' 40|', ' 30|', ' 20|', ' 10|', '  0|']

    chart = 'Percentage spent by category\n'
    i = 100

    for mark in chart_marks:
        chart += mark

        for item in cat_percent_spent.values():
            if item >= i:
                chart += ' o '
            else:
                chart += '   '

        chart += ' \n'
        i -= 10

    chart += '    -' + '-' * (3 * num_categories) + '\n'  # Add divider

    footer = ''

    longest_cat_name = len(max(cat_percent_spent.keys(), key=len))

    for i in range(longest_cat_name):
        footer += '     '

        for cat in cat_percent_spent.keys():
            if(len(cat) > i):
                footer += cat[i] + '  '
            else:
                footer += '   '

        footer += '\n'

    chart += footer.rstrip('\n')

    return chart


food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

# # print(food)
# # print(clothing)

print(create_spend_chart([food, clothing, auto]))
