from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'supersecretkey_diamond_car_wash'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/book', methods=['POST'])
def book():
    name = request.form.get('name')
    phone = request.form.get('phone')
    service = request.form.get('service')
    
    # Here you can handle saving to database or sending an email/SMS
    flash(f'Thank you {name}! Your booking request for {service} has been received. We will call you shortly.', 'success')
    return redirect(url_for('home') + '#contact')

if __name__ == '__main__':
    app.run(debug=True, port=5000)