# You can obtain this program's source code and assets
#  by following me on GitHub https://github.com/dev-harshhh18/.

# In this program, we calculate students' marks and grades using a framework, 
# which allows for the simultaneous use of WebDev and Python, making it very convenient.

# We are utilizing the *FLASK* framework to connect WebDev and Python. For frontend development, 
# we are using HTML, CSS, and JS, and for backend development, we are using Python.

# Import necessary modules from Flask
# Create Flask application instance
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Define a class to manage student result data
class Result:

    # Method to store student roll number and name
    def info(self, roll, name):
        self.roll = roll        
        self.name = name

# Method to store marks for Physics, Mathematics, and Chemistry
    def mark(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

# Method to store marks for Cricket, Hockey, and Chess
    def smark(self, sm1, sm2, sm3):
        self.sm1 = sm1
        self.sm2 = sm2
        self.sm3 = sm3

# Method to calculate total and percentage for academic subjects
    def total(self):
        self.tot = self.m1 + self.m2 + self.m3
        self.per = self.tot * 100 / 300

# Method to calculate total and percentage for sports
    def stotal(self):
        self.stot = self.sm1 + self.sm2 + self.sm3
        self.sper = self.stot * 100 / 300

# Method to display results and assign grades based on sports marks
    def disp(self):
        grade = 'A' if self.sper >= 70 else 'B' if self.sper >= 50 else 'C' if self.sper >= 35 else 'Fail'
        return {
            'roll': self.roll,
            'name': self.name,
            'm1': self.m1,
            'm2': self.m2,
            'm3': self.m3,
            'sm1': self.sm1,
            'sm2': self.sm2,
            'sm3': self.sm3,
            'tot': self.tot,
            'per': self.per,
            'stot': self.stot,
            'sper': self.sper,
            'grade': grade
        }

# Route to render the main HTML page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission and calculate results
@app.route('/calculate', methods=['POST'])
def calculate():
    roll = request.form['rollNumber']
    name = request.form['name']
    m1 = int(request.form['pMarks'])
    m2 = int(request.form['mMarks'])
    m3 = int(request.form['cMarks'])
    sm1 = int(request.form['sm1'])
    sm2 = int(request.form['sm2'])
    sm3 = int(request.form['sm3'])

    r = Result()
    r.info(roll, name)
    r.mark(m1, m2, m3)
    r.smark(sm1, sm2, sm3)
    r.total()
    r.stotal()
    result_data = r.disp()

    return jsonify(result_data)

# Run the Flask application in debug mode
if __name__ == '__main__':
    app.run(debug=True)
