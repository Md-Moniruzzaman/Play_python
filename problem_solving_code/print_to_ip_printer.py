from escpos.printer import Network

def print_receipt():
    try:
        printer = Network("192.168.1.100", 9100)  # Replace with your printer's IP
        printer.text("Hello, Printer!\n")
        printer.text("This is a test print.\n")
        printer.cut()
        print("Printed successfully.")
    except Exception as e:
        print(f"Printing failed: {e}")

print_receipt()
