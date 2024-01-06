from flask import Flask, render_template

app = Flask(__name__)

company_name = "Kowtow Digital"  # Replace this with your actual company name

# Define routes for each tab
@app.route('/')
def home():
    return render_template('dashboard.html', active_tab='home', company_name=company_name)

@app.route('/report')
def report():
    return render_template('dashboard.html', active_tab='report', company_name=company_name)

@app.route('/approvals')
def approvals():
    return render_template('dashboard.html', active_tab='approvals', company_name=company_name)

@app.route('/marketing')
def marketing():
    return render_template('dashboard.html', active_tab='marketing', company_name=company_name)

@app.route('/stats')
def stats():
    return render_template('dashboard.html', active_tab='stats', company_name=company_name)

@app.route('/expenditure')
def expenditure():
    return render_template('dashboard.html', active_tab='expenditure', company_name=company_name)

@app.route('/calendar')
def calendar():
    return render_template('dashboard.html', active_tab='calendar', company_name=company_name)

if __name__ == '__main__':
    app.run(debug=True)
