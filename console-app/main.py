import requests
import questionary
from questionary import Choice
from utils import print_transactions

SERVER_URL = "http://localhost:8000"

while True:
    choice = questionary.select(
        "What do you want to do?",
        choices=[
            "Add Transactions",
            "Manage Wallets",
            "Exit"
        ]
    ).ask()

    if choice == "Exit":
        break
    elif choice == "Add Transactions":
        transactions = []
        wallet_id = questionary.text("Choose the wallet to add transactions(enter wallet id):").ask()
        while True:
            print("Transaction details:")
            trans = {
                "type": questionary.select("Transaction Type:", choices=[Choice("INCOME","income"), Choice("EXPENSE","expense"), Choice("ADJUSTMENT","adjustment")]).ask(),
                "name": questionary.text("Transaction Name:").ask(),
                "amount": float(questionary.text("Transaction Amount:").ask()),
                "category": questionary.text("Transaction Category (optional):").ask() or None,
            }
            transactions.append(trans)
            
            confirm_more_cancel = questionary.select(
                "Any more transactions to add?",
                choices=[Choice("Confirm current transactions","Confirm"), Choice("Add more transactions","Add"), Choice("Cancel", "Cancel")]
            ).ask()

            match confirm_more_cancel:
                case("Confirm"):
                    if len(transactions) == 1:
                        transactions[0]["wallet_id"] = wallet_id
                        response = requests.post(f"{SERVER_URL}/transactions", json=transactions[0])
                    else:
                        payload = {
                            "transactions": transactions,
                            "wallet_id": wallet_id
                        }
                        response = requests.post(f"{SERVER_URL}/transactions/bulk", json=payload)
                    print(response.json())
                    break
                case("Add"):
                    continue
                case("Cancel"):
                    break
    elif choice == "Manage Wallets":
        response = requests.get(f"{SERVER_URL}/wallets/")
        wallets = response.json()["wallets"]
        manage_wallets = questionary.select(
            "Manage Wallets:",
            choices = [Choice(f'({str(wallet["id"])}) {wallet["name"]}', value=wallet["id"]) for wallet in wallets] + [Choice("Add new wallet", value="new"), Choice("\u21a9 Go Back", value="back")]
        ).ask()
        if manage_wallets == "back": continue
        if manage_wallets == "new":
            print("Wallet Details:")
            payload = {
                "name": questionary.text("Wallet Name:").ask(),
                "amount": float(questionary.text("Wallet Amount").ask())
            }
            response = requests.post(f"{SERVER_URL}/wallets/", json=payload)
            print(response.json())
        else:
            response = requests.get(f"{SERVER_URL}/wallets/{manage_wallets}")
            wallet = response.json()["wallet"]
            print(f'\033[1m[[ {wallet["name"]} ]]\nAmount: {wallet["amount"]}\nLast Activity: {wallet["updated_when"]}\033[0m')
            wallet_do = questionary.select(
                "Options:",
                choices = [
                    Choice("See Transactions", "see transactions"),
            ]).ask()
            if wallet_do == "see transactions":
                response = requests.get(f"{SERVER_URL}/transactions/wallet/{wallet['id']}")
                print_transactions(response.json()["transactions"])