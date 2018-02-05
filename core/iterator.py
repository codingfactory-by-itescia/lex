class Iterator:
    def __init__(self, db, current_hash):
        self.db = db
        self.current_hash = current_hash

    def next(self):
        current = self.db.find_one({"hash": self.current_hash})
        return self.db.find_one({"hash": current['previous_hash']})
