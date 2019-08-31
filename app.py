from flask import Flask, jsonify, request
from sudoku import *
 
app = Flask(__name__)
 
@app.route('/sudoku', methods = ['POST'])
def sudoku():
    data = request.get_json()
    board = data["board"]

    result = solve(board)
    
    return jsonify({
        "board": result
    })
    
app.run(debug=True)
