def kid_mod11(a, length=15):
    """
    Function used to find the KID from a number (MOD 11)
    """
    account = str(a)
    sum = 0

    # Find weighted the sum of the account
    for i in range(0, len(account)):
        thisWeight = (i % 6) + 2
        sum += thisWeight * int(account[len(account) - i - 1])

    mod11 = sum % 11
    ctrlNum = 11 - mod11

    if(ctrlNum == 10):
        ctrlNum = "-"
    elif(ctrlNum == 11):
        ctrlNum = "0"
    else:
        ctrlNum = str(ctrlNum)

    kid = account + ctrlNum
    return _pad(kid, size=length)


def _pad(kid, size=7):
    """Pad kid number to correct size"""
    if len(kid) < size:
        pad_by = size - len(kid)
        padding = "0" * pad_by
        kid = padding + kid
    return kid
