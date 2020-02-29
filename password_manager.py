import pyperclip
PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}

account = input("Password for? ")
if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print("Your Password for {} has been copied to clipboard.".format(account))
else:
    print("No account with the name {} found!".format(account))
