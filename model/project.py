from sys import maxsize


class Project:
    def __init__(self, id=None, p_name=None, status=None, view_status=None, description=None):
        self.id = id
        self.p_name = p_name
        self.status = status
        self.view_status = view_status
        self.description = description


    def __repr__(self):
        return f"ID: {self.id}, Name: {self.p_name}, Status: {self.status}, View_status: {self.view_status}," \
               f"Description:{self.description}"

    def __eq__(self, other):
       return self.p_name == other.p_name

    def id_or_max(pr):
        if pr.id:
            return int(pr.id)
        else:
            return maxsize