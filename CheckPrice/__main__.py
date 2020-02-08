from CheckPrice import CheckPrice


def main():
    print("Hello World")

    myCheckPrice = CheckPrice()
    myCheckPrice.submitTravelForm()
    myCheckPrice.fillTravelersForm()
    myCheckPrice.terminate()

if __name__ == "__main__":
    main()
