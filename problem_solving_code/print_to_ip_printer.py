from escpos.printer import Network

def print_receipt():
    try:
        printer = Network("10.168.122.179", 9100)  # Replace with your printer's IP

        # Print image at the top (Use a BMP file instead of ICO)
        # printer.image(r"D:\Tfl_data_hub\logo_kfc.bmp")  # Replace with your BMP image path

        # Set alignment to center
        printer.set(align='center',  bold= True)

        # Print text in the center
        printer.text("KFC\n")
        printer.text("Dine In\n")
        printer.text("Invoice No. 4456\n")
        printer.text("Thank you!\n")

        # Add extra space before cutting
        printer.text("\n" * 3)  # Add 5 blank lines before cutting

        # Cut the paper
        printer.cut()

        print("Printed successfully.")
    except Exception as e:
        print(f"Printing failed: {e}")

print_receipt()
