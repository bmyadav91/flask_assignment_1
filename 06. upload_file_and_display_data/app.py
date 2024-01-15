from flask import Flask, redirect, request, url_for, render_template
import os

app = Flask(__name__)

folder_name = '06. upload_file_and_display_data'
app.config['UPLOAD_FOLDER'] = os.path.join(folder_name, 'uploads')

# Ensure the upload folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Home page route
@app.route("/", methods=["POST", "GET"])
def home_page():
    if request.method == "POST":
        if 'upload_file' not in request.files:
            return redirect(request.url)

        file = request.files['upload_file']

        if file.filename == "":
            return redirect(request.url)
        
        if file:
            # Save the file
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            # Redirect to a different route after saving the file
            return redirect(url_for('file_uploaded'))
    
    # List all uploaded files on the home page
    uploaded_files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template("index.html", uploaded_files=uploaded_files)

# New route to handle file_uploaded
@app.route("/file_uploaded")
def file_uploaded():
    # Display the list of uploaded files
    uploaded_files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template("index.html", uploaded_files=uploaded_files)

if __name__ == "__main__":
    app.run(debug=True)
