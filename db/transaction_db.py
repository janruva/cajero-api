from datetime import datetime
from pydantic import BaseModel

class TransactionInDB(BaseModel):
    id_transaction: int = 0
    username: str
    date: datetime = datetime.now()
    value: int
    actual_balance: int

database_transactions = []
generator = {"id":0}

def save_transaction(transaction_in_db: TransactionInDB):
    generator["id"] = generator["id"] + 1
    transaction_in_db.id_transaction = generator["id"]
    database_transactions.append(transaction_in_db)
    return transaction_in_db

#lista de transacciones de un usuario
def get_transactions(username: str):
    transactions = []
    for t in database_transactions: #itera de la bd de transacciones
        if t.username == username: #Si el usuario es igual al dado
            transactions.append(t) #añade a la lista las transacciones de un usuario
    return transactions #retorna la lista