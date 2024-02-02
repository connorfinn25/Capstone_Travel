from flask import Flask, redirect, request, send_from_directory

app = Flask(__name__, static_folder='public')

@app.route('/book-flight', methods=['POST'])
def book_flight():
    print("Flight Booking Details:", request.form)
    # Here, you would add code to save data to a database
    return redirect('/')

@app.route('/book-hotel', methods=['POST'])
def book_hotel():
    print("Hotel Booking Details:", request.form)
    # Database code would go here
    return redirect('/')

@app.route('/')
def index():
    return send_from_directory('public', 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
