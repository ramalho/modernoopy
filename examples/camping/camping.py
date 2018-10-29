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

    def report(self):
        """report displays names and amounts due or owed"""
        average = self.total() / len(self._contributions)
        msg = f"Total: ${self.total():5.2f}; per person: ${average:5.2f}"
        print(msg.center(40).rstrip())
        print("-"* 40)
        for name in self.people():
            paid = self._contributions[name] 
            op = "gets" if paid >= average else "owes"
            diff = abs(paid - average)
            print(f"{name:>10} paid ${paid:5.2f}, {op} ${diff:5.2f}")
