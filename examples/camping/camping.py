"""
Class ``camping.Budget`` represents the budget for a camping trip.
"""

class Budget:

    def __init__(self, names):
        self._contributions = {name:0.0 for name in names.split()}

    def total(self):
        return sum(self._contributions.values())

    def people(self):
        return sorted(self._contributions)

    def contribute(self, who, amount):
        if who not in self._contributions:
            raise LookupError("Person not in budget")
        self._contributions[who] += amount

    def individual_share(self):
        return self.total() / len(self._contributions)

    def balances(self):
        share = self.individual_share()
        for name in self.people():
            paid = self._contributions[name]
            yield (name, paid, paid - share)

    def report(self):
        """report displays names and amounts due or owed"""
        template = "Total: ${:6.2f}; per person: ${:6.2f}"
        heading = template.format(self.total(), self.individual_share()) 
        print(heading.center(40).rstrip())
        print("-"* 40)
        for name, paid, balance in self.balances():
            op = "gets" if balance >= 0 else "owes"
            amount = abs(balance)
            print(f"{name:>10} paid ${paid:6.2f}, {op} ${amount:6.2f}")
