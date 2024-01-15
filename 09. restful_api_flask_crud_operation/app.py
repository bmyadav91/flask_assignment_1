from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3 as sql
import os

# assing db path 
db_path = os.path.join(os.path.dirname(__file__), "database.db")
app = Flask(__name__)
app.secret_key = "your_secret_key"

# home page 
@app.route("/")
def home_page():
    with sql.connect(db_path) as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM `movies`")
        records = cur.fetchall()
    return render_template("index.html", records=records)

# add movie 
@app.route("/add_movie", methods = ["GET"])
def add_movie():
    movie_name = request.args.get("m_name")
    actors = request.args.get("actor_name")
    description = request.args.get("description")
    release_date = request.args.get("release_data")

    # insert movie to database 
    with sql.connect(db_path) as con:
        cur = con.cursor()
        insert_movie = cur.execute("INSERT INTO `movies` (movie_name, actor, description, release_data) VALUES(?,?,?,?)", (movie_name, actors, description, release_date))
        if insert_movie:
            message = "alert('Movie Inserted Successfully');"
        else:
            message = "alert('Error While Inserting Movie');"
    return redirect(url_for("home_page", message=message))

# edit render 
@app.route("/edit_movie")
def edit_page():
    if request.method == "GET":
        movie_id = request.args.get("id")
        with sql.connect(db_path) as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM `movies` WHERE `id`=?",(movie_id,))
            movie = cur.fetchone()
            # movie_name = movie[1]
            # movie_actor = movie[2]
            # movie_desc = movie[3]
            # movie_release_date = movie[4]
        return render_template("edit_movie.html", movie=movie)
    
# update movie 
@app.route("/update_movie")
def update_movie():
    try:
        movie_id = request.args.get("id")
        movie_name = request.args.get("m_name")
        actors = request.args.get("actor_name")
        description = request.args.get("description")
        release_date = request.args.get("release_date")
        with sql.connect(db_path) as con:
            cur = con.cursor()
        cur.execute("UPDATE `movies` SET `movie_name`=?, `actor`=?, `description`=?, `release_data`=? WHERE `id`=?", (movie_name,actors,description,release_date,movie_id))
        con.commit()
        return redirect(url_for("home_page", message="Update Successfully"))
    except Exception as e:
        print(e)
    finally:
        return redirect(url_for("home_page"))
    


# delete movie 
@app.route("/del")
def delete_movie():
    del_id = request.args.get("id")
    with sql.connect(db_path) as con:
        cur = con.cursor()
        cur.execute("DELETE FROM `movies` WHERE id=?",(del_id,))
        cur.fetchone()
        return redirect(url_for("home_page"))  

# run Environment
if __name__ == "__main__":
    app.run(debug=True)