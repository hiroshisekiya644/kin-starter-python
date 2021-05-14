from agora.client import Client, Environment
from agora.keys import PrivateKey, PublicKey
from agora.utils import kin_to_quarks
from agora.model import Payment, TransactionType
from typing import List, Optional
from agora.error import AccountExistsError


class Kin:

    @staticmethod
    def generate_key():
        return PrivateKey.random()

    def __init__(self, env: Environment, app_index: Optional[int] = 0):
        self.client = Client(env, app_index, kin_version=4)

    def create_account(self, private_key: PrivateKey) -> List[PublicKey]:
        try:
            # Create Account
            self.client.create_account(private_key)
        except AccountExistsError:
            print(f'account {private_key.public_key.stellar_address} already exists')

        # Resolve Token Account
        return self.client.resolve_token_accounts(private_key.public_key)

    def get_balance(self, account: PublicKey):
        return self.client.get_balance(account)

    def request_airdrop(self, public_key: PublicKey, amount: str):
        return self.client.request_airdrop(public_key, kin_to_quarks(amount))

    def submit_payment(
            self, sender: PrivateKey, destination: PublicKey, amount: str,
            tx_type: TransactionType, memo: Optional[str]
    ):
        payment = Payment(sender, destination, tx_type, kin_to_quarks(amount), memo)
        return self.client.submit_payment(payment)

    def submit_earn(
            self, sender: PrivateKey, destination: PublicKey,
            amount: str, memo: Optional[str]
    ):
        return self.submit_payment(sender, destination, amount, TransactionType.EARN, memo)

    def submit_spend(
            self, sender: PrivateKey, destination: PublicKey,
            amount: str, memo: Optional[str]
    ):
        return self.submit_payment(sender, destination, amount, TransactionType.SPEND, memo)

    def submit_p2p(
            self, sender: PrivateKey, destination: PublicKey,
            amount: str, memo: Optional[str]
    ):
        return self.submit_payment(sender, destination, amount, TransactionType.P2P, memo)
