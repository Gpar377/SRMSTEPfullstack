# gdb/tests/test_interface_factory.py
from gdb.domain.account_factory import AccountFactory

def main():
    print("=== Activity 12: Factory-Driven System Suite ===")

    # Step 1: Create one of each account type through AccountFactory only
    sa = AccountFactory.create_account("SAVINGS", "SA100", "Alice", 25, 5000.0, "Active", "1234")
    ca = AccountFactory.create_account("CURRENT", "CA200", "Bob", 35, 10000.0, "Active", "5678")
    sal = AccountFactory.create_account("SALARY", "SAL300", "Charlie", 28, 0.0, "Active", "9999")
    fd = AccountFactory.create_account("FIXEDDEPOSIT", "FD400", "Diana", 45, 50000.0, "Active", "0000")

    # Step 2: Assert via IAccount members only (no concrete class references)
    assert sa.get_account_type() == "Savings"
    assert sa.balance == 5000.0
    sa.deposit(500.0)
    assert sa.balance == 5500.0
    sa.withdraw(200.0)
    assert sa.balance == 5300.0

    assert ca.get_account_type() == "Current"
    assert ca.balance == 10000.0
    ca.deposit(1000.0)
    assert ca.balance == 11000.0
    ca.withdraw(500.0)
    assert ca.balance == 10500.0

    assert sal.get_account_type() == "Salary"
    assert sal.balance == 0.0
    sal.deposit(30000.0)
    assert sal.balance == 30000.0

    assert fd.get_account_type() == "FixedDeposit"
    assert fd.balance == 50000.0
    interest = fd.calculate_interest()
    assert interest == 3250.0  # 50000 * 6.5% * (12/12)

    print("All accounts created and validated through IAccount interface only!")

if __name__ == "__main__":
    main()
