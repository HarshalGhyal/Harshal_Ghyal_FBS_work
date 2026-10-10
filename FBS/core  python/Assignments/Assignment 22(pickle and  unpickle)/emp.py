import pickle


class Emp:
    def __init__(self, eid, ename, basic):
        self.eid = eid
        self.ename = ename
        self.basic = basic

    def __str__(self):
        return f"ID: {self.eid}, Name: {self.ename}, Basic: {self.basic}"


FILENAME = "emp.dat"


def load_records():
    """Load all Emp records from the pickle file."""
    records = []
    try:
        with open(FILENAME, "rb") as f:
            while True:
                try:
                    records.append(pickle.load(f))
                except EOFError:
                    break
    except FileNotFoundError:
        return []
    return records


def save_records(records):
    """Save all Emp records to the pickle file (rewrites the entire file)."""
    with open(FILENAME, "wb") as f:
        for rec in records:
            pickle.dump(rec, f)