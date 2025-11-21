from fileinput import lineno
from .models import Transaction
from users.models import User
from wallet.models import Wallet
from django.db import transaction as db_transaction
from decimal import Decimal
import logging
transactions_logger = logging.getLogger("transactions_logger")

def send_money_service(sender_ac_no,reciver_ac_no,amount):
   
    print(reciver)
    try:
        sender  = User.objects.get(account_number=sender_ac_no)
        reciver = User.objects.get(account_number=reciver_ac_no)
    except User.DoesNotExist:
        transactions_logger.error(
    f"[{lineno}]FAILED Transaction — User Does Not Exist"
)
        return {"success": False, "message": "Sender or Receiver does not exist."}
    transactions_logger.error(
    f"[{lineno}]FAILED Transaction — Insufficient Balance"
    )
    
    sender_wallet = sender.wallet
    reciver_wallet = reciver.wallet
    amount = Decimal(amount)
    with db_transaction.atomic():
        if sender.wallet.balance < amount:
            transactions_logger.error(
    f"[{lineno}]FAILED Transaction — Insufficient Balance"
    )
            return {"success": False, "message": "Insufficient balance."}
        else:
            sender.wallet.balance -= amount
            reciver.wallet.balance += amount
            sender.wallet.save()
            reciver.wallet.save()
            transaction = Transaction.objects.create(
                sender=sender,
                receiver=reciver,
                sender_wallet=sender_wallet,
                receiver_wallet=reciver_wallet,
                amount=amount,
                transaction_type='sendmoney'
            )
            transactions_logger.info(f"[{lineno}] Sucessful transaction: from {sender.account_number} to {reciver.account_number} amount: {amount} transaction_id: {transaction.transaction_id}")
            return {"success": True, "message": "Transaction completed successfully.", "transaction_id": transaction.transaction_id}