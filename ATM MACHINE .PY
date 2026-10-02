import tkinter as tk
from tkinter import messagebox
from datetime import datetime


# ==========================================
# ACCOUNT CLASS
# ==========================================

class Account:

    def __init__(self, balance, account_no):
        self.balance = balance
        self.account_no = account_no
        self.transactions = []

    def credit(self, amount):

        if amount <= 0:
            return "Invalid amount"

        self.balance += amount

        self.transactions.append(
            ("CREDIT", amount, self.balance)
        )

        return f"₹{amount:.2f} credited successfully"

    def debit(self, amount):

        if amount <= 0:
            return "Invalid amount"

        if amount > self.balance:
            return "Insufficient balance"

        self.balance -= amount

        self.transactions.append(
            ("DEBIT", amount, self.balance)
        )

        return f"₹{amount:.2f} debited successfully"


# ==========================================
# GLOBAL ACCOUNT
# ==========================================

account = None


# ==========================================
# MAIN LOGIN WINDOW
# ==========================================

root = tk.Tk()

root.title("MyBank - Welcome")
root.geometry("500x550")
root.configure(bg="#eef2ff")
root.resizable(False, False)


# ==========================================
# HEADER
# ==========================================

header = tk.Frame(
    root,
    bg="#172554",
    height=130
)

header.pack(fill="x")

tk.Label(
    header,
    text="MYBANK",
    font=("Arial", 30, "bold"),
    bg="#172554",
    fg="white"
).pack(pady=(25, 5))

tk.Label(
    header,
    text="Secure Banking System",
    font=("Arial", 11),
    bg="#172554",
    fg="#cbd5e1"
).pack()


# ==========================================
# ACCOUNT CARD
# ==========================================

card = tk.Frame(
    root,
    bg="white",
    padx=35,
    pady=30
)

card.pack(
    padx=40,
    pady=40,
    fill="both"
)


tk.Label(
    card,
    text="Welcome",
    font=("Arial", 24, "bold"),
    bg="white",
    fg="#172554"
).pack()

tk.Label(
    card,
    text="Enter your account details",
    font=("Arial", 10),
    bg="white",
    fg="#64748b"
).pack(pady=(5, 25))


# Account Number

tk.Label(
    card,
    text="Account Number",
    font=("Arial", 10, "bold"),
    bg="white"
).pack(anchor="w")

account_entry = tk.Entry(
    card,
    font=("Arial", 13),
    bd=1,
    relief="solid"
)

account_entry.pack(
    fill="x",
    pady=(5, 15),
    ipady=7
)


# Opening Balance

tk.Label(
    card,
    text="Opening Balance",
    font=("Arial", 10, "bold"),
    bg="white"
).pack(anchor="w")

balance_entry = tk.Entry(
    card,
    font=("Arial", 13),
    bd=1,
    relief="solid"
)

balance_entry.pack(
    fill="x",
    pady=(5, 20),
    ipady=7
)


# ==========================================
# OPEN BANK BUTTON
# ==========================================

def open_bank():

    global account

    try:

        account_no = int(account_entry.get())
        balance = float(balance_entry.get())

        if balance < 0:
            messagebox.showerror(
                "Error",
                "Balance cannot be negative."
            )
            return

        account = Account(
            balance,
            account_no
        )

        # Close first window
        root.withdraw()

        # Open banking dashboard
        banking_window()

    except ValueError:

        messagebox.showerror(
            "Error",
            "Please enter valid account details."
        )


tk.Button(
    card,
    text="ENTER BANKING",
    command=open_bank,
    bg="#2563eb",
    fg="white",
    font=("Arial", 12, "bold"),
    relief="flat",
    cursor="hand2"
).pack(
    fill="x",
    ipady=10
)


# ==========================================
# BANKING DASHBOARD
# ==========================================

def banking_window():

    bank = tk.Toplevel(root)

    bank.title("MyBank - Banking Dashboard")
    bank.geometry("900x700")
    bank.configure(bg="#f1f5f9")
    bank.resizable(False, False)


    # ======================================
    # TOP HEADER
    # ======================================

    header = tk.Frame(
        bank,
        bg="#172554",
        height=80
    )

    header.pack(
        fill="x"
    )

    tk.Label(
        header,
        text="MYBANK",
        font=("Arial", 25, "bold"),
        bg="#172554",
        fg="white"
    ).pack(
        side="left",
        padx=30,
        pady=20
    )

    tk.Label(
        header,
        text=f"Account: {account.account_no}",
        font=("Arial", 11),
        bg="#172554",
        fg="#cbd5e1"
    ).pack(
        side="right",
        padx=30
    )


    # ======================================
    # BALANCE CARD
    # ======================================

    balance_card = tk.Frame(
        bank,
        bg="#2563eb",
        height=150
    )

    balance_card.pack(
        padx=35,
        pady=25,
        fill="x"
    )

    tk.Label(
        balance_card,
        text="TOTAL BALANCE",
        font=("Arial", 12, "bold"),
        bg="#2563eb",
        fg="#dbeafe"
    ).pack(
        pady=(25, 5)
    )

    balance_label = tk.Label(
        balance_card,
        text=f"₹ {account.balance:,.2f}",
        font=("Arial", 32, "bold"),
        bg="#2563eb",
        fg="white"
    )

    balance_label.pack()


    # ======================================
    # TRANSACTION FRAME
    # ======================================

    transaction = tk.Frame(
        bank,
        bg="white",
        padx=25,
        pady=20
    )

    transaction.pack(
        padx=35,
        fill="x"
    )


    tk.Label(
        transaction,
        text="Make a Transaction",
        font=("Arial", 18, "bold"),
        bg="white",
        fg="#172554"
    ).pack(
        anchor="w",
        pady=(0, 15)
    )


    # Amount

    amount_entry = tk.Entry(
        transaction,
        font=("Arial", 13),
        bd=1,
        relief="solid"
    )

    amount_entry.pack(
        side="left",
        fill="x",
        expand=True,
        ipady=8
    )


    # ======================================
    # UPDATE BALANCE
    # ======================================

    def update_balance():

        balance_label.config(
            text=f"₹ {account.balance:,.2f}"
        )


    # ======================================
    # CREDIT
    # ======================================

    def credit_money():

        try:

            amount = float(
                amount_entry.get()
            )

            result = account.credit(amount)

            if "successfully" in result:

                update_balance()

                add_transaction(
                    "CREDIT",
                    amount
                )

                messagebox.showinfo(
                    "Credit",
                    result
                )

                amount_entry.delete(
                    0,
                    tk.END
                )

            else:

                messagebox.showerror(
                    "Error",
                    result
                )

        except ValueError:

            messagebox.showerror(
                "Error",
                "Enter a valid amount."
            )


    # ======================================
    # DEBIT
    # ======================================

    def debit_money():

        try:

            amount = float(
                amount_entry.get()
            )

            result = account.debit(amount)

            if "successfully" in result:

                update_balance()

                add_transaction(
                    "DEBIT",
                    amount
                )

                messagebox.showinfo(
                    "Debit",
                    result
                )

                amount_entry.delete(
                    0,
                    tk.END
                )

            else:

                messagebox.showerror(
                    "Error",
                    result
                )

        except ValueError:

            messagebox.showerror(
                "Error",
                "Enter a valid amount."
            )


    # ======================================
    # CREDIT BUTTON
    # ======================================

    tk.Button(
        transaction,
        text="CREDIT",
        command=credit_money,
        bg="#16a34a",
        fg="white",
        font=("Arial", 11, "bold"),
        relief="flat",
        cursor="hand2"
    ).pack(
        side="left",
        padx=10,
        ipadx=20,
        ipady=8
    )


    # ======================================
    # DEBIT BUTTON
    # ======================================

    tk.Button(
        transaction,
        text="DEBIT",
        command=debit_money,
        bg="#dc2626",
        fg="white",
        font=("Arial", 11, "bold"),
        relief="flat",
        cursor="hand2"
    ).pack(
        side="left",
        ipadx=20,
        ipady=8
    )


    # ======================================
    # TRANSACTION HISTORY
    # ======================================

    history_frame = tk.Frame(
        bank,
        bg="white"
    )

    history_frame.pack(
        padx=35,
        pady=25,
        fill="both",
        expand=True
    )


    tk.Label(
        history_frame,
        text="Transaction History",
        font=("Arial", 18, "bold"),
        bg="white",
        fg="#172554"
    ).pack(
        anchor="w",
        padx=20,
        pady=15
    )


    # Listbox

    history_list = tk.Listbox(
        history_frame,
        font=("Arial", 11),
        bd=0,
        bg="#f8fafc"
    )

    history_list.pack(
        padx=20,
        pady=(0, 20),
        fill="both",
        expand=True
    )


    # ======================================
    # ADD TRANSACTION
    # ======================================

    def add_transaction(transaction_type, amount):

        now = datetime.now().strftime(
            "%d-%m-%Y %H:%M:%S"
        )

        if transaction_type == "CREDIT":

            text = (
                f"  🟢 CREDIT   "
                f"+₹{amount:,.2f}   "
                f"Balance: ₹{account.balance:,.2f}   "
                f"{now}"
            )

        else:

            text = (
                f"  🔴 DEBIT    "
                f"-₹{amount:,.2f}   "
                f"Balance: ₹{account.balance:,.2f}   "
                f"{now}"
            )

        history_list.insert(
            tk.END,
            text
        )


    # ======================================
    # CLOSE BANK
    # ======================================

    def close_bank():

        bank.destroy()
        root.deiconify()


    bank.protocol(
        "WM_DELETE_WINDOW",
        close_bank
    )


# ==========================================
# START APPLICATION
# ==========================================

root.mainloop()
