"""
Description: An app that get as input the amount of a bill for a particular period and the days
that each of the flatmates stayed in the house for that period and returns how much each
flatmates has to pay.  It also generates a PDF report
stating the name of flatmates, the period, and how much each of them had to pay.

IS_A
HAS_A

NOUNS:
App, Bill, Period, Flatmate,

ADJ:
number of days in period
length_of_stay
name

VERB:
output_pdf
get_amount_to_pay

"""


class Bill:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount


class FlatMate:
    def __init__(self, name, days):
        self.name = name
        self.days = days


class PaymentCalculator:
    def __init__(self, days_in_period, flatmate_list, bill_list):
        self.days_in_period = days_in_period
        self.flatmate_list = flatmate_list
        self.bill_list = bill_list

    def get_total_days_for_all(self):
        total = 0
        for f in self.flatmate_list:
            total += f.days
        return total

    def get_percent_for_flatmate(self, flatmate):
        return flatmate.days / self.get_total_days_for_all()

    def get_amounts_per_bill_for_flatmate(self, flatmate):
        output = {}
        for b in self.bill_list:
            output[b.name] = self.get_percent_for_flatmate(flatmate) * b.amount
        return output

    def text_report(self):
        text = f"REPORT for {self.days_in_period}\n"
        for f in self.flatmate_list:
            bills_dict = self.get_amounts_per_bill_for_flatmate(f)
            text += f"\t{f.name}\n"
            for name in bills_dict:
                amount = bills_dict[name]
                text += f"\t\t{name}: {amount}\n"
        return text


c = PaymentCalculator(
    30,
    [
        FlatMate("Bob", 30),
        FlatMate("Carol", 10),
    ],
    [
        Bill("Power", 100),
        Bill("Water", 100),
        Bill("Cable", 100)
    ]
)

print(c.text_report())
