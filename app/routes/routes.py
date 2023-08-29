from flask import redirect, jsonify, render_template, request
import pandas as pd
from app.models import db, Fooditems
from flask import Blueprint

routes_bp = Blueprint(
    'routes_bp', __name__,
    template_folder='templates',
    static_folder='static'
)


@routes_bp.route('/api/fooditems')
def get_fooditems():
    df = pd.read_csv('fastfood.csv', usecols=["restaurant", "item", "calories"])
    json_data = df.values.tolist()
    print(jsonify(json_data))
    return jsonify(json_data)

@routes_bp.route('/')
def home():
    return render_template('table.html')


@routes_bp.route('/import')
def import_csv():
    title = 'Import Datasets'
    return render_templates('import.html', title=title)

@routes_bp.route('/import/upload_file', methods=['POST'])
def upload_file():

    upload_file = request.files['file']

    if uploaded_file.filename != '':
        uploaded_file.save(uploaded_file.filename)
        parse_csv(uploaded_file.filename)
    return redirect('/import')

def parse_csv(file_path):
    csv_data = pd.read_csv(file_path)
    for i, row in csv_data.iterrows():
        fooditems = Fooditems(
            restaurant=row['restaurant'],
            item=row['item'],
            calories=row['calories']
        )

        db.ssession.add(fooditem)
    db.session.commit()