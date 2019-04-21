"""
Class ``camping.Budget`` represents the budget for a camping trip.
"""

class Budget:

    def __init__(self, *names):
        self._contributions = {name:0.0 for name in names}

    def total(self):
        return sum(self._contributions.values())

    def people(self):
        return sorted(self._contributions)

    def contribute(self, name, amount):
        if name not in self._contributions:
            raise LookupError("Person not in budget")
        self._contributions[name] += amount

    def individual_share(self):
        return self.total() / len(self._contributions)

    def balances(self):
        share = self.individual_share()
        result = []
        for name in self.people():
            paid = self._contributions[name]
            result.append((paid - share, name, paid))
        return result

    def report(self):
        """report displays names and amounts due or owed"""
        template = "Total: ${:6.2f}; per person: ${:6.2f}"
        heading = template.format(self.total(), self.individual_share()) 
        print(heading.center(42).rstrip())
        print("-"* 42)
        for balance, name, paid in sorted(self.balances()):
            print(f"{name:>10} paid ${paid:6.2f}, balance: $ {balance:6.2f}")
