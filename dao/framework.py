from dao.model.framework import Framework


class FrameworkDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, fpk):
        return self.session.query(Framework).get(fpk)

    def get_all(self):
        return self.session.query(Framework).all()

    def get_filter_by_language(self, filter_data):
        return self.session.query(Framework).filter(Framework.name == filter_data).one()
