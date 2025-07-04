from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# 📸 Photographer Data (to be moved to DynamoDB later)
photographers = [
    {"id": "p1", "name": "Arjun Shots", "skills": ["Wildlife", "Portrait"], "image": "arjun.jpg", "rating": 4.6, "price": "₹3200"},
    {"id": "p2", "name": "Sneha Clicks", "skills": ["Fashion", "Wedding"], "image": "sneha.jpg", "rating": 4.9, "price": "₹4600"},
    {"id": "p3", "name": "Sam Vision", "skills": ["Product", "Event"], "image": "sam.jpg", "rating": 4.2, "price": "₹2700"},
    {"id": "p4", "name": "Priya Lens", "skills": ["Candid", "Newborn"], "image": "priya.jpg", "rating": 4.5, "price": "₹3100"},
    {"id": "p5", "name": "Nikhil Studio", "skills": ["Wedding", "Travel"], "image": "nikhil.jpg", "rating": 4.7, "price": "₹3900"},
    {"id": "p6", "name": "Tanya Frames", "skills": ["Food", "Fashion"], "image": "tanya.jpg", "rating": 4.3, "price": "₹3000"},
    {"id": "p7", "name": "Rohit Captures", "skills": ["Documentary", "Portrait"], "image": "rohith.jpg", "rating": 4.4, "price": "₹3300"},
    {"id": "p8", "name": "Ananya Snaps", "skills": ["Maternity", "Candid"], "image": "ananya.jpg", "rating": 4.8, "price": "₹4200"}
]


availability_data = {
    "p1": ["2025-07-02", "2025-07-05"],
    "p2": ["2025-07-03", "2025-07-06"],
    "p3": ["2025-07-07"],
    "p4": ["2025-07-04"],
    "p5": ["2025-07-08"],
    "p6": ["2025-07-06", "2025-07-09"],
    "p7": ["2025-07-02"],
    "p8": ["2025-07-03", "2025-07-10"]
}

# 🔄 Temporary bookings data (to replace with DynamoDB later)
bookings = []

# ---------- Routes ----------
@app.route('/')
def index():
    return redirect(url_for('home'))

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/book', methods=['GET', 'POST'])
def book():
    if request.method == 'POST':
        photographer_id = request.form.get('photographer_id')
        user_id = request.form.get('user_id')
        date = request.form.get('date')
        price = request.form.get('price')
        address = request.form.get('address')

        # 👇 This will be stored in DynamoDB later
        bookings.append({
            "user_id": user_id,
            "photographer_id": photographer_id,
            "date": date,
            "price": price,
            "address": address
        })

        flash("Booking successful!", "success")
        return redirect(url_for('orders'))

    return render_template('book.html', photographers=photographers)

@app.route('/orders')
def orders():
    return render_template('order.html', bookings=bookings)

@app.route('/show-photographers')
def show_photographers():
    return render_template('photographers.html', photographers=photographers, availability_data=availability_data)

# ---- Service Pages ----
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

# ---- Static Pages ----
@app.route('/about')
def about():
    return render_template('aboutus.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def register():
    return render_template('register.html')

# ---------- Run ----------
if __name__ == '__main__':
    app.run(debug=True)
