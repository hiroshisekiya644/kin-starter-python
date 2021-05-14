from agora.client import Environment
from agora.utils import quarks_to_kin
from kin import Kin
import time


if __name__ == '__main__':

    # Set up Kin client
    kin = Kin(Environment.TEST)

    # Prepare tokens for Alice and Bob
    private_key_alice = Kin.generate_key()
    token_accounts_alice = kin.create_account(private_key_alice)

    print(f'🔑 Public Key Alice    {private_key_alice.public_key.to_base58()}')
    for token_account in token_accounts_alice:
        print(f'🗝  Token Account Alice {token_account.to_base58()}')

    private_key_bob = Kin.generate_key()
    token_accounts_bob = kin.create_account(private_key_bob)

    print(f'🔑 Public Key Bob    {private_key_bob.public_key.to_base58()}')
    for token_account in token_accounts_bob:
        print(f'🗝  Token Account Bob {token_account.to_base58()}')

    # Helper method to sleep a bit, then print balance of Alice and Bob
    def sleep_and_print_balances():
        print('😴 Sleeping for a bit...')
        time.sleep(15)
        balance = kin.get_balance(private_key_alice.public_key)
        print(f'👛 Balance for Alice:  {quarks_to_kin(balance)} Kin')
        balance = kin.get_balance(private_key_bob.public_key)
        print(f'👛 Balance for Bob:  {quarks_to_kin(balance)} Kin')

    sleep_and_print_balances()

    print('🙏 Request Airdrop for Alice')
    kin.request_airdrop(token_accounts_alice[0], '10')

    print('🙏 Request Airdrop for Bob')
    kin.request_airdrop(token_accounts_bob[0], '10')

    sleep_and_print_balances()

    print('💸 Submit P2P Payment from Alice to Bob')
    kin.submit_p2p(private_key_alice, private_key_bob.public_key, '2', 'My demo payment')

    sleep_and_print_balances()

    print('✅ Done!')
