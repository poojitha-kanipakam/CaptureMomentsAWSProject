from flask import Flask, render_template, request, redirect, url_for, flash
import boto3
import uuid
from datetime import datetime

# Step 1: Create the Flask app
app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # For flash messages

# Step 2: Connect to AWS DynamoDB
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

# Step 3: Define the tables
photographers_table = dynamodb.Table('photographers')  # Table where photographer details are stored
bookings_table = dynamodb.Table('booking')  # Table where booking records will be stored

# ---------- ROUTES ----------

# Home Page
@app.route('/')
def index():
    return redirect(url_for('home'))

@app.route('/home')
def home():
    return render_template('home.html')


# Booking Page
@app.route('/book', methods=['GET', 'POST'])
def book():
    if request.method == 'POST':
        photographer_id = request.form.get('photographer_id')  # photographer_id from form
        user_id = request.form.get('user_id')  # user_id from form
        date = request.form.get('date')  # booking date from form
        price = request.form.get('price')  # price from form
        address = request.form.get('address')  # user's address from form

        # Generate a unique booking ID
        booking_id = str(uuid.uuid4())

        # Insert the booking record into the DynamoDB "booking" table
        bookings_table.put_item(Item={
            'booking_id': booking_id,
            'photographer_id': photographer_id,  # Refers to photographer_id in "photographers" table
            'user_id': user_id,
            'date': date,
            'price': price,
            'address': address,
            'timestamp': datetime.now().isoformat()
        })

        flash('Booking successful!', 'success')
        return redirect(url_for('orders'))

    # Load photographers for dropdown from DynamoDB "photographers" table
    response = photographers_table.scan()  # Scan the table to get all photographers
    photographers = response.get('Items', [])  # List of photographer items

    return render_template('book.html', photographers=photographers)


# Booking Orders Page (Displays all bookings)
@app.route('/orders')
def orders():
    # Retrieve all booking records from DynamoDB "booking" table
    response = bookings_table.scan()
    bookings = response.get('Items', [])
    return render_template('order.html', bookings=bookings)


# Photographer Gallery Page (Displays all photographers)
@app.route('/show-photographers')
def show_photographers():
    # Retrieve all photographer records from DynamoDB "photographers" table
    response = photographers_table.scan()
    photographers = response.get('Items', [])
    availability_data = {
        p['photographer_id']: p.get('availability', []) for p in photographers
    }
    return render_template('photographers.html', photographers=photographers, availability_data=availability_data)


# ---------- SERVICE PAGES ----------

@app.route('/wedding')
def wedding():
    return render_template('wedding.html')

@app.route('/fashion')
def fashion():
    return render_template('fashion.html')

@app.route('/event')
def event():
    return render_template('event.html')

@app.route('/baby')
def baby():
    return render_template('baby.html')

@app.route('/travel')
def travel():
    return render_template('travel.html')

@app.route('/product')
def product():
    return render_template('product.html')

@app.route('/food')
def food():
    return render_template('food.html')


# ---------- STATIC PAGES ----------

@app.route('/about')
def about():
    return render_template('aboutus.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def register():
    return render_template('register.html')


# ---------- RUN SERVER ----------
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
