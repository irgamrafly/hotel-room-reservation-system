
# Hotel Room Reservation System

## Description
Hotel Room Reservation System is a simple Python-based program designed to simulate a hotel room reservation process. This program allows users to select a room type, add an optional breakfast package, calculate the total reservation cost, and display a payment receipt.

This project was developed as part of learning the fundamentals of Python programming, particularly conditional statements, user input, and basic arithmetic operations.

## Features
- **Guest Capacity Validation:** Limits the maximum number of guests to 4 people per reservation.
- **Room Selection:** Provides three room options: Deluxe, Superior, and Standard.
- **Breakfast Package:** Allows users to add an optional breakfast package.
- **Price Calculation:** Automatically calculates the total reservation cost.
- **Payment Receipt:** Displays a summary of the selected room, breakfast cost, and total payment.

## Room Prices

| Room Type | Price |
|---|---:|
| Deluxe | Rp 500,000 |
| Superior | Rp 300,000 |
| Standard | Rp 200,000 |

**Additional Breakfast:** Rp 50,000

## Technologies Used
- Python 3
- Visual Studio Code (VS Code)

## How to Run
1. Make sure Python 3 is installed on your computer.
2. Download or clone this repository.
3. Open the project folder in your code editor.
4. Run the Python file using the following command:

```bash
python hotel_reservation.py
```

5. Follow the instructions displayed in the terminal.

## Programming Concepts
This project demonstrates the use of:
- Variables and Data Types
- User Input (`input()`)
- Conditional Statements (`if`, `elif`, and `else`)
- Type Conversion (`int()`)
- String Methods (`lower()`)
- Basic Arithmetic Operations
- Formatted Output (`f-strings`)

## Example Output

```text
=== Sistem Reservasi Kamar Hotel ===
Masukkan jumlah tamu: 2

Pilihan Kamar: deluxe / superior
Masukkan tipe kamar: deluxe
Tambah paket sarapan? (y/t): y
Info: Paket sarapan ditambahkan.

=== Struk Reservasi ===
Tipe Kamar       : Kamar Deluxe
Harga Kamar      : Rp 500000
Biaya Sarapan    : Rp 50000
------------------------------
TOTAL BAYAR      : Rp 550000
```

## Author
**Irga Mochamad Rafly**

Informatics Student  
Faculty of Engineering  
Universitas Siliwangi

## License
This project is created for educational purposes.
