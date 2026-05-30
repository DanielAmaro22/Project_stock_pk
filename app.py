from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///test.db'
db= SQLAlchemy(app)

class Todo(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    articulo= db.Column(db.String(10),nullable=False)
    cantidad= db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Agregado articulo: {self.articulo!r}>"


@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        art_num = request.form['content']
        art_cantidad = request.form['cantidad']
        if not art_cantidad:
            art_cantidad = 0
        else:
            art_cantidad = int(art_cantidad)

        new_art = Todo(articulo=art_num,cantidad =art_cantidad)

        try:
            db.session.add(new_art)
            db.session.commit()
            return redirect('/')
        except:
            return "Hubo un error al agregar"
    else:
        art = Todo.query.order_by(Todo.articulo).all()
        return render_template('index.html', arts = art)


if __name__ == "__main__":
    app.run(debug=True)
