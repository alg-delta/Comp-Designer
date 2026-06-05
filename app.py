# app.py
from flask import Flask, render_template, redirect, url_for, session, request
from create_db import create_db
from models import db, Moni, Arls, Dop, Sti


app = Flask(__name__)

# --- КОНФІГУРАЦІЯ FLASK ---
app.config['SECRET_KEY'] = 'your_super_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


# --- МАРШРУТИ (ROUTES) ---

@app.route('/')
def home():
    session.clear()
    """
    Головна сторінка додатку.
    """
    return render_template('index.html')

@app.route('/st', methods=['GET', 'POST'])
def st():
    if request.method == 'POST':
        sti_id = request.form.get('st')
        if sti_id:
            session['sti_id'] = int(sti_id)
            return redirect(url_for('sum'))

    sti = Sti.query.all()
    return render_template('st.html', st=sti)

@app.route('/step1', methods = ['GET', 'POST'])
def step1():
    #POST - коли натискаємо кнопку Далі
    if request.method =='POST':
        moni_id = request.form.get('mon')
        if  moni_id:
            session['moni_id'] = int(moni_id)
            #print(session)

            return redirect(url_for('step2'))

     #GET -кoли входимо на сторінку
    session.clear() #чістка session
    moni = Moni.query.all()  #отримує всі данні з таблиці moni
    return  render_template('step1.html', moni= moni)

@app.route('/step2', methods = ['GET', 'POST'])
def step2():
    if 'moni_id' not in session:
        return redirect(url_for('step1'))

    #POST - коли натискаємо кнопку Далі
    if request.method =='POST':
        arls_id = request.form.get('arl')
        if  arls_id:
            session['arl_id'] = int(arls_id)
            #print(session)

            return redirect(url_for('step3'))

     #GET -кали входимо на сторінку

    arls= Arls.query.all()  #отримує всі данні з таблиці

    return  render_template('step2.html', arls= arls)

@app.route('/step3', methods=['GET', 'POST'])
def step3():
        if 'arl_id' not in session:
            return redirect(url_for('step2'))

        # POST - коли натискаємо кнопку Далі
        if request.method == 'POST':
            dop_ids = [int(value) for value in request.form.getlist('dop')]
            session['dop_ids'] = dop_ids
            name = request.form.get('name')
            phone = request.form.get('phone')
            comment = request.form.get('comment')
            session['name']=name
            session['phone'] = phone
            session['comment'] = comment
            dop_quantities ={}
            for dop_id in dop_ids:
                many = request.form.get(f'count_{dop_id}')
                dop_quantities[dop_id] = int(many)
            session['dop_quantities'] =  dop_quantities
            return redirect(url_for('sum'))

        dops = Dop.query.all()  # отримує всі данні з таблиці Main
        return render_template('step3.html', dops=dops)

@app.route('/sum', methods=['GET', 'POST'])
def sum():
    total_price = 0
    name = session.get('name')
    phone = session.get('phone')
    comment = session.get('comment')

    sti_id = session.get('sti_id')
    sti = Sti.query.get(sti_id) if sti_id else None

    moni_id = session.get('moni_id')
    moni = Moni.query.get(moni_id) if moni_id else None

    arls_id = session.get('arl_id')
    arls = Arls.query.get(arls_id) if arls_id else None

    dop_ids = session.get('dop_ids', [])
    dops = Dop.query.filter(Dop.id.in_(dop_ids)).all() if dop_ids else []
    selected_quantities = {
        int(key): value for key, value in session.get('dop_quantities', {}).items()
    }

    moni_price = moni.price if moni else 0
    arls_price = arls.price if arls else 0
    sti_price = sti.price if sti else 0
    print(sti_id)

    total_price= moni_price + arls_price + sti_price
    for dop in dops:
        count=selected_quantities.get(dop.id)
        total_price+=count*dop.price

    return render_template('sum.html', total_price=total_price,comment=comment, sti=sti, name=name, phone=phone, moni = moni, arls = arls, dops=dops, selected_quantities=selected_quantities)



# --- ЗАПУСК ДОДАТКА ---
if __name__ == '__main__':
    # create_db()
    app.run(debug=True)
