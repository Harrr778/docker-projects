from flask import Flask
	import psycopg2
	import os
	
	app = Flask(__name__)
	
	DB_HOST = os.environ.get('DB_HOST', 'db')
	DB_NAME = os.environ.get('DB_NAME', 'testdb')
	DB_USER = os.environ.get('DB_USER', 'testuser')
	DB_PASS = os.environ.get('DB_PASS', 'testpass')
	
	def get_connection():
	    return psycopg2.connect(
	        host=DB_HOST,
	        dbname=DB_NAME,
	        user=DB_USER,
	        password=DB_PASS
	    )
	
	@app.route("/")
	def index():
	    conn = get_connection()
	    cur = conn.cursor()
	    cur.execute("SELECT NOW();")
	    result = cur.fetchone()
	    cur.close()
	    conn.close()
	    return f"Hello! Current time from DB: {result[0]}"
		
	if __name__ == "__main__":
	    app.run(host="0.0.0.0", port=5000)
