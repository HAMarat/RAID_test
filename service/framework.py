from dao.framework import FrameworkDAO


class FrameworkService:
    def __init__(self, dao: FrameworkDAO):
        self.dao = dao

    def get_one(self, fpk):
        return self.dao.get_one(fpk)

    def get_all(self):
        return self.dao.get_all()

    def get_filter_by_language(self, filter_data):
        return self.dao.get_filter_by_language(filter_data)
