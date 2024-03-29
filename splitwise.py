class Person:
    def __init__(self, name, idx):
        self.name = name.lower()
        self.idx = idx

class TransactionManager:
    def __init__(self, total_people):
        self.total_people = total_people
        self.people = []
        self.transactions = [[0] * total_people for _ in range(total_people)]

    def add_person(self, name):
        person = Person(name, len(self.people))
        self.people.append(person)

    def _get_person_index(self, name):
        name_lower = name.lower()
        for person in self.people:
            if person.name == name_lower:
                return person.idx
        return -1

    def add_transaction(self, person1_name, person2_name, amount):
        person1_idx = self._get_person_index(person1_name)
        person2_idx = self._get_person_index(person2_name)

        if person1_idx == -1 or person2_idx == -1:
            print(f"Error: Person is not in the list of people.")
            return

        self.transactions[person1_idx][person2_idx] = amount

    def simplify(self):
        def find_max_creditor(temp):
            max_creditor = max(range(self.total_people), key=lambda x: temp[x])
            return max_creditor

        def find_max_debtor(temp):
            max_debtor = min(range(self.total_people), key=lambda x: temp[x])
            return max_debtor

        def settle_transactions(temp):
            max_creditor = find_max_creditor(temp)
            max_debtor = find_max_debtor(temp)

            if temp[max_creditor] == 0 and temp[max_debtor] == 0:
                return

            amount = min(abs(temp[max_debtor]), temp[max_creditor])
            temp[max_creditor] -= amount
            temp[max_debtor] += amount

            print(f"{self.people[max_debtor].name.capitalize()} has to pay Rs {amount} to {self.people[max_creditor].name.capitalize()}")

            settle_transactions(temp)

        temp = [0] * self.total_people

        for i in range(self.total_people):
            for j in range(self.total_people):
                temp[i] += self.transactions[j][i] - self.transactions[i][j]

        settle_transactions(temp)


if __name__ == "__main__":
    print("################################## CASH FLOW MINIMIZER ##################################")
    total_people = int(input("Enter the number of people: "))
    transaction_manager = TransactionManager(total_people)

    print(f"Please enter the name of {total_people} people")
    for _ in range(total_people):
        name = input().strip()
        transaction_manager.add_person(name)

    print("\nPlease enter the transactions in the format: Person1 Person2 Payment")
    print("Enter 0 to exit")

    while True:
        transaction_input = input().strip().split()
        if transaction_input[0] == '0':
            break
        person1_name, person2_name, amount = transaction_input
        transaction_manager.add_transaction(person1_name, person2_name, int(amount))

    print("\nSimplified Transactions:")
    transaction_manager.simplify()
