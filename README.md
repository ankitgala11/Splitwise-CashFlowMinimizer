# Splitwise-CashFlowMinimizer
Minimize Cash Flow among a given set of friends who have borrowed money from each other.

In this code:

-The Person class remains the same, representing individuals participating in transactions.
-The TransactionManager class maintains a debts matrix to keep track of the debts between people.
-The add_transaction method adds the given transaction amount to the corresponding positions in the debts matrix.
-The simplify method calculates the net debts for each person and then iteratively settles transactions until all debts are minimized.
-The find_creditor_debtor function finds the creditor (the person owed money) and the debtor (the person owing money) based on their net debts.
-The settle_transactions function iteratively settles transactions between the creditor and debtor until their debts are minimized.
-At the end, the simplified transactions are printed, indicating who needs to pay whom and how much.

Visualization :

![image](https://github.com/ankitgala11/Splitwise-CashFlowMinimizer/assets/58542521/bd380e67-2997-47ab-8cf5-051411e4ea70)


Output Screenshot:

![image](https://github.com/ankitgala11/Splitwise-CashFlowMinimizer/assets/58542521/7f4d705d-1ab2-438d-9f48-6abee5af48c2)

