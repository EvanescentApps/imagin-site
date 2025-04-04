from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/forum')
def forum():
    return render_template('list_forum.html')

@app.route('/inscription-projets')
def inscription_projets():
    return render_template('inscription_projets.html')

@app.route('/anciens-projets')
def anciens_projets():
    return render_template('anciens_projets.html')

@app.route('/votes')
def votes():
    return render_template('votes.html')

@app.route('/discussion/<int:id>')  # Define the route with <int:id>
def discussion(id):
    # Now you have the 'id' value!
    # You can use it to fetch the discussion content from a database, etc.

    # Example:
    discussion_content = get_discussion_content(id)  # Replace with your data fetching logic

    return render_template('discussion.html', discussion=discussion_content)

def get_discussion_content(id):
    # Replace this with your actual data fetching logic (e.g., from a database)
    # This is just a placeholder for demonstration
    discussions = {
        1: {'title': 'Aménagement convivial et sportif du bois de la grange', 'content': 'Details about discussion 1'},
        2: {'title': 'Embellissement de la parcelle du parc des Coquibus', 'content': 'Details about discussion 2'},
        3: {'title': 'Aménagement d\'un dragon glouton', 'content': 'Details about discussion 3'},
    }
    return discussions.get(id)


if __name__ == '__main__':
    app.run(debug=True)