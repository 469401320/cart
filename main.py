import getopt
import sys
from com.solution.invoice import Invoice
from com.solution.solutionlog import logger


def main(argv):
    products = []
    try:
        opts, args = getopt.getopt(argv, "hp:", ["product="])
    except getopt.GetoptError:
        print('error input')
        print('main.py --product=<product>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('main.py --product=<product>')
            sys.exit()
        elif opt in "--product=":
            if len(arg) > 0 and arg[0] == '\'' and arg[-1] == '\'':
                products.append(arg[1:-1])
    print(products)
    invoice = Invoice(products)
    if not invoice.check():
        logger.error("error args")
    invoice.calc_total()
    invoice.invoice_print()


if __name__ == "__main__":
    main(sys.argv[1:])
