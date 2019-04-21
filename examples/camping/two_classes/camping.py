import operator

class Camper:

    max_name_len = 0

    def __init__(self, name, paid=0.0):
        self.name = name
        self.paid = paid
        if len(name) > Camper.max_name_len:
            Camper.max_name_len = len(name)

    def pay(self, amount):
        self.paid += amount

    def display(self, individual_share):
        camper_tpl = '{name:>{width}} paid ${paid:7.2f}, balance: $ {balance:7.2f}'
        print(camper_tpl.format(
            name = self.name,
            width = self.max_name_len,
            paid = self.paid,
            balance = self.paid - individual_share,
        ))

class Budget:
    """
    Class ``camping.Budget`` represents the budget for a camping trip.
    """

    def __init__(self, *names):
        self._campers = {name: Camper(name) for name in names}

    def total(self):
        return sum(c.paid for c in self._campers.values())

    def people(self):
        return sorted(self._campers)

    def contribute(self, name, amount):
        if name not in self._campers:
            raise LookupError("Name not in budget")
        self._campers[name].pay(amount)

    def individual_share(self):
        return self.total() / len(self._campers)

    def summaries(self):
        share = self.individual_share()
        return [camper.summary() for camper in self._campers.values()]

    def report(self):
        """report displays names and amounts due or owed"""
        share = self.individual_share()
        heading_tpl = "Total: ${:6.2f}; individual share: ${:6.2f}"
        print(heading_tpl.format(self.total(), share))
        print("-"* 42)
        sorted_campers = sorted(self._campers.values(), key=operator.attrgetter('paid'))
        for camper in sorted_campers:
            camper.display(share)
