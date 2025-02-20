from escpos.printer import Network

def print_receipt(order_number):
    try:
        printer = Network("10.168.122.179", 9100)  # Replace with your printer's IP

        # Print KFC Logo (Ensure BMP format)
        # printer.image(bmp_path)

        # Set text alignment to center
        printer.set(align='center', double_height=True,double_width=True)
        printer.textln("KFC")

        # Print Order Details
        printer.text("\n")  # Space after logo
        printer.set(align='center',  bold=True, double_height=True)
        printer.text(f"Order Number: ")
        printer.set(align='center', double_height=True,  double_width=True)
        printer.text(f"{order_number}\n")

        # Reset text size
        printer.set(normal_textsize=True)
        printer.text("Thank You !\n")
        printer.text("Please check your order status on display screen.\n")

        # Add a footer
        printer.text("\nPowered by: Transcom Technology\n")

        # Add extra space before cutting
        printer.text("\n" * 2)

        # Cut the paper
        printer.cut()

        print("Printed successfully.")
    except Exception as e:
        print(f"Printing failed: {e}")

# Example usage
print_receipt(1932)
