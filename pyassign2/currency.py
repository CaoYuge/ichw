import re
from urllib.request import urlopen

def getting_url(currency_from,currency_to,amount_from):
    """Get the url from the values entered"""
    url = 'http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=' + currency_from + '&to=' + currency_to + '&amt=' + '' + amount_from  # the url to be urlopened
    return url

def exchange(currency_from,currency_to,amount_from):
    """Returns: amount of currency received in the given exchange.

    In this exchange, the user is changing amount_from money in
    currency currency_from to the currency currency_to. The value
    returned represents the amount in currency currency_to.

    The value returned has type float.

    Parameter currency_from: the currency on hand
    Precondition: currency_from is a string for a valid currency code

    Parameter currency_to: the currency to convert to
    Precondition: currency_to is a string for a valid currency code

    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float"""
    url = getting_url(currency_from, currency_to, amount_from)
    doc = urlopen(url)
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    jstrletter = re.split(',|\{|\:| |\"|\}',jstr)
    jstr1 = ""
    amount_to = ""
    for i in jstrletter:
        if i != "":
            jstr1 = jstr1 + i
    for s in range(jstr1.find("to"),len(jstr1)-1):
        if 47 < ord(jstr1[s]) < 58 or jstr1[s] == ".":
            amount_to = amount_to + jstr1[s]
    return amount_to
    # Processing the strings fedback to get the amount_to

def test_getting_url():
    """Test the function of getting_url"""
    assert(getting_url('USD','EUR','2.5') == 'http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=USD&to=EUR&amt=2.5')
    assert(getting_url('CNY','USD','10000000') == 'http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=CNY&to=USD&amt=10000000')
    assert(getting_url('EUR','CNY','0.0000001') == 'http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=EUR&to=CNY&amt=0.0000001')

def test_exchange():
    """Test the function of exchange"""
    assert(exchange('USD','EUR','2.5') == '2.0952375' )
    assert(exchange('USD','CNY','2.5') == '16.315375' )

def test_all():
    """Test all the functions"""
    test_getting_url()
    test_exchange()

def main():
    test_all()
    currency_from = input("please enter the oringinal currency:")
    currency_to = input("please enter the target currency:")
    amount_from = input("please enter the amount:") # enter the basic information
    print(exchange(currency_from, currency_to, amount_from)) # print the amount_to

while __name__ == '__main__':
    main()