from CheckPrice import CheckPrice

def main():
    print("Starting Allegiant Air Automation\n")

    myCheckPrice = CheckPrice()
    myCheckPrice.submitTravelForm()
    myCheckPrice.fillTravelersForm()
    myCheckPrice.checkData()
    myCheckPrice.terminate()

if __name__ == "__main__":
    main()
