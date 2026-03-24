from flask import Flask, jsonify, request


app = Flask(__name__)


# In-memory banking system collections
accounts = [
	{"id": 1, "name": "Alice", "balance": 1000.0},
	{"id": 2, "name": "Bob", "balance": 500.0},
	{"id": 3, "name": "Charlie", "balance": 250.0}
]
transactions = []


# Create a new account
@app.route('/accounts', methods=['POST'])
def create_account():
	data = request.get_json()
	if not data or not data.get("name"):
		return jsonify({"error": "Name is required"}), 400
	new_id = max([acc["id"] for acc in accounts], default=0) + 1
	new_account = {
		"id": new_id,
		"name": data["name"],
		"balance": 0.0
	}
	accounts.append(new_account)
	return jsonify(new_account), 201

# Get all accounts
@app.route('/accounts', methods=['GET'])
def get_all_accounts():
	return jsonify(accounts)
from flask import Flask, jsonify, request

# View account details
@app.route('/accounts/<int:account_id>', methods=['GET'])
def get_account(account_id):
	acc = next((acc for acc in accounts if acc["id"] == account_id), None)
	if acc:
		return jsonify(acc)
	return jsonify({"error": "Account not found"}), 404

# Deposit money
@app.route('/accounts/<int:account_id>/deposit', methods=['POST'])
def deposit(account_id):
	data = request.get_json()
	amount = data.get("amount")
	if amount <= 0:
		return jsonify({"error": "Deposit amount must be positive"}), 400
	acc = next((acc for acc in accounts if acc["id"] == account_id), None)
	if not acc:
		return jsonify({"error": "Account not found"}), 404
	acc["balance"] += amount
	transactions.append({
		"account_id": account_id,
		"type": "deposit",
		"amount": amount
	})
	return jsonify({"message": "Deposit successful", "balance": acc["balance"]})

# Withdraw money
@app.route('/accounts/<int:account_id>/withdraw', methods=['POST'])
def withdraw(account_id):
	data = request.get_json()
	amount = data.get("amount")
	if amount <= 0:
		return jsonify({"error": "Withdrawal amount must be positive"}), 400
	acc = next((acc for acc in accounts if acc["id"] == account_id), None)
	if not acc:
		return jsonify({"error": "Account not found"}), 404
	if acc["balance"] < amount:
		return jsonify({"error": "Insufficient funds"}), 400
	acc["balance"] -= amount
	transactions.append({
		"account_id": account_id,
		"type": "withdrawal",
		"amount": amount
	})
	return jsonify({"message": "Withdrawal successful", "balance": acc["balance"]})

# View transaction history
@app.route('/accounts/<int:account_id>/transactions', methods=['GET'])
def get_transactions(account_id):
	acc = next((acc for acc in accounts if acc["id"] == account_id), None)
	if not acc:
		return jsonify({"error": "Account not found"}), 404
	acc_transactions = [t for t in transactions if t["account_id"] == account_id]
	return jsonify(acc_transactions)

@app.route('/')
def home():
	return jsonify({"message": "Hello, Flask API is working!"})

if __name__ == '__main__':
	app.run(debug=True)
