#! python3
import sys
import pyperclip

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}

if len(sys.argv) < 2:
    print("usage: py pw.py [account] - copy account password")
    sys.exit()

account = sys.argv[1]  # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print("copied")
else:
    print("{} not in lib".format(account))
