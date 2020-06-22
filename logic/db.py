from pymongo import MongoClient


class DbClient:
    def __init__(self):
        self.client = MongoClient('localhost', 27017)

    def db(self):
        return self.client['project-db']

    def get_values(self, page):
        posts = self.db().posts
        return posts.find_one({'page': page})

    def set_values(self, page, data):
        posts = self.db().posts
        posts.update_one({'page': page}, {'$set': data})
