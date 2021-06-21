from flask import Flask, app, json, request, render_template, redirect, jsonify
from collections import OrderedDict

app = Flask(__name__)
# we want to turn off sort keys to ensure that we get the output order we want
app.config['JSON_SORT_KEYS'] = False

# database to hold the records
DB = []
# DB = [
#     {
#         "payer": "DANNON", 
#         "points": 1000, 
#         "timestamp": "2020-11-02T14:00:00Z"
#     },
#     {
#         "payer": "UNILEVER", 
#         "points": 200, 
#         "timestamp": "2020-10-31T11:00:00Z"
#     },
#     {
#         "payer": "DANNON", 
#         "points": -200, 
#         "timestamp": "2020-10-31T15:00:00Z"
#     },
#     {
#         "payer": "MILLER COORS", 
#         "points": 10000, 
#         "timestamp": "2020-11-01T14:00:00Z" 
#     },
#     {
#         "payer": "DANNON", 
#         "points": 300, "timestamp": 
#         "2020-10-31T10:00:00Z"
#     }
# ]


# landing page
@app.route('/', methods=['GET'])
def home():
    return "<h1>Fetch Rewards Coding Exercise</h1><p>This is Famim's submission for the coding exercise.</p>"

# get the point balance of all items in the DB
@app.route('/getPointBalance',methods=['GET'])
def getPointBalance():
    # create order dict to preserve 
    temp_dict = OrderedDict()
    for i in DB:
        if i['payer'] not in temp_dict:
            temp_dict[i['payer']] = 0
        temp_dict[i['payer']] += i['points']
    return jsonify(temp_dict)

# add a single transaction into the DB -- uses the form.html to get the input from the user
@app.route('/addTransaction',methods=['GET', 'POST'])
def addTransactions():
    global_dict = globals()
    if request.method == 'POST':
        # check that form is not empty
        form = request.form
        missing = []
        for k,v in form.items():
            if v == "":
                missing.append(k)

        # give feedback if input is not fully completed
        if missing:
            feedback = f"Missing fields for {', '.join(missing)}"
            return render_template('form.html', feedback=feedback)

        global_dict['DB'].append({'payer':form['payer'], 'points':int(form['points']), 'timestamp':form['timestamp']})

    return render_template('form.html')

# spend point taken in with form
@app.route('/spendPoints', methods=['POST','GET'])
def spendPoints():
    if request.method == 'POST':
        form = request.form
        if form['points'] == '':
            feedback = f'Missing points'
            return render_template('spend.html', feedback=feedback)
        
        # points user wants to spend
        points_to_spend = int(form['points'])
        want_to_spend = points_to_spend

        # sort the DB by timestamp
        # create a dict with key being payer name to ensure that their points are totaled correctly
        # update the DB after subtractions are made
        # create a list of dicts of records which are to be removed
        sorted_DB = sort_DB()
        # update the database and subtract points
        payer_dict = OrderedDict() # holds the payer and the amount of points they spend in an ordered dict
        DB_remove_list = [] # holds the index of items to be removed from global DB
        payer_list = []
        for i in range(len(sorted_DB)):
            DB_item = sorted_DB[i]
            if DB_item['points'] == 0:
                continue
            if DB_item['payer'] not in payer_dict:
                payer_dict[DB_item['payer']] = 0
            spend_points = min(points_to_spend, DB_item['points'])
            # if all points are spent from this payer
            DB[i]['points'] -= spend_points
            payer_dict[DB_item['payer']] += spend_points
            points_to_spend -= spend_points
            if points_to_spend == 0:
                for i in payer_dict:
                    temp_dict = {'payer':i, 'points':-1*payer_dict[i]}
                    payer_list.append(temp_dict)
                global_dict = globals()
                global_dict['DB'] = DB
                return jsonify(payer_list)
        if points_to_spend > 0:
            feedback = f'Not enough points to spend {want_to_spend} points'
            return render_template('spend.html', feedback=feedback)
    return render_template('spend.html')

def sort_DB(DB = DB):
    sorted_DB = sorted(DB, key=lambda x: x['timestamp'])
    global_dict = globals()
    global_dict['DB'] = sorted_DB
    return sorted_DB

@app.route('/getTransactions', methods=['GET'])
def getDB():
    return jsonify(DB)


if(__name__=='__main__'):
    app.run()