from dbm import DB
try:
    db = DB()
    print(db.submit_message("John Doe", "This is a test message"))
    
    # Fetch the 5 most recent messages
    messages = db.fetch_messages(5)
    for message in messages:
        print(message)
    
    db.close()

except Exception as e:
    print(e)
