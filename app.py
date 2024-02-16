from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Define the website flow
website_flow = {
    'home': '/',
    'page_a': '/page_a',
    'page_b': '/page_b',
    'page_c': '/page_c',
    'page_e': '/page_e',
    'page_f': '/page_f'
}

# Route for Page A
@app.route('/page_a')
def page_a():
    update_breadcrumbs('page_a')
    return render_template('page_a.html', breadcrumbs=session.get('breadcrumbs', []), website_flow=website_flow)

# Route for Page B
@app.route('/page_b')
def page_b():
    update_breadcrumbs('page_b')
    return render_template('page_b.html', breadcrumbs=session.get('breadcrumbs', []), website_flow=website_flow)

# Route for Page C
@app.route('/page_c')
def page_c():
    update_breadcrumbs('page_c')
    return render_template('page_c.html', breadcrumbs=session.get('breadcrumbs', []), website_flow=website_flow)

# Route for Page E
@app.route('/page_e')
def page_e():
    update_breadcrumbs('page_e')
    return render_template('page_e.html', breadcrumbs=session.get('breadcrumbs', []), website_flow=website_flow)

# Route for Page F
@app.route('/page_f')
def page_f():
    update_breadcrumbs('page_f')
    return render_template('page_f.html', breadcrumbs=session.get('breadcrumbs', []), website_flow=website_flow)

# Function to update breadcrumbs in session
def update_breadcrumbs(page):
    breadcrumbs = session.get('breadcrumbs', [])
    if page in breadcrumbs:
        breadcrumbs = breadcrumbs[:breadcrumbs.index(page)+1]
    else:
        breadcrumbs.append(page)
    session['breadcrumbs'] = breadcrumbs

# def update_breadcrumbs(page):
#     breadcrumbs = session.get('breadcrumbs', [])
#     breadcrumbs.append(page)
#     session['breadcrumbs'] = breadcrumbs

# Route for handling back button
@app.route('/back')
def back():
    breadcrumbs = session.get('breadcrumbs', [])
    if len(breadcrumbs) > 1:
        breadcrumbs.pop()  # Remove current page from breadcrumbs
        session['breadcrumbs'] = breadcrumbs
        prev_page = breadcrumbs[-1]
        return redirect(url_for(prev_page))
    else:
        return redirect(url_for('index'))  # Redirect to homepage or some other default page

# Home page
@app.route('/')
def home():
    # session.pop('breadcrumbs', None)  # Clear breadcrumbs on homepage
    session['breadcrumbs'] = ['home']  # Initialize breadcrumbs with 'Home'
    return render_template('index.html', breadcrumbs=session.get('breadcrumbs', []), website_flow=website_flow)

if __name__ == '__main__':
    app.run(debug=True)
